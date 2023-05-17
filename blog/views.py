from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category
from .forms import PostForm,EditForm
from django.urls import reverse_lazy
# Create your views here.
# def home(response):
#     return render(response,"home.html",{})

class HomeView(ListView):
    model=Post
    template_name='home.html'
    # ordering=['-post_date']
    ordering=['-id']

class ArticleDetailView(DetailView):
    model=Post
    template_name='article_details.html'

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'
    # fields='__all__'
    #fields=('title','body')

class UpdatePostView(UpdateView):
    model=Post
    form_class=EditForm
    template_name='update_post.html'

class DeletePostView(DeleteView):
    model=Post
    template_name='delete-post.html'
    success_url=reverse_lazy('home')

class AddCategoryView(CreateView):
    model=Category
    # form_class=PostForm
    template_name='add_category.html'
    fields='__all__'

def CategoryView(request,cats):
    category_posts=Post.objects.filter(category=cats.replace('-',' '))
    return render(request,'category.html',{'cats':cats.replace('-',' '),'cat_post':category_posts})