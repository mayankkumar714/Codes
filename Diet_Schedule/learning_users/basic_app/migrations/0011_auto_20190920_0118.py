# Generated by Django 2.2.4 on 2019-09-19 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0010_remove_userprofileinfo_portfolio_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='reference_Id',
            field=models.CharField(default='DEFAULT', max_length=20),
        ),
        migrations.AlterField(
            model_name='video',
            name='tags',
            field=models.CharField(default='DEFAULT', max_length=10),
        ),
    ]
