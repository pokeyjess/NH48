from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from nh48_app.models import Post
from nh48_user.models import NHUser
from nh48_app.forms import PostForm

def index(request):
    post_list = Post.objects.all().order_by('-time_posted')
    return render(request, "index.html", {"post_list": post_list})

def post_form_view(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if 'mountain_image' not in request.FILES:
            return HttpResponse("Please select an image")
        new_post = Post.objects.create(poster=request.user, caption=request.POST['caption'], mountain=request.POST['mountain'], mountain_image=request.FILES['mountain_image'])
        return redirect('post', new_post.pk)
    form = PostForm()
    return render(request, 'generic_form.html', {'form': form})
    
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    poster_id = post.poster.id
    return render(request, 'post_detail.html', {'post': post})
