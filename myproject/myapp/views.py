from django.shortcuts import render


def home(request):
  return render(request, 'home.html')

def impact(request):
  return render(request, 'impact.html')

def about(request):
  return render(request, 'about.html')

def policies(request):
  return render(request, 'policies.html')

def education(request):
  return render(request, 'education.html')

def unpage(request):
  return render(request, 'unpage.html')
