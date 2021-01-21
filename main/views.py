from django.shortcuts import render
def homepage(request):
    return HttpResponse("Hello world")

def test(request):
    return render(request, "test.html")

# Create your views here.
