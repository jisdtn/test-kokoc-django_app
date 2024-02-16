# Generated by Django 3.2.24 on 2024-02-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charcode', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('rate', models.IntegerField()),
            ],
        ),
    ]