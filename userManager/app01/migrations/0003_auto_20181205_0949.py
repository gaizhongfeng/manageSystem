# Generated by Django 2.0.6 on 2018-12-05 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_sutdent_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='cls',
        ),
        migrations.AddField(
            model_name='teacher',
            name='cls',
            field=models.ManyToManyField(to='app01.Classes'),
        ),
    ]