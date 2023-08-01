from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    peoples =[
        {'name' : 'Sourav Mandal' , 'age' : 30},
        {'name' : 'S Mandal' , 'age' : 13},
        {'name' : 'R Mandal' , 'age' : 24},
        {'name' : 'SR Mandal' , 'age' : 17},
        {'name' : 'SASsa Mandal' , 'age' : 63},
    ]

    

    return render(request , "home/index.html" , context={'peoples' : peoples})

def about(request):
    return render(request , "home/about.html")


def contact(request):
    return render(request , "home/contact.html")