from django.http import HttpResponse
from django.shortcuts import redirect

def index(request):
	"""
	访问首页
	:param request:
	:return:
	"""
	return HttpResponse("index")

def login(request):
	return redirect("/index")

def reg(request):
	return redirect("reg")

def add_cart(request):
	return HttpResponse("add_cart")