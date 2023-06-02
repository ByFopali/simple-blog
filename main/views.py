from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm, CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

@login_required(login_url='login')
def index(request):
    # articles = Article.objects.filter(user=request.user)

    p = Paginator(Article.objects.filter(user=request.user), 2)
    page = request.GET.get('page')
    particles = p.get_page(page)

    context = {'particles': particles}
    return render(request, 'main/index.html', context)

@login_required(login_url='login')
def create(request):
    form = ArticleForm()
    if request.method == 'POST':
        data = ArticleForm(request.POST)
        if data.is_valid():
            data.instance.user = request.user
            data.save()
            return redirect('/')
    context = {'form': form}

    return render(request, 'main/post.html', context)
def contact(request):
    return render(request, 'main/contact.html')
def about(request):
    return render(request, 'main/about.html')
@login_required(login_url='login')
def delete(request, pk):
    current_obj = Article.objects.get(id=pk)
    if request.method == 'POST':
        current_obj.delete()
        return redirect('/')
    context = {'article': current_obj}
    return render(request, 'main/delete.html', context)
@login_required(login_url='login')
def update(request, pk):
    current_obj = Article.objects.get(id=pk)
    form = ArticleForm(instance=current_obj)
    if request.method == 'POST':
        data = ArticleForm(request.POST, instance=current_obj)
        if data.is_valid():
            data.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'main/post.html', context)

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
    context = {'form': form}
    return render(request, 'main/register.html', context)

def loginin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password']
            )
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'username OR password is incorrect')

    context = {}
    return render(request, 'main/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')