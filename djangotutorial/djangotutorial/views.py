from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>My First Heading</h1> <h1 style='background-color:DodgerBlue;'>Hello World</h1> <p style='background-color:Tomato;'>Lorem ipsum...</p><p>My first paragraph.</p>")