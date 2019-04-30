# Generated by Django 2.2 on 2019-04-30 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0005_remove_buyorder_cookie_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyorder',
            name='product_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='product_id', to='homepage.Cookie'),
        ),
    ]
