from django.http import HttpResponse

def homepage(request):
    return HttpResponse("<h>Yo pips</h>")
