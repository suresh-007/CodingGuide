# Generated by Django 2.1.3 on 2020-07-12 14:34

from django.db import migrations
import hashid_field.field


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_auto_20200712_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='id',
            field=hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, primary_key=True, serialize=False),
        ),
    ]
