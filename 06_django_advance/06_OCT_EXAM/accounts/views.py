from django.shortcuts import render, redirect, get_object_or_404  ####
# accounts 에서 import할 모든 것 들은 django.contrib.auth안에서 찾아야함 init에서
from django.contrib.auth import login as auth_login ####
from django.contrib.auth import logout as auth_logout  ####
# User 모델을 가져오는 함수
from django.contrib.auth import get_user_model ####
###accouts에서 import할 Model(User), Form UCF, AF
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.contrib.auth.decorators import login_required

# @require_http_methods  <== @@@@@ 데코레이터 사이너업
# 중요 로근 짤때 그대로 복사해서 넣어버림

def signup(request):
    if request.user.is_authenticated: # is_authenticated는 함수가 아님.
        return redirect('articles:article_list')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:article_list')
    else:
        form = UserCreationForm()
    return render(request, "accounts/form.html", {
        'form': form,
    })

def login(request):
    if request.user.is_authenticated: # is_authenticated는 함수가 아님.
        return redirect('articles:article_list')
    if request.method == 'POST':
        # Authform은 인자가 두개임 request핵심
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # save가 아님 성공한 유저 꺼내옴
            user = form.get_user()
            auth_login(request, user)
            # return redirect('articles:article_list') 마음 편하게 이거하면됨.
            return redirect(request.GET.get('next') or 'articles:article_list')
    else:
        form = AuthenticationForm()
    return render(request, "accounts/form.html", {
        'form': form,
    })


def logout(request):
    #auth_logout은 인자가 1개
    auth_logout(request)
    return redirect('articles:article_list')

