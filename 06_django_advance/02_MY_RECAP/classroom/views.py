from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from .models import Student
# Create your views here.


def index(request):
    return render(request, 'classroom/index.html')


def list(request):
    students = Student.objects.all()
    return render(request, 'classroom/list.html', {
        'students': students,
    })


def detail(request, id):
    student = get_object_or_404(Student, id=id) 
    return render(request, 'classroom/detail.html', {
        'student': student,
    })


def new(request):
    return render(request, 'classroom/new.html')


def create(request):
    student = Student()
    student.name = request.GET.get('name')
    student.age = request.GET.get('age')
    student.major = request.GET.get('major')
    student.save()
    return redirect('classroom:detail', student.id)


def edit(request, id):
    student = Student.objects.get(id=id)
    return render(request, 'classroom/edit.html', {
        'student': student,
    })


def update(request, id):
    student = Student.objects.get(id=id)
    student.name = request.GET.get('name')
    student.age = request.GET.get('age')
    student.major = request.GET.get('major')
    student.save()
    return redirect('classroom:detail', student.id)


def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect('classroom:list')
