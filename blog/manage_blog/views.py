from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView
from .models import CreateBlog, Comment
from .serializers import CreateBlogSerializer, CommentSerializer



class commentCreateView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
class BlogListView(ListAPIView):
    queryset = CreateBlog.objects.all()
    serializer_class = CreateBlogSerializer
    
    def get_queryset(self):
        return CreateBlog.objects.all().order_by('-date_added')
    
class BlogCreateView(CreateAPIView):
    queryset = CreateBlog.objects.all()
    serializer_class = CreateBlogSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    

class BlogDetailView(APIView):
    def get(self, request, slug, format=None):
        try:
            blog = CreateBlog.objects.get(slug=slug)
        except CreateBlog.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        blog_serializer = CreateBlogSerializer(blog)
        
        comments = Comment.objects.filter(post=blog)
        comments_serializer = CommentSerializer(comments, many=True)
        return Response({
            "article": blog_serializer.data,
            "comments": comments_serializer.data
        })
