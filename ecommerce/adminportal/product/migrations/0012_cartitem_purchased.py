# Generated by Django 4.0.1 on 2022-01-28 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_remove_address_user_address_address_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='purchased',
            field=models.BooleanField(default=False),
        ),
    ]
