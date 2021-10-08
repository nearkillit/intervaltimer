import re, json
from rest_framework import viewsets, routers, status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import UserInfo
from todo.models import TimerTable, IntervalTable
from .serializers import IntervalTestSerializer, TimerTestSerializer, UserTestSerializer
from .utils.auth import NormalAuthentication
from django_filters import rest_framework as filters

# objectsの操作 https://qiita.com/shonansurvivors/items/12b087cf5ab591273c8c
class SignUp(APIView):
    def post(self, request, *args, **kwargs):  
        print(request.data)      
        serializer_user = UserTestSerializer(data=request.data)        
        if serializer_user.is_valid():
            get_user = serializer_user.save()
            return Response({"user":get_user.id}, status.HTTP_201_CREATED)
        else:
            return Response({"message":"既にユーザー名が存在します"}, status.HTTP_400_BAD_REQUEST)

class Login(APIView):

    authentication_classes = [NormalAuthentication,]

    def post(self, request, *args, **kwargs):
        return Response({"token": request.user})

    def put(self, request, *args, **kwargs):
        set_request_timers = []
        request_intervals = []
        # request_timers_json = json.loads(request.data["timers"])
        request_timers_json = request.data["timers"]        
        for t in request_timers_json:
            _request_timers = { "user": request.data["user"] }
            _request_intervals = {}
            for k in t:
                if k == "timer_name": # 改修予定
                    _request_timers[k] = t[k]
                    _request_intervals[k] = t[k]
                elif k == "id":
                    _request_timers[k] = t[k]
                    _request_intervals["timer"] = t[k]                                    
                elif k == "interval":
                    _request_intervals[k] = t[k]
            set_request_timers.append(_request_timers)
            request_intervals.append(_request_intervals)        
        s_test = TimerTable.objects.filter(user=1)
        serializer_timer = TimerTestSerializer(s_test,data=set_request_timers)        
        get_timer = None # IDが付与されたタイマーテーブルデータ
        if serializer_timer.is_valid():
            get_timer = serializer_timer.save()
        # インターバルのシリアライザ
        get_timer_idAndname = [{ "timer_id": t.id, "timer_name":t.timer_name } for t in get_timer ]        
        s_test = IntervalTable.objects.filter(timer__in=[t["timer_id"] for t in get_timer_idAndname])
        # インターバルデータ変換
        set_request_intervals = []
        _distinct_check_timer_id = []
        for req_intv in request_intervals:
            _request_intervals = {}            
            if req_intv["timer"] == 1:
                for t in get_timer_idAndname:
                    if t["timer_name"] == req_intv["timer_name"] and not t["timer_id"] in _distinct_check_timer_id:
                        _distinct_check_timer_id.append(t["timer_id"])                        
                        _request_intervals = { "timer":t["timer_id"] } 
                        break                                    
            else:
                _request_intervals = { "timer":req_intv["timer"] }            
            for i, intv in enumerate(req_intv["interval"]):
                _request_intervals = { **_request_intervals, "interval_order":i+1, "interval_second":intv }
                set_request_intervals.append(_request_intervals)        
        # timerとinteval.timerを結びつける
        serializer_interval = IntervalTestSerializer(s_test,data=set_request_intervals)
        if serializer_interval.is_valid():
            get_interval = serializer_interval.save()        
        return Response({"token": "success"})

    # user:1, username=takashi, password=takashi123,,        
    # timers:[
    #   {"id":6, "timer_name":"筋トレ2", "interval":[90,20] },
    #   {"id":7, "timer_name":"ヒート2", "interval":[40,20] },
    #   {"id":1, "timer_name":"クランチ", "interval":[120,20] },
    #   {"id":1, "timer_name":"クランチ２", "interval":[180,40] }])
    # ]
    #  ↓
    #  user:1, username=takashi, password=takashi123,
    #  timers: [
    #   {"id":6, "timer_name":"筋トレ2", "user":1 },
    #   {"id":7, "timer_name":"ヒート2", "user":1 },
    #   {"id":1, "timer_name":"クランチ", "user":1 },
    #   {"id":1, "timer_name":"クランチ２", ""user":1 }
    #  ]
    #  intervals:[
    #   { "interval":[90,20], "timer":6 },
    #   { "interval":[40,20], "timer":7 },
    #   { "interval":[120,20], "timer":?? },
    #   { "interval":[180,40], "timer":?? },
    #  ]        
    #  timers: [
    #   {"id":6, "timer_name":"筋トレ2", "user":1 },
    #   {"id":7, "timer_name":"ヒート2", "user":1 },
    #   {"id":18とか, "timer_name":"クランチ", "user":1 },
    #   {"id":19とか, "timer_name":"クランチ２", ""user":1 }
    #
    # intervals:[
    #  {'timer': 6, 'timer_name': '筋トレ2', 'interval': [90, 20]}, 
    #  {'timer': 7, 'timer_name': 'ヒート2', 'interval': [40, 20]},
    #  {'timer': 1, 'timer_name': 'クランチ', 'interval': [120, 40]}
    # ]