from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm
from .models import Post #The dot before models means current directory or current application


# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	#Note that we need to use exactly the same name as the one we specified in urls (pk). Omitting this variable is incorrect and will result in an error!
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False) #commit=False means that we don't want to save the Post model yet – we want to add the author first
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form':form})