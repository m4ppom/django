from django.shortcuts import render, HttpResponse


def index(request):
    return render(request, 'home/index.html')


def guess(request):
    return render(request, 'home/guess.html')


def answer(request):
    count = 0
    if request.POST.get('q1') == 'a':
        count += 1
    if request.POST.get('q2') == 'b':
        count += 1
    if request.POST.get('q3') == 'c':
        count += 1

    return render(request, 'home/answer.html', {
        'count': count,
    })