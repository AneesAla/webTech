from django.shortcuts import render


def home(request):
  return render(request, 'home.html')


def testpage(request):
  return render(request, 'myapp/testpage.html')
