from rest_framework import serializers
from .models import CreateBlog, Comment

class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateBlog
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Comment
        fields = ['email', 'author', 'body','post']