# Generated by Django 5.0.4 on 2024-04-14 00:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assign', '0004_alter_homework_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='assign.homework')),
            ],
            options={
                'ordering': ['created'],
                'indexes': [models.Index(fields=['created'], name='assign_comm_created_828107_idx')],
            },
        ),
    ]
