from rest_framework import serializers
from .models import Blog, Comment

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'intro', 'body', 'image', 'date_added']

class CommentSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Comment
        fields = ['email', 'author', 'body','post']