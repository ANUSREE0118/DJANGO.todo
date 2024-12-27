from django.urls import path
from . import views
urlpatterns=[
    path('', views.home,name='home-page'),
    path('register/',views.register,name='register'),
    path('login/',views.loginpage,name='loginpage'),
    path('logout/',views.logoutview,name='logout'),
    path('DeleteTask/<str:name>/',views.DeleteTask,name='deletes'),
    path('update/<str:name>/',views.Update,name='update'),
    # path('notask/<str:mane>/ ',views.notask,name='notask'),
  
]
