# Generated by Django 5.0.6 on 2024-06-29 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoping', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='complete',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='complete_date',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
    ]
