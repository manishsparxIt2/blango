from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

def index(request):
  
  posts = Post.objects.filter(published_at__lte=timezone.now())
  
  if request.user.is_active:
    if request.method=="POST":

      if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.content_object = post
        comment.reate=request.user
        comment.save()
        return redirect(request.path_into)
    else:
      comment_form=CommentFomr()
  else:
    comment_form = None

  return render(request, "blog/index.html", {"posts": posts})
  # Create your views here.
def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post": post})
