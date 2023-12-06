from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.BlogView.as_view(), name ='blog-list'),
    path('<int:id>/', views.BlogDetailView.as_view(), name='blog-detail')
]