from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('index',views.index,name='index'),     
    path('<int:id>',views.view_employee,name='view_employee'),
    path('add/',views.add,name='add'),
    path('edit/<int:id>/',views.edit, name='edit'),
    path('delete/<int:id>/',views.delete, name='delete'),
    path('login',views.login,name='login'),

    
]
