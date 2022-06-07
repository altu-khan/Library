# Generated by Django 4.0.5 on 2022-06-07 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=60)),
                ('Summary', models.TextField(max_length=250)),
                ('Author', models.CharField(max_length=35)),
                ('Subject', models.CharField(max_length=60)),
            ],
        ),
    ]