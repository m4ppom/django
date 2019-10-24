from django.shortcuts import render, redirect, get_object_or_404  ####
# accounts 에서 import할 모든 것 들은 django.contrib.auth안에서 찾아야함 init에서

# User 모델을 가져오는 함수
from django.contrib.auth import get_user_model ####
###accouts에서 import할 Model(User), Form UCF, AF
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm
# @require_http_methods  <== @@@@@ 데코레이터 사이너업
# 중요 로근 짤때 그대로 복사해서 넣어버림

# 좋아요부분
def like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    user = request.user
    # if article.like_users.filter(id=user.id).exists():
    if user in article.like_users.all():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)
    return redirect('articles:article_list')



@require_GET
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {
        'articles':articles,
    })


@require_GET
def article_detail(request, article_id):
    #### get_object_or_404 인자 모델명 2번째 인자id=구하는 id
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/detail.html', {
        'article':article
    })


@login_required
@require_http_methods(['GET', 'POST']) # 썻다가 불안하면 쓰지말 것
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:article_detail', article.id)
    else:
        form = ArticleForm()
    return render(request, 'articles/form.html', {
        'form':form,
    })


@login_required
@require_http_methods(['GET', 'POST']) # 썻다가 불안하면 쓰지말 것
def article_update(request, article_id):
    
    #article찾기
    article = get_object_or_404(Article, id=article_id)
    #유저비교
    if article.user != request.user:
        return redirect('articles:article_list')

    if request.method == 'POST':
        form = ArticleForm(request.POST, instanse=article) ##update에 추가하는거.
        if form.is_valid():
            # 고치기
            article = form.save()
            return redirect('articles:article_detail', article.id)
    else:
        # instance주기
        form = ArticleForm(instance=article)
    return render(request, 'articles/form.html', {
        'form':form,
    })

@login_required
def article_delete(request, article_id):
    #article찾기
    article = get_object_or_404(Article, id=article_id)
    #유저비교하기
    if article.user != request.user:
        pass
