from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.http import HttpResponse


def index(request):
    templates = "posts/index.html"
    posts = Post.objects.order_by('-pub_date'[:10])
    title = "Это главная страница проекта Yatube"
    context = {'title': title,
               'posts': posts}
    return render(request, templates, context)


def group_post(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {'group': group,
               'posts': posts}
    return render(request, 'posts/group_list.html', context)