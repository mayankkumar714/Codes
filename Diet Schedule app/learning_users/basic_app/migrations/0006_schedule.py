# Generated by Django 2.2.4 on 2019-09-10 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_auto_20170307_0657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_item', models.CharField(max_length=200)),
                ('number_of_times', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
            ],
        ),
    ]
