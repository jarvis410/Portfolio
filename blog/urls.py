from django.urls import path
from blog import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.blog, name='blog'),
]
