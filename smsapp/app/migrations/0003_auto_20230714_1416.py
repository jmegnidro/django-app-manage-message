# Generated by Django 2.2.28 on 2023-07-14 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20230714_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagesdiffusion',
            name='recipient',
            field=models.ManyToManyField(to='app.ClientBoxs'),
        ),
    ]
