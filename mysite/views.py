from django.shortcuts import render_to_response

#这是应该首页的处理方法
def home(request):
	context={}
	return render_to_response('home.html',context)