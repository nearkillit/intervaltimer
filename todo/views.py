from django.views import generic
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm

# ToDoの一覧表示機能
class TodoListView(generic.ListView):
    model = Todo
    paginate_by = 5

# ToDoの詳細表示機能
class TodoDetailView(generic.DeleteView):
    model = Todo

# ToDoの作成機能
class TodoCreateView(generic.CreateView):
    model = Todo
    form_class = TodoForm
    # reverse_lasy,renderについてhttps://teratail.com/questions/50683
    # reverse_lasyは同期的にURLを持ってこれるのでロードする前にURLを逆引きしたい時に使う
    success_url = reverse_lazy('todo:list')

# Todoの編集機能
class TodoUpdateView(generic.UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('todo:list')

# Todoの削除機能
class TodoDeleteView(generic.DeleteView):
    model = Todo    
    success_url = reverse_lazy('todo:list')