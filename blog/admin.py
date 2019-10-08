from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display         = ('title','id','slug','author','status')
    list_filter          = ('author','status','publish','created')
    search_fields        = ('title','body')