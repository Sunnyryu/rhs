# Generated by Django 2.2.6 on 2019-11-24 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subway', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subway',
            name='bread',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='subway',
            name='drink',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='subway',
            name='menu',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='subway',
            name='vegetable',
            field=models.CharField(max_length=50),
        ),
    ]