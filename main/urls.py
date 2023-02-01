from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('news/', views.news, name='news'),
    path('analysis/', views.analysis, name='analysis'),
    path('services/', views.services, name='services'),

    # Auth
    path('signup/', views.signupuser, name="signupuser"),
    path('login/', views.loginuser, name="loginuser"),
    path('logoutuser/', views.logoutuser, name="logoutuser"),

]
