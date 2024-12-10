from django.urls import path
from . import views
from .views import  admin_dashboard

urlpatterns = [
    path('', views.home, name='home_page'),
    path('registerpage', views.registerpage),
    path('loginpage', views.loginpage),
    path('adminlogin', views.adminlogin),
    path('adminhome', views.admin_dashboard, name='admin_dashboard'),  # Ensure this line has the name 'admin_dashboard'
    path('pending/', views.pending, name='pending_list'),
    path('approve/<int:id>/', views.approve, name='approve'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('approved', views.approved, name='approve_list'),
    path('approved/api', views.approved_api, name='approve_api'),
    path('delete/approved_user/<int:id>/', views.delete_approved_user, name='delete_approved_user'),
    path('metrics', views.metrics),
    path('health', views.health),
    path('cardio', views.cardio),
    path('report/', views.report, name='report'),  # No username needed
    path('report/<str:username>/', views.report, name='report_with_username'),  # Username is optional
    path('training',views.training_plan),
    path('tips',views.tips),
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
]

