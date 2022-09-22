# Generated by Django 4.1.1 on 2022-09-22 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_card_alter_paymentmethod_account_delete_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='expire_on',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='gateway',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.paymentgateway'),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='payment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='app.paymenttype'),
        ),
    ]
