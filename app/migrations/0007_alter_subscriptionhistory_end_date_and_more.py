# Generated by Django 4.1.1 on 2022-09-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_subscription_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscriptionhistory',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='subscriptionhistory',
            name='start_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date_of_transaction',
            field=models.DateTimeField(),
        ),
    ]
