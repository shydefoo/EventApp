# Generated by Django 2.1.7 on 2019-03-04 10:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('79602893-5f3f-4bf4-bb41-10144f1cd060'), editable=False, primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('0baf91e7-75bd-4389-af0c-d6aad896718d'), editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('description', models.CharField(max_length=2000)),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('27351da9-637d-495f-bb87-36b42f7385f9'), editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to='app.UserAccount'),
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(related_name='participants', to='app.UserAccount'),
        ),
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Event'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.UserAccount'),
        ),
    ]
