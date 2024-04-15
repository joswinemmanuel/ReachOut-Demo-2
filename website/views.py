from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def assistance(request):
    return render(request, 'assistance.html')

def contact(request):
    return render(request, 'contact.html')

def team(request):
    return render(request, 'team.html')

def testimonial(request):
    return render(request, 'testimonial.html')

def Error404(request):
    return render(request, '404.html')

def user_login(request):
    return render(request, 'login.html')