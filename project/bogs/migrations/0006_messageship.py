# Generated by Django 3.1.2 on 2020-12-03 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phaseone', '0003_messageform'),
        ('bogs', '0005_auto_20201203_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messageship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phaseone.messageform')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bogs.group')),
            ],
        ),
    ]
