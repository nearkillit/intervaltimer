# Generated by Django 3.2.7 on 2021-10-05 02:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='intervaltable',
            name='timer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.timertable'),
        ),
        migrations.AlterField(
            model_name='timertable',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.usertable'),
        ),
    ]