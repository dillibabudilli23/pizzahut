# Generated by Django 5.1.1 on 2024-12-05 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='topping1',
            new_name='maindish',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='topping2',
            new_name='sidish',
        ),
    ]
