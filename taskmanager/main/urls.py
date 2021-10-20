from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about-us', views.personal_area, name='personal_area'),
    path('logout/', views.user_logout, name='logout'),

]