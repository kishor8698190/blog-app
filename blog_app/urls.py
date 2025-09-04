from django.urls import path
from .views import CreateBlogPostAPIView, MineBlogPostAPIView, CreateCommentAPIView

urlpatterns = [
    path('api/posts/', CreateBlogPostAPIView.as_view()),
    path('api/posts/mine/', MineBlogPostAPIView.as_view()),
    path('api/posts/<int:blog_id>/comments/', CreateCommentAPIView.as_view())
]
