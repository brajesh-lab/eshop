# Generated by Django 3.1.6 on 2021-07-23 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=20)),
                ('l_name', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=30)),
                ('pas', models.CharField(max_length=10)),
            ],
        ),
    ]
