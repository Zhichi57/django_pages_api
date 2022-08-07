# Generated by Django 4.1 on 2022-08-06 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('bitrate', models.IntegerField()),
                ('counter', models.IntegerField()),
            ],
            options={
                'db_table': 'audios',
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('value', models.CharField(max_length=255)),
                ('counter', models.IntegerField()),
            ],
            options={
                'db_table': 'texts',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video_ulr', models.URLField()),
                ('subtitles_ulr', models.URLField()),
                ('counter', models.IntegerField()),
            ],
            options={
                'db_table': 'videos',
            },
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('audios', models.ManyToManyField(to='main.audio')),
                ('texts', models.ManyToManyField(to='main.text')),
                ('videos', models.ManyToManyField(to='main.video')),
            ],
            options={
                'db_table': 'pages',
            },
        ),
    ]
