# Generated by Django 4.0.4 on 2022-05-19 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=12)),
                ('userid', models.CharField(max_length=16)),
                ('profileName', models.CharField(max_length=150)),
                ('helpfulness', models.CharField(max_length=3)),
                ('score', models.FloatField()),
                ('time', models.PositiveBigIntegerField()),
                ('summary', models.TextField()),
                ('text', models.TextField()),
            ],
        ),
    ]