from django.urls import path

from BlogApp import views

urlpatterns = [
    path('',views.blogs,name='blogs'),
    path('delete/<int:blogid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update')

]