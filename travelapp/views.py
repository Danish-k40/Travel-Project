from django.http import HttpResponse
from django.shortcuts import render
from .models import place, news_post


# Create your views here.

# program for hello world

# def fun(request):
#     return HttpResponse("HELLO WORLD")

# here load html page from templates

def fun(request):
    # here dictionary is used to pass values #
    # return render(request, 'home.html', {'name': 'Dilshan k'})
    # we call the class tables from modules #
    # obj = place()
    # obj.name='Kerala'
    # obj.img=''
    # obj.id=''
    # obj.desc='This is kerala'
    # obj.price=599

    obj = place.objects.all()
    o = news_post.objects.all()

    return render(request, 'index.html', {'results': obj, 'answers': o})


# Addition Function using GET or POST method
def addition(request):
    num1 = int(request.POST['num1'])
    num2 = int(request.POST['num2'])
    num3 = num1 + num2
    return render(request, 'result.html', {'Sum': num3})
