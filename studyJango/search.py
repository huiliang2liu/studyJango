from django.shortcuts import render,redirect
from django.http import HttpResponse

def search_form(request):
    return render(request,'search_form.html')

def search(request):
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        message='你搜索的内容为:'+request.GET['q']
    else:
        message='你提交了空表单'
    return HttpResponse(message)


def post(request):
    ctx = {}
    if request.POST:
        ctx['rlt']=request.POST['q']
    return render(request,'post.html',ctx)

def year_month(request,year,month):
    print(year,month)
    return HttpResponse("year:{},month:{},path:{}".format(year,month,request.path))


def main(request):
    token=request.COOKIES.get('token')
    if not token:
        return redirect('/user/login')
    return render(request, "main.html", {'username': token2user(token)})
    pass

def token2user(token):
    return token
