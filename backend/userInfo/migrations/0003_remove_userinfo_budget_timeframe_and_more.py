# Generated by Django 4.1.5 on 2023-01-19 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userInfo', '0002_remove_userinfo_email_remove_userinfo_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='budget_timeframe',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='budget_value',
        ),
    ]