from django.urls import path
from .views import PostListView, Post_detail_view
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', Post_detail_view, name='post_detail'),
    
]