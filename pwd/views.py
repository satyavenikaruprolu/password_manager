from django.http import HttpResponse
from .forms import UserForm, PasswordForm
from .models import User, Password
from django.shortcuts import render, redirect
from django.urls import reverse




# Create your views here.
def home(request):    
    return render(request, "home.html")


def signup(req):    
    context = {'code': None}
    form = None
    if req.method == 'POST':
        form = UserForm(req.POST)
        if form.is_valid():
            print(req.POST.get('username'), '-----')
            if User.objects.filter(username=req.POST.get('username')):
                print('user already exist')
                context.update({'message': 'username already taken', 'code': 'failed'})
            else:
                form.save()
                context.update({'message': 'successfully created user', 'code': 'success'})            
        else:    
            context.update({'message': 'error creating user', 'code': 'failed'})
    else:
        form = UserForm()        
    context['form'] = form
    return render(req, 'signup.html', context)

def login(req):        
    form = UserForm()        
    context = {'code': None, 'form': form}
    if req.method == 'POST':                
        user =  User.objects.get(username=req.POST.get('username'))
        if not user:
            context.update({'message': 'username does not exist', 'code': 'failed'})
        elif not user.pwd==req.POST.get('pwd'):
            context.update({'message': 'incorrect password', 'code': 'failed'}) 
        else:
            user.loggedin =  True
            user.save()
            req.session['user'] = user.username
            return redirect('dashboard')
    return render(req, 'login.html', context)


def dashboard(req, *args, **kwargs):
    context = {}    
    user = req.session.get('user')
    if user:
        user = User.objects.filter(username=user).first()
        if not user.loggedin:
            return redirect('/login/')
    else:    
        return redirect('/login/')
    if req.method == 'POST':        
        form = PasswordForm(req.POST)
        if form.is_valid():
            if Password.objects.filter(domain_name=req.POST.get('domain_name')):
                context.update({'message': 'already exists'})
            else:
                Password.objects.create(**{
                    'domain_name': req.POST.get('domain_name'),
                    'password': req.POST.get('password'),
                    'user': user
                })
    passwords = Password.objects.all()   
    form = PasswordForm()
    context.update({
        'user': user.username,
        'avatar': user.username[0].upper(),
        'form':form,
        'passwords': passwords
    })    
    return render(req, 'dashboard.html', context)

def delete_pwd(req, dname):
    pwd = Password.objects.filter(domain_name=dname).first()
    pwd.delete()
    return redirect('/dashboard/')