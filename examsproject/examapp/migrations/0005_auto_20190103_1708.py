# Generated by Django 2.1.4 on 2019-01-03 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0004_thirdquestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='firstquestion',
            name='marks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='secondquestion',
            name='marks',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='thirdquestion',
            name='marks',
            field=models.IntegerField(default=0),
        ),
    ]
