# Generated by Django 4.2.6 on 2023-10-06 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.JSONField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
