# Generated by Django 5.0.6 on 2024-07-02 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoping', '0002_alter_order_complete_alter_order_complete_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
    ]
