from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect

from datetime import date

from .models import Todo

#Diferenças entre FBVs(Function Based Views) e CBVs(Class Based Views)
def todo_list(request):
    todos = Todo.objects.all()
    return render(request, 'todos/todo_list.html', {'todos': todos})

#Essa classe faz o mesmo que a função acima
class TodoListView(ListView):
    #Por padrão, a classe ListView procura o template com o caminho ./templates/nomeApp/nomeClasse_list
    model = Todo

class TodoCreateView(CreateView):
    #Por padrão, a classe ListView procura o template com o caminho ./templates/nomeApp/nomeClasse_form 
    model = Todo
    #Com uma classe CreateView, é necessário o parâmetro fields, que tem uma lista com os nomes dos campos do model que devem aparecer no formulario
    fields = ['title', 'deadline']
    #Com uma classe CreateView, é necessário o parâmetro success_url, que recebe o nome de uma das urls definidas da aplicação
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ['title', 'deadline']
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_as_complete()
        return redirect("todo_list")