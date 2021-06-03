from django.http import HttpResponse
from django.shortcuts import render,redirect

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    if request.method == "POST":
        req=redirect('/main')
        username=request.POST.get('user_name')
        pwd=request.POST.get('pass')
        req.set_cookie('token',username)
        return req
        # return render(request,"main.html",{'username':username})
    # response=HttpResponse("")
    # response.
    return HttpResponse(status=400)