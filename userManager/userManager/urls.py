"""userManager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app01 import views
from django.conf.urls import  url,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('login.html',views.login),

    #url指向一个类       views.类名.as_view()  类一定要继承views.View
    url('login.html',views.Login.as_view()),

    url(r'^index.html',views.index),
    url(r'^logout.html',views.logout),
    url(r'^classes.html',views.handle_classes),
    url(r'^add_classes.html',views.handle_add_classes),
    url(r'^student.html',views.handle_student),
    url(r'^teacher.html',views.handle_teacher),
    url(r'^add_teacher.html',views.add_teacher),
    url(r'^upload.html',views.upload),
    url(r'^edit_teacher-(\d+).html',views.edit_teacher),
    path('js_cookie.html',views.js_cookie),
]
