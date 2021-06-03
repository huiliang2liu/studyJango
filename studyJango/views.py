from django.http import HttpResponse
from django.shortcuts import render
import datetime

def hello(request):
    return HttpResponse("Hello world")

def runnob(request):
    context={}
    context['hello']='Hello World'
    context['name']='刘慧良'
    context['list']=['list','list1','list2']
    context['dir']={'dir1':'dadad','dir2':'eqeqeq'}
    context['name']='刘慧良'
    context['fileSize']=1024*1024
    context['date']=datetime.datetime.now()
    context['views_str']="<a href='https://www.runoob.com/'>点击跳转</a>"
    return render(request,'runoob.xhtml',context)