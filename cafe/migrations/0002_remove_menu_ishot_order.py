# Generated by Django 5.0.3 on 2024-04-08 04:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='isHot',
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0, verbose_name='PRICE')),
                ('quantity', models.IntegerField(default=0, verbose_name='QUANTITY')),
                ('ice', models.BooleanField(default=True, verbose_name='ICE')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.menu')),
            ],
        ),
    ]
