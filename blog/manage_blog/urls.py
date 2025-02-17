from.views import BlogListView, BlogDetailView, BlogCreateView,commentCreateView
from django.urls import path

app_name = 'manage_blog'
urlpatterns = [
    path('blogs/<slug:slug>', BlogDetailView.as_view(), name='blog-detail'),
    path('blogs', BlogListView.as_view(), name='blog-list'), 
    path('create', BlogCreateView.as_view(), name='blog-create'),
    path('comment', commentCreateView.as_view(), name='comment-create'),
]
