# Generated by Django 4.1.1 on 2022-09-21 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_subscription_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='tags', to='app.tag'),
        ),
    ]
