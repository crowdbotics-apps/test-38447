# Generated by Django 2.2.28 on 2023-01-25 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salesDate', models.DateTimeField(auto_now=True)),
                ('qty', models.SmallIntegerField()),
                ('price', models.BigIntegerField()),
            ],
        ),
    ]
