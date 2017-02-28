from django.shortcuts import render

# Create your views here.

def myView(request):
    return render(request, 'blabla.html', {
    })
