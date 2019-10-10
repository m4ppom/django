from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from .models import Article
from .forms import ArticleModelForm, CommentModelForm
from IPython import embed


# CRUD
@require_http_methods(['GET', 'POST'])  # GET, POST요청 받겠다., 다양한 method있어서 저거 써주는게 좋음
def new_article(request):  # 어떤 방식으로 요청이 들어오는지
    # 요청이 GET POST인지 확인
    # 만약 POST라면 
    if request.method == 'POST':
        # ArticleModelForm 의 인스턴스를 생성하고 Data를 채운다.
        form = ArticleModelForm(request.POST)
        # =->binding된 form이 유효한지 확인한다.
        # embed()  # =-> 서버가 멈춤
        if form.is_valid():
            # 유효하면 저장
            article = form.save()
            # 저장한 article로 redirect
            return redirect(article)  # models에 absolute 선언해줘서 article만 써도 가능한거 
        # form 유효하지 않으면
        else:
            # 유효하지 않은 입력데이터를 담은 HTML과 에러메시지를 사용자한테 보여준다.
            return render(request, 'board/new.html', {
                'form': form,
            })

    # 만약 GET이라면
    elif request.method == 'GET':
        # 비어있는 form을 만든다
        form = ArticleModelForm()
        # form과 html을 사용자에게 보여준다.
        return render(request, 'board/new.html', {
            'form': form,
        })   


@require_GET
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'board/list.html', {
        'articles': articles,
    })


@require_GET
def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comments = article.comment_set.all()

    return render(request, 'board/detail.html', {
        'article': article,
        'comments': comments,
    })
    

@require_http_methods(['GET', 'POST'])
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleModelForm(request.POST, instance=article)  # 제출받은 요청 바디깆
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        form = ArticleModelForm(instance=article)
    return render(request, 'board/edit.html', {
        'form': form,
    })


@require_POST
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('board:article_list')


@require_POST
def new_comment(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    comment = Comment()
    comments = article.comment_set.all().order_by('-id')
    comment.content = request.POST.get('comment_content')
    comment.article_id = article.id
    comment.save()
    return redirect(article)

# @require_GET
# def index(request):
#     return render(request, 'board/index.html')


# @require_GET
# def list(request):
#     articles = Article.objects.all()  # 다 가져다줘여
#     # [<article1>, <article2>,....] 리스트로 리턴
#     return render(request, 'board/list.html', {
#         'articles': articles,
#     })


# @require_GET
# def detail(request, id):
#     article = get_object_or_404(Article, id=id)  # a id 해당 객체 리턴
#     return render(request, 'board/detail.html', {
#         'article': article,
#     })


# def new(request):
#     if request.method == 'POST':
#         form = ArticleModelForm(request.POST)

#         if form.is_valid():
#             article = Zform.save()
#             return redirect(article)
        
#     else:
#         form = ArticleModelForm()

#     return render(request, 'board/new.html', {
#         'form': form,
#     })


# def edit(request, id):
#     article = get_object_or_404(Article, id=id)
#     if request.method == 'POST':
#         article = Article.objects.get(id=id)
#         article.title = request.POST.get('title')
#         article.content = request.POST.get('content')
#         article.save()
#         return redirect(article)
#         article = Article.objects.get(id=id)
#     else:
#         article = Article.objects.get(id=id)
#         return render(request, 'board/edit.html', {
#             'article': article,
#         })


# @require_POST
# def delete(request, id):
#     article = Article.objects.get(id=id)
#     article.delete()
#     return redirect('board:list')
