from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Choice
from .forms import ChoiceModelForm
from IPython import embed
# 2개 함수
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    choices = question.choice_set.all()
    choice_form = ChoiceModelForm()
    return render(request, 'poll/question_detail.html', {
        'question': question,
        'choices': choices,
        'choice_form': choice_form,
    })


def upvote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    
    # 검증되지 않은 데이터는 사용하면 안되지만, 현재 select 태그에서 제한된 보기만 제공.
    chocie_content = request.POST.get('content')
    # 추가로, 만약 choice_content 에 이상한 데이터가 들어있다 해도, get_object_or_404 에서 검증단계를 거침
    old_chocie = get_object_or_404(Choice, content=chocie_content, question_id=question.id)
    
    choice_form = ChoiceModelForm(request.POST, instance=old_chocie)
    if choice_form.is_valid():
        new_choice = choice_form.save(commit=False)
        new_choice.votes += 1
        new_choice.save()

    return redirect(question)

