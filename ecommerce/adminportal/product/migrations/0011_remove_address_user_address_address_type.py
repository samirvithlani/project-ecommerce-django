# Generated by Django 4.0.1 on 2022-01-28 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_remove_order_cart_item_order_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='user',
        ),
        migrations.AddField(
            model_name='address',
            name='address_type',
            field=models.CharField(default='Home', max_length=7),
        ),
    ]
