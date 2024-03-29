# Generated by Django 4.1.1 on 2022-09-22 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_transaction_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.RESTRICT, to='app.transactioncategory'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='payment_method',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='app.paymentmethod'),
            preserve_default=False,
        ),
    ]
