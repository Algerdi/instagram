# Generated by Django 4.0.3 on 2022-03-27 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(),
        ),
    ]
