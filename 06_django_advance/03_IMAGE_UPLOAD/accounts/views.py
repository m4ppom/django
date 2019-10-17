from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.http import require_http_methods

@require_http_methods(['GET', 'POST'])
def signup(request):  # new_article같이
    # 회원가입할 데이터를 보냈음ㄴ
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('sns:posting_list')
        # else:
        #     return render(request, 'accounts/signup.html' {
        #         'form': form,
        #     })
    else:  # 회원가입 html달라는거
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })

def login():
    pass


def logout():
    pass


