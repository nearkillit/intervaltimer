# rest API https://racchai.hatenablog.com/entry/2016/04/12/Django_REST_framework_%E8%B6%85%E5%85%A5%E9%96%80
# rest frameworkを爆速で実装　https://qiita.com/kimihiro_n/items/86e0a9e619720e57ecd8
# rest frameworkをcurlで指示　https://qiita.com/Ajyarimochi/items/1345a49d70805db289a7
from rest_framework import viewsets, routers
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

router = routers.DefaultRouter()
router.register(r'todos', TodoViewSet)