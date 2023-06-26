from django.http import HttpResponse

def test_view(request):
    return HttpResponse("This is a test view.")