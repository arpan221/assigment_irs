# Generated by Django 4.0.4 on 2022-05-22 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0008_alter_food_userid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
