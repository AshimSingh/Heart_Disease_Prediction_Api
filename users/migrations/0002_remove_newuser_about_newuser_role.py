# Generated by Django 5.0.1 on 2024-03-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newuser',
            name='about',
        ),
        migrations.AddField(
            model_name='newuser',
            name='role',
            field=models.CharField(default='User', max_length=10),
        ),
    ]