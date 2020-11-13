import bcrypt
from django.shortcuts import render,redirect,HttpResponse
from .models import *
from django.contrib import messages 


def root(request):
    if request=='POST':
        return redirect('/')
    else:
        return render(request, 'index.html')

def success(request):
    if request.session['user_id']:
        return render(request, 'home.html', {"user": User.objects.get(id=request.session['user_id'])})
    else:
        return redirect('/')

def registration(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, errors[error])
        return redirect('/')
    else:
        email = request.POST['email']
        try:
            User.objects.get(email=email)
            messages.error(request, "A user with this email already exists")
            return redirect('/')
        except:
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            password = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt())
            print(password)
            this_user = User.objects.create(firstname = firstname,
                    lastname = lastname, email = email, password = password)
            request.session['user_id'] = this_user.id
            return redirect('/success')

def login(request):
    email = request.POST['login-email']
    try:
        this_user = User.objects.get(email=email)
        if bcrypt.checkpw(
                request.POST['login-paswd'].encode(), this_user.password.encode()):
            request.session['user_id'] = this_user.id
            messages.error(request, "Successfully registered (or logged in)!")
            return redirect('/success')
        else:
            messages.error(request, "Wrong password")
            return redirect('/')
    except:
        messages.error(request, "Email not found")
        return redirect('/')

def logout(request):
    request.session['user_id'] = None
    return redirect('/')
