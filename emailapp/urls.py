
from django.urls import path
from .import views

urlpatterns = [
    path('',views.add,name='add'),
    path('adddetails',views.adddetails,name='adddetails'),
]