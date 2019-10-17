from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth.forms import UserCreationForm

@require_http_methods(['GET', 'POST'])
def signup(request):  # new_user
    # 사용자가 회원가입할 데이터를 보냈다면,
    if request.method == 'POST':
        form = UserCreationForm(request.POST)    
        if form.is_valid():
            user = form.save()
            return redirect('sns:posting_list')

    else:  # 사용자가 회원가입 HTML 을 달라는 뜻
        form = UserCreationForm()
        
    return render(request, 'accounts/signup.html', {
        'form': form,
    })


def login(request):
    pass


def logout(request):
    pass
