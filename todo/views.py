from django.shortcuts import render
from .forms import TodoForms
from .models import Todo
from django.http import HttpResponse

def todolist(request):
    todo = Todo.objects.all()
    form = TodoForms()
    if request.method == 'POST':
        form = TodoForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Saved successfully')
    context = {
        'form': form,
        'todo': todo,
    }
    return render(request, 'index.html', context)
