from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
# def task_list(request):
#     tasks=Task.objects.all()
#     return render(request, "task_list.html", {'tasks':tasks})


# def add_task(request):
#     if request.method=='POST':
#         title=request.POST(['title'])
#         task=Task.objects.create(title=title)
#         return redirect('/task_list')

#     return render(request, "add_task.html")


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'task_list.html', {'tasks': tasks})

@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        user = request.user 
        task = Task.objects.create(title=title, user=user)
        return redirect('task_list')
    return render(request, 'add_task.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})



