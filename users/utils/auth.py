import time
import jwt
from mysite.settings import SECRET_KEY
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from rest_framework.response import Response
from users.models import UserInfo
from todo.models import TimerTable, IntervalTable
# https://teratail.com/questions/179125
from django.http import QueryDict

class NormalAuthentication(BaseAuthentication):
    def authenticate(self, request):        
        if request.method == "PUT":            
            username = QueryDict(request._request.body)["username"]
            password = QueryDict(request._request.body)["password"]            
        elif request.method == "POST":
            username = request._request.POST.get("username")
            password = request._request.POST.get("password")

        # PUTの場合 
        # print(QueryDict(request._request.body)) 
        # filter https://yu-nix.com/blog/2020/11/28/django-filter/ 
        user_obj = UserInfo.objects.filter(username=username).first()
        if not user_obj:
            raise exceptions.AuthenticationFailed('認証失敗')
        elif user_obj.password != password:
            raise exceptions.AuthenticationFailed('パスワードあってません')
        user_timer = TimerTable.objects.filter(user=user_obj.id).all()
        user_interval = list(range(len(user_timer)))        
        for index, ui in enumerate(user_timer):
            user_interval[index] = { "interval":IntervalTable.objects.filter(timer=ui.id).all(), "timer_id": ui.id }         
        # username = たかし
        # user_timer = [{ id:6, timer_name:"筋トレ", user:1 }, { id:7, timer_name:"ヒート", user:1 }]
        # user_interval = [ { id:1, interval_order:1, interval_second:90, timer:6 }, ...]        
        token = generate_jwt(user_obj, user_timer, user_interval)
        return (token, None)

    def authenticate_header(self, request):
        pass

# 先程インストールしたjwtライブラリでTokenを生成します
# Tokenの内容はユーザーの情報とタイムアウトが含まれてます
# タイムアウトのキーはexpであることは固定してます
# ドキュメント: https://pyjwt.readthedocs.io/en/latest/usage.html?highlight=exp
def generate_jwt(user, timer, interval):
    timestamp = int(time.time()) + 60*60*24*7
    timers = list(range(len(timer)))
    timerinterval = []
    for index, t in enumerate(timer):
        for itv in interval:
            if itv["timer_id"] == t.id: 
                _timerinterval = itv["interval"]
                timerinterval = list(range(len(_timerinterval)))
                for titv in _timerinterval:                                        
                    timerinterval[titv.interval_order - 1] = titv.interval_second                
        timers[index] = { "id": t.id, 
                          "name": t.timer_name, 
                          "interval": timerinterval }    
    return jwt.encode(
        {"userid": user.pk, 
         "username": user.username, 
         "exp": timestamp,
         "timers": timers,
        },SECRET_KEY).decode("utf-8")