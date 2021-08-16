from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render

from myapp.models import Users
# Create your views here.
'''
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

def queryValue(request):
    def listAll(currentlist):
        for u in currentlist:
            print(u.id,u.name,u.age,u.addTime)

    mod=Users.objects

    #获取全部数据
    ulist=mod.all()
    listAll(ulist)

    #数据过滤
    print("name=额")
    ulist_filtered=mod.filter(name="额")
    listAll(ulist_filtered)

    #获取年龄大于20岁的
    print("age>20")
    ulist_filtered=mod.filter(age__gt=20)
    listAll(ulist_filtered)

    #获取年龄大于等于20岁的
    print("age>=20")
    ulist_filtered=mod.filter(age__gte=20)
    listAll(ulist_filtered)

    #获取年龄小于等于20岁的
    print("age<=20")
    ulist_filtered=mod.filter(age__lte=20)
    listAll(ulist_filtered)

    #排序
    print("ordered")
    ulist_ordered=mod.order_by("age")
    listAll(ulist_ordered)

    #切片
    print("sliced")
    ulist_sliced=mod.order_by("age")[:4]
    listAll(ulist_sliced)

    return(HttpResponse("queried"))
'''
#以上为测试数据
#项目**********
#浏览用户信息
#加载添加用户信息表单
#执行用户信息添加
#执行用户信息删除
#加载用户信息修改表单
#执行用户信息修改
#***************
def index(request):
    return(render(request,"myapp/users/mainPage.html"))
#浏览用户信息
def indexUsers(request):
    try:
        ulist=Users.objects.all()
        uploadContext={"userslist":ulist}
        return(render(request,"myapp/users/index.html",uploadContext))#加载模板
    except:
        return(HttpResponse("没有找到用户信息(○´･д･)ﾉ"))
#加载添加用户信息表单
def addUsers(request):
    return(render(request,"myapp/users/add.html"))
#执行用户信息添加
def insertUsers(request):
    try:
        ob=Users()
        #从表单获取要添加的信息
        ob.name=request.POST['name']
        ob.age=request.POST['age']
        ob.phone=request.POST['phone']
        ob.save()
        uploadContext={"info":"添加成功"}
    except:
        uploadContext={"info":"添加失败"}
    return(render(request,"myapp/users/info.html"),uploadContext)
#执行用户信息删除
def delUsers(request,userId=0):
    pass
#加载用户信息修改表单
def editUsers(request,userId=0):
    pass
#执行用户信息修改
def updateUsers(request):
    pass

