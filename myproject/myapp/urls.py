from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('impact/', views.impact, name='impact'),
    path('about/', views.about, name='about'),
    path('policies/',views.policies, name='policies'),
    path('education/', views.education, name='education'),
    path('unpage/',views.unpage, name='unpage')
]
