# Generated by Django 3.1.5 on 2021-01-12 00:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inteiro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itens', models.CharField(max_length=1001, validators=[django.core.validators.int_list_validator])),
            ],
        ),
    ]