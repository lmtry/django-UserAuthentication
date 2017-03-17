from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

# Create your views here.
def login(request):
    return render_to_response('login.html', locals())

def submit(request):
    if 'username' in request.POST:
        username = request.POST['username']
        password=request.POST['userpass']
    else:
        username = "Not inputUserName"
    ctx={
        'user':username,
        'pass':password,
    }
    return render_to_response('login.html', ctx,)