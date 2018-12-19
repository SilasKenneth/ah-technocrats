# Generated by Django 2.1 on 2018-12-19 08:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0003_auto_20181218_2105'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('classification', models.TextField(default='article')),
                ('article', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Article')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='articles.Comment')),
                ('notified', models.ManyToManyField(blank=True, related_name='notified', to=settings.AUTH_USER_MODEL)),
                ('notify_comments', models.ManyToManyField(blank=True, related_name='notify_comments', to=settings.AUTH_USER_MODEL)),
                ('read', models.ManyToManyField(blank=True, related_name='read', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
