from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# def home(request):
#     return HttpResponse('Hey Hi There!')
import random

def home(request):
    return render(request,'/Users/shivamsharma612/Downloads/webdevelopmentCourse1/password_generator/password_generator_project/generator/templates/generator/home.html'
                  )

# def eggs(request):
#     return HttpResponse('Eggs are tasty!')

def password(request):
    # added in random password generation

    characters=list('abcdefghijklmnopqrstuvwxyz')

    # length = 10
    # 29. form data using
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('`+-_=/?.>,<;:!@##$%^&*'))

    if request.GET.get('numbers'):
        characters.extend(list('123456789'))

    length = int(request.GET.get('length'))



    thepassword = ''

    for x in range(length):
        thepassword +=random.choice(characters)

    return render(request,
                  '/Users/shivamsharma612/Downloads/webdevelopmentCourse1/password_generator/password_generator_project/generator/templates/generator/password.html',
                  {'password':thepassword}
                  )

def About_us(request):
    return render(request,'/Users/shivamsharma612/Downloads/webdevelopmentCourse1/password_generator/password_generator_project/generator/templates/generator/About_us.html'
                  )
