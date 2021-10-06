# django.urls https://www.sejuku.net/blog/26584
# from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView   
# 追加
from users.views import Login

urlpatterns = [
    # 追加
    path('login/', Login.as_view(), name='login'),    
    path('', TemplateView.as_view(template_name='home.html'), name='home'),    
    path('todo/', include('todo.urls')),
    path('admin/', admin.site.urls),           
]
