from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,Http404
from django.contrib.auth.models import User
from django.views.generic import ListView
from .models import Article
from .forms import ArticleCreateForm


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'posts'  # Default: object_list
    paginate_by = 5
    queryset = Article.objects.all()  # Default: Model.objects.all()
    ordering = ['-created_on']

# def article_list(request):
#     posts = Article.objects.all()
#     context = {
#         'posts': posts
#     }
#     return render(request,'articles/article_list.html',context)

def article_detail(request,pk=None):
    post  = get_object_or_404(Article,pk=pk)
    context = {
        'post':post
    }
    return render(request,'articles/article_detail.html',context)

def article_create(request):
    form = ArticleCreateForm(request.POST or None)
    if form.is_valid():
        form.instance.created_by = request.user
        form.save()
        return redirect('article-list')
    context = {
        'form':form
    }
    return render(request,'articles/article_create.html',context)

def article_update(request,pk=None):
    post = get_object_or_404(Article,pk=pk)
    form = ArticleCreateForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('article-list')
    context = {
        'form':form
    }
    return render(request,'articles/article_update.html',context)

def article_delete(request,pk=None):
    post = get_object_or_404(Article,pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('article-list')
    context = {
        'post':post
    }
    return render(request,'articles/article_delete.html',context)