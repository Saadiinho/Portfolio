# Generated by Django 3.2.20 on 2023-07-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_alter_project_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='logo',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
