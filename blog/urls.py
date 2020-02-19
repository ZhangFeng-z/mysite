from django.urls import path
from . import views
#设置app 的路由
urlpatterns = [
	path('',views.blog_list,name='blog_list'),  #此处是点击博客后的链接
	path('<int:blog_pk>',views.blog_detail,name="blog_detail"),
	path('type/<int:blog_type_pk>',views.blog_with_type,name="blog_with_type"),
]
