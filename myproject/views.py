from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from django.http import HttpResponse, JsonResponse
from .models import BlogPost
from .forms import BlogPostForm


def homepage(request):
    if request.method == 'POST':  # If the request method is POST
        return JsonResponse({"message": "This is a POST request"})
    else:  # Default to GET if no other method is specified
        return HttpResponse("This is a GET request")


# ListView for displaying blog posts
class BlogPostListView(ListView):
    model = BlogPost
    template_name = 'blog_post_list.html'
    context_object_name = 'posts'


# CreateView for creating new blog posts
class BlogPostCreateView(LoginRequiredMixin, CreateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'create_blog_post.html'
    success_url = reverse_lazy('blog_post_list')


