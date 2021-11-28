from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('image/', views.image,name='image'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('video/', views.video,name='video'),
    path('pdf/', views.pdf,name='pdf'),
    path('index/', views.index,name='index'),
    path('update/',views.update,name='update'), 
    path('deleteimage/<int:taskid>/',views.deleteimage,name='deleteimage'),
    path('deletevideo/<int:taskid>/',views.deletevideo,name='deletevideo'),
    path('deletepdf/<int:taskid>/',views.deletepdf,name='deletepdf'),
    path('updateimage/<int:id>/',views.updateimage,name='updateimage'),
    path('updatevideo/<int:id>/',views.updatevideo,name='updatevideo'),
    path('updatepdf/<int:id>/',views.updatepdf,name='updatepdf'),



]
