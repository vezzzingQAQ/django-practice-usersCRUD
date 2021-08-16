from django.urls import path
from . import views
urlpatterns=[
	path("",views.index,name="index"),
    path("addUserZS",views.addaValue,name="addZS"),
    path("deleteUser2",views.deleteaValue,name="delete2"),
    path("changeUser4",views.changeValue,name="change4"),
]