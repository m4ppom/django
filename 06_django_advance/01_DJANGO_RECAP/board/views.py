from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from .models import Article


@require_GET
def index(request):
    return render(request, 'board/index.html')


@require_GET
def list(request):
    articles = Article.objects.all()  # 다 가져다줘여
    # [<article1>, <article2>,....] 리스트로 리턴
    return render(request, 'board/list.html', {
        'articles': articles,
    })


@require_GET
def detail(request, id):
    article = get_object_or_404(Article, id=id)  # a id 해당 객체 리턴
    return render(request, 'board/detail.html', {
        'article': article,
    })


@require_GET
def new(request):
    return render(request, 'board/new.html')


@require_POST
def create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('board:detail', article.id)


@require_GET
def edit(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'board/edit.html', {
        'article': article,
    })


@require_POST
def update(request, id):
    article = Article.objects.get(id=id)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('board:detail', article.id)


@require_POST
def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    return redirect('board:list')
