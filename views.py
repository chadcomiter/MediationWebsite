from django.shortcuts import render
from .models import Instructor, Program, QuestionAnswer, HomePageMessage
# Create your views here.

def home(request):
    return render(
        request = request,
        template_name='main/home.html'
    )

def instructors(request):
    return render(
        request=request,
        template_name='main/instructors.html'
    )

def programs(request):
    return render(
        request=request,
        template_name='main/programs.html'
    )

def faq(request):
    return render(
        request=request,
        template_name='main/faq.html',
        context={"questions":QuestionAnswer.objects.all}
    )