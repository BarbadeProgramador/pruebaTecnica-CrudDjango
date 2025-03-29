from django.contrib import admin
from django.urls import path
from .views import index,template_create,create,delete,template_update ,update
urlpatterns = [
    
    path('',index , name='route_home'),
    
    # routes create
    path('crear/', template_create , name='route_template_create' ),
    path('crear/guardar', create , name='route_create' ),    
    
    # routes delete 
    path('eliminar/<int:id>/', delete, name='route_delete'),


    # routes update
    path('editar/<int:id>/',template_update , name='route_template_update'),
    path('editar/guardar/<int:id>', update,  name='route_update'),
    
    
]
