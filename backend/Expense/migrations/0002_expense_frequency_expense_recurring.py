# Generated by Django 4.1.5 on 2023-01-19 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Expense', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='frequency',
            field=models.CharField(default='Monthly', max_length=255),
        ),
        migrations.AddField(
            model_name='expense',
            name='recurring',
            field=models.BooleanField(default=True),
        ),
    ]
