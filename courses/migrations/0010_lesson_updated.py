# Generated by Django 5.1.4 on 2024-12-12 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_alter_lesson_options_lesson_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
