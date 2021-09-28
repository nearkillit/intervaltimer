# serializersとは、ざっくり言って、modelデータをJSONで出力するための機能です。
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields='__all__'  # 3.3.0からfiledかexcludeの指定が必要になった
                          # https://qiita.com/HIJIKI/items/a88d1ca86788bed3af9e