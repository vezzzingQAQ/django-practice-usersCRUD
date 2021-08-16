from django.urls import path
from myapp import views
'''
path("",views.index,name="index"),
path("addUserZS",views.addaValue,name="addZS"),
path("deleteUser2",views.deleteaValue,name="delete2"),
path("changeUser4",views.changeValue,name="change4"),
path("queryValue",views.queryValue,name="query"),
'''
#以上为测试数据******
urlpatterns=[
    path("",views.index,name="index"),
    #users信息操作
    path("users",views.indexUsers,name="indexusers"),
    path("users/add",views.addUsers,name="addusers"),
    path("users/insert",views.insertUsers,name="insertusers"),
    path("users/del/<int:userId>",views.delUsers,name="delusers"),
    path("users/edit/<int:userId>",views.editUsers,name="editusers"),
    path("users/update",views.updateUsers,name="updateusers"),
]