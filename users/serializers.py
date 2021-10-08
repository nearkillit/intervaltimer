# serializersとは、ざっくり言って、modelデータをJSONで出力するための機能です。
# もっとざっくりいうとforms.pyのAPI版がserializers
# https://note.crohaco.net/2018/django-rest-framework-serializer/
from rest_framework import serializers
from .models import UserInfo
from todo.models import TimerTable, IntervalTable

class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields='__all__'

class UserTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields=('username','password')

    # def update(self, instance, validated_data):
    #     print(validated_data)
    #     return super().update(instance, validated_data)

class TimerInfoSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    # interval = serializers.ListField()

    class Meta:        
        model = TimerTable
        fields='__all__'

class TimerTestSerializer(serializers.ListSerializer):
    child = TimerInfoSerializer()

    def update(self, instance, validated_data):        
        timer_mapping = {timer.id: timer for timer in instance}
        # id=1の場合追加
        data_mapping = {}
        data_mapping_add = []
        for item in validated_data:            
            if item["id"] == 1:
                data_mapping_add.append(item)
            else:
                data_mapping = {**data_mapping, item['id']: item}
        if len(data_mapping_add) > 0:
            data_mapping = {**data_mapping, 1: data_mapping_add}            
        
        ret = []
        for id, data in data_mapping.items():
            # id=1の場合データを追加
            if id == 1:
                for data_add in data:
                    new_data_add = {}
                    for k in data_add:                        
                        # dataから"id"を省いている
                        if not k == "id":
                            new_data_add = {**new_data_add, k:data_add[k]}                    
                    ret.append(self.child.create(new_data_add))            
            else:
                timer = timer_mapping.get(id, None)
                if timer is None:
                    print("data is None")
                else:                    
                    ret.append(self.child.update(timer, data))

        for id, timer in timer_mapping.items():
            if id not in data_mapping:
                timer.delete()
        
        return ret

class IntervalInfoSerializer(serializers.ModelSerializer):    

    class Meta:
        model = IntervalTable
        fields='__all__'

class IntervalTestSerializer(serializers.ListSerializer):
    child = IntervalInfoSerializer()

    def update(self, instance, validated_data):
        
        interval_mapping = {interval.id: interval for interval in instance}
        data_mapping = [ item for item in validated_data ]
        data_mapping_timer = [ t["timer"] for t in validated_data ]                        
        print(data_mapping)
        for interval_id, interval in interval_mapping.items():            
            print(interval)
            if interval.timer in data_mapping_timer:
                interval.delete()
            
        ret = []
        for data in data_mapping:
            ret.append(self.child.create(data))

        return ret
