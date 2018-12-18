
class PageHelper:
    def __init__(self):
        pass


    def getStart(self,current_page,pre_page=10):
        return (current_page - 1) * pre_page
    def getEnd(self,current_page,pre_page=10):
        return  current_page*pre_page

    # pre_page:每页显示的记录数
    def page_str(self,toal_count,current_page,base_url,pre_page=10):
        # 每页显示10条数据
        # divmod 方法返回两个值一个是商，一个是余数
        v, a = divmod(toal_count, pre_page)
        if a != 0:
            v += 1
        pager_list = []
        if current_page > 1:
            pager_list.append('<a href = "%s?p=%s" >上一页</a>' % (base_url,current_page - 1))

        # 总页数<=11
        #     page_start=1
        #     page_end= 总页数
        #
        # 总页数 > 11
        #     当前页<6
        #         page_start=1
        #         page_end=11
        #     else
        #         page_start = 当前页 -5
        #          page_end = 当前页 + 6
        #          if page_end> 总页数
        #               page_end = 总页数
        #
        #
        if v <= 11:
            page_start = 1
            page_end = v + 1
        else:
            if current_page < 6:
                page_start = 1
                page_end = 12
            else:
                page_start = current_page - 5
                page_end = current_page + 6
                if page_end > v:
                    page_start = v - 10
                    page_end = v + 1

        for i in range(page_start, page_end):
            # 为当前页设置class，让用户可以知道当前是第几页
            if i == current_page:
                pager_list.append('<a class="active" href = "%s?p=%s" >%s</a>' % (base_url,i, i))
            else:
                pager_list.append('<a href = "%s?p=%s" >%s</a>' % (base_url,i, i))


        # pager = '''
        #     <a href="classes.html?p=1">1</a>
        #     <a href="classes.html?p=2">2</a>
        #     <a href="classes.html?p=3">3</a>
        # '''

        if current_page < v:
            pager_list.append('<a href = "%s?p=%s" >下一页</a>' % (base_url,current_page + 1))

        pager = "".join(pager_list)
        return pager