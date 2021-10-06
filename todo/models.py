from django.db import models
from users.models import UserInfo

# Create your models here.
class Todo(models.Model):
    todo = models.CharField('ToDo', max_length=100, blank=False)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    # 管理画面で確認するためのもの
    def __str__(self):
        return self.todo

# JSONの扱い方　https://qiita.com/xKxAxKx/items/7752f42b730b819fb7da
class TimerTable(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name="user_table")
    timer_name = models.CharField('タイマー名', max_length=18, blank=False)    

class IntervalTable(models.Model):
    timer = models.ForeignKey(TimerTable, on_delete=models.CASCADE, related_name="timer_table")
    interval_order = models.IntegerField('インターバルタイマー順番', blank=False, null=False)
    interval_second = models.IntegerField('インターバルタイマー秒数', blank=False, null=False)
