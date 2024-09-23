from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm


def homepage(request):
    if request.method == 'POST':  # If the request method is POST
        return JsonResponse({"message": "This is a POST request"})
    else:  # Default to GET if no other method is specified
        return HttpResponse("This is a GET request")


def create_blog_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the data to the BlogPost model
            return redirect('blog_post_list')  # Redirect to the list view after saving
    else:
        form = BlogPostForm()

    return render(request, 'create_blog_post.html', {'form': form})


def blog_post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_post_list.html', {'posts': posts})
