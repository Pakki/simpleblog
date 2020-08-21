from django.shortcuts import render
from django.http import request, HttpRequest, HttpResponse
from .models import Category, Tag, Post, ViewsCount
from django.views.generic import ListView, DetailView, CreateView
from django.db.models import F

#------

class HomePosts(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    allow_empty = True
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Блог главная'
        return context


class PostsByCategory(HomePosts):

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['title'] = f'{Category.objects.get(slug=self.kwargs["slug"])}'
        return context


    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs["slug"]).select_related("category")


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['title'] = f'{self.object.title}'
        counter, created = ViewsCount.objects.get_or_create(post=self.object, defaults={'count': 0})     
        counter.count += 1
        counter.save()
        context['views'] = counter.count
        return context


class PostsWithTag(HomePosts):
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['title'] = f'Записи по тегу: {Tag.objects.get(slug=self.kwargs["slug"])}'
        return context


    def get_queryset(self):
        
        return Post.objects.filter(tags__slug=self.kwargs["slug"])

class Search(HomePosts):
    template_name = 'blog/search.html'

    def get_queryset(self):
        return Post.objects.filter(title__icontains=self.request.GET.get('search_phrase'))
    

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['title'] = 'Поиск'
        context['search_phrase'] = f"{self.request.GET.get('search_phrase')}&"
        return context