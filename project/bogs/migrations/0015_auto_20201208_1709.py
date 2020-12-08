# Generated by Django 3.1.4 on 2020-12-08 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bogs', '0014_auto_20201207_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='primary',
            field=models.CharField(default='1', max_length=256, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='userid',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
