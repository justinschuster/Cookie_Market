# Generated by Django 2.2 on 2019-04-30 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_cookie_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyorder',
            name='purchase_price',
            field=models.IntegerField(default=0),
        ),
    ]
