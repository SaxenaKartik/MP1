# Generated by Django 2.2 on 2019-11-13 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scheduler_project', '0013_process_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Efficiency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_efficiency', models.IntegerField()),
                ('weekly_efficiency', models.IntegerField()),
                ('total_efficiency', models.IntegerField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Efficiency',
            },
        ),
    ]
