# Generated by Django 3.2.22 on 2023-10-16 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Name')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
    ]
