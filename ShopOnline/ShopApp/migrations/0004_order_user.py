# Generated by Django 3.2.5 on 2021-08-18 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopApp', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.CharField(default='admin', max_length=255),
            preserve_default=False,
        ),
    ]