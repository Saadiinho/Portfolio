# Generated by Django 3.2.20 on 2023-07-06 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('petiteDescription', models.CharField(max_length=2000)),
                ('langage', models.CharField(max_length=50)),
                ('isFinish', models.BooleanField(default=False)),
            ],
        ),
    ]
