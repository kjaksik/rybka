# Generated by Django 3.2.4 on 2021-06-29 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.BinaryField(),
        ),
    ]
