# Generated by Django 3.0.6 on 2020-05-14 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ddtank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loai', models.CharField(max_length=50)),
                ('khoangcach', models.FloatField(max_length=10)),
                ('docao', models.FloatField(max_length=10)),
                ('gio', models.FloatField(max_length=10)),
                ('goc', models.FloatField(max_length=10)),
                ('luc', models.FloatField(max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
