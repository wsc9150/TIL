# Generated by Django 3.0.3 on 2020-09-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shareRes', '0003_auto_20200925_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurant_content',
            field=models.TextField(),
        ),
    ]
