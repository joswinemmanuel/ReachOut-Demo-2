from django.shortcuts import render

def journaling(request):
    return render(request, 'journaling.html')

def appointments(request):
    return render(request, 'appointments.html')

def chatbot(request):
    return render(request, 'chatbot.html')

def recommended(request):
    return render(request, 'recommended.html')

def dailytask(request):
    return render(request, 'dailytask.html')

def progress(request):
    return render(request, 'progress.html')

def dashboard(request):
    return render(request, 'dashboard.html')