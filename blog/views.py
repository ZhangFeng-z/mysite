from django.shortcuts import render_to_response,get_object_or_404
from django.core.paginator import Paginator
from django.conf import settings
from .models import Blog,BlogType

# Create your views here.
#这个区域写处理方法  用来点击之后展示出来的视图

#获取博客的分类来 展示给前端页面
def blog_list(request):
	blogs_all_list=Blog.objects.all()
	paginator=Paginator(blogs_all_list,settings.EACH_PAHE_BLOGS_NUMBER) # 分页器实例化 每10页进行分页
	page_num=request.GET.get('page',1)  # 获取url的当前页面参数   不一定是int类型的
	page_of_blogs=paginator.get_page(page_num)  # 会自动转换传过来的值  如 str转int
	currentr_page_num = page_of_blogs.number  # 获取当前页码
#	page_range=[ currentr_page_num - 2,currentr_page_num - 1 ,currentr_page_num ,currentr_page_num + 1 ,currentr_page_num +2 ]  
	# 获取当前页码 前后俩个页码号 
	page_range = [x for x in range(int(currentr_page_num)-2,int(currentr_page_num)+3) if 0<x<=paginator.num_pages]
	# 加上省略号
	if page_range[0] -1>=2:
		page_range.insert(0,'...')
	if paginator.num_pages - page_range[-1] >=2:
		page_range.append('...')
	# 页码前面加上 1 和尾页
	if page_range[0] !=1:
		page_range.insert(0,1) # insert 插入,第一个位置,加如数字1
	if page_range[-1] !=paginator.num_pages:
		page_range.append(paginator.num_pages)  # append 添加

	context={}
	context['blogs']=page_of_blogs.object_list      # 获取全部博客分类 返回给前端展示 
	context['page_of_blogs']=page_of_blogs   #获取一个页码信息
	context['page_range']=page_range
	context['blog_types']=BlogType.objects.all()  
	return  render_to_response('blog/blog_list.html',context)  

#根据主键  获取具体的博客内容
def blog_detail(request,blog_pk):  
	context={}
	context['blog']=get_object_or_404(Blog,pk=blog_pk)
	return render_to_response('blog/blog_detail.html',context)

#点击分类可以调转的方法
def blog_with_type(request,blog_type_pk):
	context={}
	blog_type=get_object_or_404(BlogType,pk=blog_type_pk)
	#context['blogs']=Blog.objects.filter(blog_type=blog_type)
	#context['blog_types']=BlogType.objects.all()  
	blogs_all_list= Blog.objects.filter(blog_type=blog_type)    # 获取分类下的博客

	paginator=Paginator(blogs_all_list,settings.EACH_PAHE_BLOGS_NUMBER) # 分页器实例化 每10页进行分页
	page_num=request.GET.get('page',1)  # 获取url的当前页面参数   不一定是int类型的
	page_of_blogs=paginator.get_page(page_num)  # 会自动转换传过来的值  如 str转int
	currentr_page_num = page_of_blogs.number  # 获取当前页码
#	page_range=[ currentr_page_num - 2,currentr_page_num - 1 ,currentr_page_num ,currentr_page_num + 1 ,currentr_page_num +2 ]  
	# 获取当前页码 前后俩个页码号 
	page_range = [x for x in range(int(currentr_page_num)-2,int(currentr_page_num)+3) if 0<x<=paginator.num_pages]
	# 加上省略号
	if page_range[0] -1>=2:
		page_range.insert(0,'...')
	if paginator.num_pages - page_range[-1] >=2:
		page_range.append('...')
	# 页码前面加上 1 和尾页
	if page_range[0] !=1:
		page_range.insert(0,1) # insert 插入,第一个位置,加如数字1
	if page_range[-1] !=paginator.num_pages:
		page_range.append(paginator.num_pages)  # append 添加

	context={}
	context['blog_type']=blog_type
	context['blogs']=page_of_blogs.object_list      # 获取全部博客分类 返回给前端展示 
	context['page_of_blogs']=page_of_blogs   #获取一个页码信息
	context['page_range']=page_range
	context['blog_types']=BlogType.objects.all()  
	return render_to_response('blog/blog_with_type.html',context)
