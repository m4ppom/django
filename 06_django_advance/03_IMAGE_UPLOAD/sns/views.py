from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST

from .models import Posting, Comment
from .forms import PostingModelForm, CommentModelForm

@require_GET
def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'sns/posting_list.html', {
        'postings': postings,
    })

@require_GET
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comments.all()  # posting.comment_set 이 아닌 이유는 Model => related_name
    return render(request, 'sns/posting_detail.html', {
        'posting': posting,
        'comments': comments,
    })


@require_POST
def create_posting(request):
    form = PostingModelForm(request.POST, request.FILES)  # 검증 & 저장 준비
    if form.is_valid():  # 검증!
        posting = form.save()  # 저장 => Posting 객체 return
        return redirect(posting)  # 성공하면 detail page
    else:
        return redirect('sns:posting_list')  # 실패하면 list page


@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('sns:posting_list')


@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    form = CommentModelForm(request.POST)  # content 만 값을 확인 
    if form.is_valid():  # content 만 값을 검증
        comment = form.save(commit=False)  # 아직 posting_id 가 비어있기 때문에, 저장하는 '척' 만 하고 Comment 객체 return
        comment.posting = posting  # comment.posting_id = posting.id
        comment.save()
    return redirect(posting)
