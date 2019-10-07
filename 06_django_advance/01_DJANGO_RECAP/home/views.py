from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render('home/index.html')
    # return HttpResponse(f'hi {name}')
def guess(request):
    return render(request, 'home/guess.html')
def hi(request, name):
    # return HttpResponse('Home Page')
    
    return render(request, 'home/hi.html', {'name:': name})

def answer(request):
    count = 0
    if request.GET.get('q1') == 'asdf':
        count += 1
    elif request.GET.get('q2') == 'b':
        count += 1
    elif request.GET.get('q3') == 'c':
        count += 1
    return render(request, 'home/answer.html', {
        'count': count,
    })