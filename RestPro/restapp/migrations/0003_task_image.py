# Generated by Django 4.1.5 on 2023-03-06 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='image',
            field=models.ImageField(default='images/None/Noimage.jpg', upload_to='images/'),
        ),
    ]
