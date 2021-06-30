from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='rybka-home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='rybka-detail'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='rybka-delete'),
    path('post/new/', views.PostCreateView.as_view(), name='rybka-create'),
]
