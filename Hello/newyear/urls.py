from django.urls import path
from . import views

urlpatterns=[
    # path("",views.index,name=""),
    # path ("<str:name>",views.vname,name="varname")
    path("",views.chrismas,name="chrismas"),
    path("<int:number>",views.Birth,name="birthday"),
]