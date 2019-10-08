from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView
from blog.models import Post

class SearchListView(ListView):
    
    template_name = 'search/view.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchListView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        return context
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q','lorem')
        if query:
            lookups = Q(title__icontains=query)
            return Post.objects.filter(lookups).distinct()
        return Post.objects.none()