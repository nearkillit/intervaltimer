from django.views import generic
from django.urls import reverse_lazy
from .models import TimerTable, Todo
from .forms import TodoForm, TestForm
from django.shortcuts import render

# Timerの表示
class TimerListView(generic.ListView):
    model = TimerTable

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


# ユーザー取得
class SampleView(generic.TemplateView):
    template_name = 'sample.html'

    def __init__(self):
        self.params = {
            'title': 'Hello',
            'message': 'your data',
            'form': TestForm()            
        }            
    
    # 変数を渡す
    # https://di-acc2.com/programming/python/5269/
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["test"] = "self.request.user"
    #     return context

    #get処理
    def get(self, request, *args, **kwargs):        
        return render(request, self.template_name, self.params)
        # return super().get(request, *args, **kwargs)

    #post処理
    def post(self, request, *args, **kwargs):
        msg = 'あなたは、&lt;b&gt;' + request.POST['name'] + \
            '(' + request.POST['age'] + ') &lt;/b&gt; さんです' + \
            '&lt;br&gt;メールアドレスは&lt;b&gt;' + request.POST['mail'] + '&lt;/b&gt;でござろう。'
 
        self.params['message'] = msg
        self.params['form'] = TestForm(request.POST)
        self.params['test'] = str(type(self.request.user))
        return render(request, self.template_name, self.params)
