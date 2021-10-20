from.import views 
from django.urls import path

urlpatterns =[
    path("",views.index,name="index"),
    path("Reham",views.Reham,name="reham"),
    path("Rita",views.Rita,name="rita"),
    path("<str:name>",views.greet,name="greet")
]