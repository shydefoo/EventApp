# Generated by Django 2.1.7 on 2019-03-11 03:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('9287f49d-ff07-4072-a9c1-2f6afd8bcd3e'), editable=False, primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=2000)),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('4716138f-54b5-4310-8d4f-bbaee02f33d0'), editable=False, primary_key=True, serialize=False)),
                ('date_created', models.DateField(auto_now=True)),
                ('datetime_of_event', models.DateTimeField(blank=True, null=True)),
                ('description', models.CharField(max_length=2000)),
                ('title', models.CharField(max_length=200)),
                ('location', models.CharField(blank=True, max_length=20)),
                ('category', models.ManyToManyField(blank=True, to='app.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Event')),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.UUID('8a71665f-3bc3-4669-b39c-5f6f86626547'), editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, verbose_name='username')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
            ],
        ),
        migrations.CreateModel(
            name='UserSaltTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salt', models.UUIDField(default=uuid.UUID('1c190b3b-d378-4078-ac91-09b748a17b0b'))),
            ],
        ),
        migrations.AddField(
            model_name='useraccount',
            name='salt',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.UserSaltTable'),
        ),
        migrations.AddField(
            model_name='event',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, related_name='likes', to='app.UserAccount'),
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, related_name='participants', to='app.UserAccount'),
        ),
        migrations.AddField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Event'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.UserAccount'),
        ),
    ]
