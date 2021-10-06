# serializersとは、ざっくり言って、modelデータをJSONで出力するための機能です。
# もっとざっくりいうとforms.pyのAPI版がserializers
# https://note.crohaco.net/2018/django-rest-framework-serializer/
from rest_framework import serializers
from .models import Todo, TimerTable, IntervalTable

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields='__all__'  # 3.3.0からfiledかexcludeの指定が必要になった
                          # https://qiita.com/HIJIKI/items/a88d1ca86788bed3af9e
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserTable
#         fields='__all__'  

class TimerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimerTable
        fields='__all__'  

class IntervalSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervalTable
        fields='__all__'  