# Generated by Django 3.2.7 on 2021-11-22 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='popup',
            name='reinstatement',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='popup',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
