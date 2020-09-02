# Generated by Django 3.0.8 on 2020-07-07 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('teacher', models.CharField(blank=True, max_length=50, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('duration', models.CharField(blank=True, max_length=20, null=True)),
                ('overview', models.CharField(blank=True, max_length=2000, null=True)),
                ('lectures', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('img', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
