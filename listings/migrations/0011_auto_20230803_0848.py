# Generated by Django 3.2.20 on 2023-08-03 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_auto_20230707_0851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='framework',
            name='logo',
            field=models.TextField(max_length=3000),
        ),
        migrations.AlterField(
            model_name='project',
            name='logo',
            field=models.ImageField(upload_to='images'),
        ),
    ]
