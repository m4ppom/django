from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from .models import Posting, Comment
from .forms import PostingModelForm, CommentModelForm

# Create your views here.

def posting_list(request):
    postings = Posting.objects.all()
    return render(request, 'sns/posting_list.html', {
        'postings': postings,
    })


@require_POST
def posting_detail(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comments = posting.comments.all()
    return render(request, 'sns/posting_detail.html', {
        'posting': posting,
        'comments': comments,
    })


@require_POST
def create_posting(request):
    posting = Posting()
    posting.content = request.POST.get('content')
    posting.icon = ''
    posting.image = request.FILES.get('image')
    posting.save()
    return redirect(posting)  # redirect('sns:posting_detail', posting.id)

@require_POST
def create_posting(request):
    form = PostingModelForm(request.POST)  # 검증 and 저장 준비
    if form.is_valid():
        posting = form.save()  # 저장 포스팅 객체를 리턴
        return redirect(posting)
    else:
        redirect('sns:posting_list')  # 실패하면 list페이지

@require_POST
def delete_posting(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    posting.delete()
    return redirect('sns:posting_list')


@require_POST
def create_comment(request, posting_id):
    posting = get_object_or_404(Posting, id=posting_id)
    form = CommentModelForm(request.POST)
    if form.is_valid():
        form.save(commit=False)  # 아직 postiin_id가 비어있기 떄문에 저장하는 척만하고 comment 객체를 return
        # comment.posting_id = posting.id
        comment.posting = posting
        comment.save()
    return redirect(posting)


@require_POST
def delete_comment(request, posting_id, comment_id):
    posting = get_object_or_404(Posting, id=posting_id)
    comment = get_object_or_404(Comment, id=comment_id, posting_id=posting_id)
    if comment in posting.comment_set.all():
        comment.delete()
    return redirect(comment.posting)

