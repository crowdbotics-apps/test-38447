# Generated by Django 2.2.28 on 2023-01-25 11:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_item', to='home.Sales'),
        ),
    ]
