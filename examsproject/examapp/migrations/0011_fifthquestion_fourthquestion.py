# Generated by Django 2.1.4 on 2019-01-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examapp', '0010_auto_20190105_1234'),
    ]

    operations = [
        migrations.CreateModel(
            name='FifthQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='sumanth', max_length=50)),
                ('answer', models.TextField()),
                ('marks', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='FourthQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='sumanth', max_length=50)),
                ('answer', models.TextField()),
                ('marks', models.IntegerField(default=0)),
            ],
        ),
    ]
