from django.shortcuts import render, redirect, get_object_or_404
from .forms import BoardForm, CommentForm
from .models import Board, Comment
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.
def index(request):
    boards = Board.objects.all()
    paging = Paginator(boards, 5)
    page = request.GET.get('page')
    try:
        page_list = paging.get_page(page)
    except PageNotAnInteger:
        page_list = paginator.page(1)
    except EmptyPage:
        page_list = paginator.page(paginator.num_pages)

    context = { 'boards':page_list}
    return render(request, 'boards/index.html', context)

@login_required
def new(request):
    
    #if request.user.is_anonymous :
    #    return redirect('boards:index')
    if request.method == "POST":
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.user = request.user
            board.save()
            return redirect('boards:index')
    else:
        form = BoardForm()
        
    context = { 'form' : form }

    return render(request, 'boards/new.html', context)

def detail(request, b_id):
    board = get_object_or_404(Board, id=b_id)
    comment_form = CommentForm()
    comments = board.comment_set.all()
    person = get_object_or_404(get_user_model(),id=board.user_id)
    # 부모 객체에서 자식 객체를 사용할 때에는 _set을 사용하며, 
    context = {'board':board, 'comment_form':comment_form, 'comments':comments, 'person':person,}

    return render(request, 'boards/detail.html', context)

def edit(request, b_id):
    board = get_object_or_404(Board, id=b_id)
    
    if request.user != board.user:
        return redirect('boards:index')
    if request.method == "POST":
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save()
            return redirect('boards:detail', b_id) # board.id도 됨 
    
    else:
        form = BoardForm(instance=board) #해당폼에 있는 보드를 넣을 수 있음

    context = { 'form':form } 
    return render(request, 'boards/edit.html', context)

def delete(request, b_id):
    board = get_object_or_404(Board, id=b_id)
    if request.user != board.user:
        return redirect('boards:index')

    if request.method == "POST":
        board.delete()
        return redirect('boards:index')
    
    return redirect('boards:detail', b_id)# board_id 가능!
@require_POST
def new_comment(request, b_id):
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.board_id = b_id 
        comment.user = request.user #w 작성하고 있는 유저와 지금 보고 있는 유저가 같기에..
        comment.save() 
        return redirect('boards:detail', b_id)
    else:
        board = Board.objects.get(id=b_id)
        comments = Board.comment_set.all()

        context = { 'board':board, 'comments':comments, 'comment_form':form }
        return render(request, 'boards:detail.html', context)

@login_required
@require_POST
def del_comment(request, c_id):
    comment = get_object_or_404(Comment, id=c_id)
    board_id = comment.board_id
    if request.user == comment.user:
        comment.delete()
    return redirect('boards:detail', board_id)

@login_required 
def like(request, b_id):
    board = get_object_or_404(Board, pk=b_id)
    
    #if board.like_users.filter(id=request.user.id).exists():
    if request.user in board.like_users.all():
        board.like_users.remove(request.user)
    else:
        board.like_users.add(request.user)

    
    return redirect('boards:index')
def search(request):
    text = request.GET.get('search')
    
    results = Board.objects.filter(title__contains=text)
    context = {'results':results}
    return render(request, 'boards/search.html', context)
