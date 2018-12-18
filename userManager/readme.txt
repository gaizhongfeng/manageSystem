1.数据库设计
class classes(models.Model):
	caption=models.CharField(max_length=32)

class Student(models.Model):
	name=models.CharField(max_length=32)
	cls=models.ForignKey('classes')
	username = models.CharField(max_length=32)
	passworf = models.CharField(max_length=32)



class Teacher(models.Model):
	name = models.CharField(max_length=32)
	username = models.CharField(max_length=32)
	passworf = models.CharField(max_length=32)
#第三张表

2.登录、注册
	提交表单：
		form
		Ajax

	-登录
		-成功：记住登录状态<-->保持会话
		-失败：错误提示

技术:
    将用户名放到 cookie 中



cookie:
    就是保存在浏览器端的键值对
    1.保存在用户浏览器
    2.可以主动清除
    3.可以被‘伪造’
    4.跨域不共享
    参数:
        path: / 表示cookie 全局有效
        max_age: cookie的过期时间
        expires: cookie的过期时间(IE)
        domain: 设置 可以访问cookie的域名

    客户端浏览器上操作 cookie
            dom 方式
            jQuery 插件: jquery.cookie.js


cookie与session:
   cookie 是放在浏览器端的键值对，发送到服务端的时候依附在请求头中，服务端返回的时候依附于响应头中

   session依赖于cookie来实现

cookie 的应用：
        登录认证
                敏感信息不宜放在cookie中，放在数据库中会频繁的操作数据库


用户管理：
    1.用户登录
    2.注册
    3.注销
    4.后台管理菜单
    5.班级操作
    6.老师、学生
知识点：
    1.form 表单
    2.ajax
    3.布局，模板
    4.序列化
    5.ajax 相关的
    6.分页
    7.xss攻击
    8.CSRF




url-> def 函数    FBV
url-> 类          CBV


CBV：
    url-> 类.as_view()



自定义分页
    - 数据从数据库来






前端用 name相同的 CheckBox 或者select 标签的时候，向后台传递多个值
后台可以用 request.POST.getlist('k') 进行获取

obj.cls.set(cls_li) set 方法用于更新第三张表 比如obj 和 cls 现在有关系(1,2) (1,3)
cls_li 里的关系是(1,3)
执行完set 方法之后obj和cls的关系只剩下 （1,3）



DOM 对象： obj = document.getElementById('sel')
DOM 对象装换成 jQuery对象 ： j = $(obj)
jQuery 对象转换成DOM 对象： obj = $('.sel')[0]


使用form 上传文件，form 标签必须加enctype="multipart/form-data" 属性
添加这个属性后， 后台获取 要在request 的FILES 里边获取:file = req.FILES.get("file")





功能：
    -数据库
        一对一
        一对多
        多对多
     -自定义分页
     -前台循环显示后台数据
     -后台接收select 发过来的多条数据
     -使用 set 方法更新数据
     -url:
        类的方式
        函数的方式
      -简单的页面布局
      -模态对话框
      -两个select 标签的值来回移动(对老师的课程进修修改)
      -文件上传:
            -form 表单上传文件
            -Ajax上传文件
            -基于form 表单和iframe自己实现ajax 请求



