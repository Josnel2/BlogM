from django.db import models

# Create your models here.
class Blog(models.Model): #comment tu appelles un modèle CreateBlog ?
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='media/', null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_added']
        
    def __str__(self):
        return self.title

class Comment(models.Model):
    post= models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    email= models.EmailField()
    author = models.CharField(max_length=255, default='Anonymous')  
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_added']