from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    # return HttpResponse("Hello World");
    return render(request, 'home.html', {
        'authors': [
            'DarkDevil',
            'Felon KR',
            "M Amandeep"
        ]
    })

def login(request):
    # return HttpResponse("Hello World");
    if request.method == 'POST':

        email = request.POST["email"]
        password = request.POST["password"]

        return render(request, 'home.html', {
            'authors': [
                'DarkDevil',
                'Felon KR',
                "M Amandeep"
            ]
        })
    else:

        return render(request, 'studentLogin.html', {
            'authors': [
                'DarkDevil',
                'Felon KR',
                "M Amandeep"
            ]
        })
