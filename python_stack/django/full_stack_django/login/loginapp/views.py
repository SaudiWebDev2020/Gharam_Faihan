import bcrypt
from django.shortcuts import render,redirect,HttpResponse
from .models import User
from django.contrib import messages 


# Create your views here.
def index(request):
    return render (request,'index.html')

def login(request):
    if request.method == 'POST':
        errors = User.objects.login_validation(request.POST)
        if len(errors) > 1:
            logged_user = User.objects.filter(
                email=request.POST['login-email'].lower()).first()
            if bcrypt.checkpw(request.POST['login-paswd'].encode(), logged_user.password.encode()):
                request.session['userid'] = logged_user.id
                request.session['name'] = f'{logged_user.firstname} {logged_user.lastname}'
                messages.success(request, 'Successfully logged in!')
                # never render on a post, always redirect!
                return redirect('/')
            else:
                messages.error(request, 'Email or Password are not match')
        else:
            print(errors)
            for key, value in errors.items():
                messages.error(request, value)
        return redirect('/')

def logout(request):
    request.session['id'] = 0
    return redirect('/')

    
def registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password'] 
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(firstname = request.POST['firstname'] , lastname= request.POST['lastname'], email= request.POST['email'], password=pw_hash)
        return redirect('/' )
    return render(request,'page.html')

