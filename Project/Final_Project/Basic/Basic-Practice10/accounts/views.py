from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCustomChangeForm, UserCustomCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, UserChangeForm
from IPython import embed
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash 
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
    if request.method == "POST":
        # form = UserCreationForm(request.POST)
        form = UserCustomCreationForm(request.POST)
        #embed()
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            #user = form.save()
            return redirect('boards:index')
    else:
        # form = UserCreationForm()
        form = UserCustomCreationForm()
        #embed()

    
    context = { 'form':form, 'label':"회원가입"}
    return render(request, 'accounts/auth_form.html', context)
    #return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('boards:index')
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'boards:index')
            # or을 넣으면 있다면 왼쪽 없으면 오른쪽 으로 간다고 생각해보자
    else:
        form = AuthenticationForm()
    
    context = { 'form':form, 'label':"로그인"}
    return render(request, 'accounts/login.html', context)
    #return render(request, 'accounts/login.html', context)

def logout(request):
    if request.method == "POST":
        auth_logout(request)

    return redirect('boards:index')

# django html에서 user.is_active 로그인 허용 여부 / user.is_superuser: 관리자 여부 / user.is_anonymous :로그아웃 판별 / user.is_authenticated : 로그인 판별
def edit(request):
    if request.method == "POST":
        form = UserCustomChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        # form = UserCustomChangeForm()
        form = UserCustomChangeForm(instance=request.user)

    context = { 'form':form, 'label':"정보수정" }
    return render(request, 'accounts/auth_form.html', context)
    #return render(request, 'accounts/edit.html', context)

def chg_pwd(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('accounts:edit')
    else:
        form = PasswordChangeForm(request.user)
        
    context = {'form':form, 'label':"암호수정"}
    return render(request, 'accounts/auth_form.html', context)
    #return render(request, 'accounts/pwd.html', context)

def delete(request):
    if request.method == "POST":
        request.user.delete()
        
    return redirect('boards:index')

@login_required()
def follow(request, u_id):
    person = get_object_or_404(get_user_model(), id=u_id)

    if person.followers.filter(id=request.user.id).exists():
        person.followers.remove(request.user)

    else:
        person.followers.add(request.user)

    return redirect('boards:index')
def profile(request, name):
    person = get_object_or_404(get_user_model(), username=name)
    context = { 'person':person }
    return render(request, 'accounts/profile.html', context)