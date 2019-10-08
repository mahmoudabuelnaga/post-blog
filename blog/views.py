from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post

class PostListView(ListView):
    model               = Post
    template_name       = 'blog/post/list.html'
    queryset            = Post.published.all()
    context_object_name = 'posts'
    # paginate_by         = 1

def Post_detail_view(request, year, month, day, slug):
    post = get_object_or_404(
        Post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=slug,
    )
    context = {
        'post':post,
    }
    return render(request, 'blog/post/detail.html', context)
