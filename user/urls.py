from django.urls import path,include
from . import views
from django.contrib import admin




urlpatterns = [
   path('',views.index,name="index"),
   path('cars',views.cars,name="cars"),
   path('registration',views.registration,name="registration"),
   path('login',views.login_view,name="login"),
   path('admin_dashboard',views.admin_dashboard,name="admin_dashboard"),
   path('admin_login',views.admin_login,name="admin_login"),
   path('add_car_details',views.add_car_details,name="add_car_details"),
   path('admin_logout',views.admin_logout,name="admin_logout"),
   path('user_logout',views.user_logout,name="user_logout"),
   path('user_dashboard',views.user_dashboard,name="user_dashboard"),
   path('single_car_details/<int:id>',views.single_car_details,name="single_car_details"),
   path('purchase/', views.purchase, name='purchase'),
   path('contact_details', views.contact_details, name='contact_details'),
   path('available_cars', views.available_cars, name='available_cars'),

]