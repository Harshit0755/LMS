# Generated by Django 3.0.8 on 2020-08-02 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0014_auto_20200803_0043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkout',
            name='status',
            field=models.CharField(default='Pending', max_length=100),
        ),
    ]