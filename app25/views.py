from django.shortcuts import render,get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from .models import Post
from django.utils import timezone
from django.shortcuts import render
from django.shortcuts import render_to_response 
from django.http import HttpResponseRedirect 
from django.contrib.auth.forms import UserCreationForm 
from django.template.context_processors import csrf
#from django.contrib.auth.models import User, Group
#from rest_framework import viewsets
#from serializers import UserSerializer, GroupSerializer
# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.filter(title__contains = 'first')
    #form2 = commentform()
    #if request.method == "POST":
        #form2 = commentform(request.POST)
        #fo = form2.save(commit=False)
	#fo.save()
    #commentsa = comments.objects.all()
    return render(request, 'app25/post_list.html', {'posts':posts})
def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'app25/post_detail.html', {'post': post})
def post_new(request):
    if request.method == "POST":

        form = PostForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)

            post.author = request.user

            post.published_date = timezone.now()

            post.save()

            return redirect('post_detail', pk=post.pk)

    else:

        form = PostForm()

    return render(request, 'app25/post_edit.html', {'form': form})
def post_edit(request, pk):

    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":

        form = PostForm(request.POST, instance=post)

        if form.is_valid():

            post = form.save(commit=False)

            post.author = request.user

            post.published_date = timezone.now()

            post.save()

            return redirect('post_detail', pk=post.pk)

    else:

        form = PostForm(instance=post)

    return render(request, 'app25/post_edit.html', {'form': form})

#def post_login(request):
    #if request.method == "POST":
        #form1 = loginform(request.POST)
        #if form1.is_valid():
            #fo = form1.save()
            #return redirect('post_list')
    #else:
        #form1 = loginform()
    #return render(request,'app25/post_login.html',{'form1': form1})

def post_fav(request):
    fav = Post.objects.filter(favourites == True)
    print fav
    return render(request,'app25/post_fav.html',{'fav':fav})

def add_fav(request,pk):
    post = get_object_or_404(Post, pk=pk)
    #if request.method == "POST":
    form = PostForm(instance=post)
        #if form.is_valid():
    print "yeh"
    post = form.save(commit=False)
    if post.favourites == False:
        post.favourites = True
    else:
        post.favourites = False 
    post.save()
    print "hello"
    return redirect('post_list')
    #return render(request, 'app25/a.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register/complete')

    else:
        form = UserCreationForm()
    token = {}
    token.update(csrf(request))
    token['form'] = form

    return render_to_response('registration/registration_form.html', token)

def registration_complete(request):
    return render_to_response('registration/registration_complete.html')

def loggedin(request):
    return render_to_response('registration/loggedin.html')


#class UserViewSet(viewsets.ModelViewSet):
    #"""
    #API endpoint that allows users to be viewed or edited.
    #"""
 #   queryset = User.objects.all().order_by('-date_joined')
  #  serializer_class = UserSerializer


#class GroupViewSet(viewsets.ModelViewSet):
 #   """
  #  API endpoint that allows groups to be viewed or edited.
    #"""
    #queryset = Group.objects.all()
    #serializer_class = GroupSerializer

