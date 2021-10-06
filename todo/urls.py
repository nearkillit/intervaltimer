from django.urls import path, include
# from django.conf.urls import url, include
from . import views, apis

app_name = 'todo'
# class based view, function base view の２つがある
# 今回はclass based view

# app_name,nameはDTLで呼び出すときの名前
urlpatterns = [
    path('list/', views.TodoListView.as_view(), name='list'),
    # detailはここで指定した<pk>プライマルキーから、レコードを特定してきてくれる
    # <int:pk>は整数の場合    
    path('detail/<int:pk>/', views.TodoDetailView.as_view(), name='detail'),
    path('create/', views.TodoCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.TodoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.TodoDeleteView.as_view(), name='delete'),
    # r は文字列　^ は〜で始めるの正規表現
    path('api/', include(apis.router.urls)),    
    # timer用
    path('timer/', views.TimerListView.as_view(), name='timer'),
    # test用
    # path('test/', views.SampleView.as_view(), name='test'),
]