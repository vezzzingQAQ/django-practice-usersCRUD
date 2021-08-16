from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Users
# Create your views here.
def index(request):
    return(HttpResponse("首页"))

def addaValue(request):
    ob=Users()
    ob.name="zs"
    ob.age=20
    ob.phone="123456789"
    ob.save()
    return(HttpResponse("added"))

def deleteaValue(request):
    mod=Users.objects#获取user的Model对象
    user=mod.get(id=2)
    print(user.name)
    user.delete()
    return(HttpResponse("deleted"))

def changeValue(request):
    ob=Users.objects.get(id=4)
    print(ob.name)
    ob.name="得得得得得得得"
    ob.age=33
    ob.save()
    return(HttpResponse("changed"))
