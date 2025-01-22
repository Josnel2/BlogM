from django.contrib import admin
from .models import CreateBlog, Comment

# Register your models here.
admin.site.register(CreateBlog)
admin.site.register(Comment)
