# Generated by Django 2.2.2 on 2019-07-02 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190702_0106'),
    ]

    operations = [
        migrations.AddField(
            model_name='alldata',
            name='keys',
            field=models.TextField(blank=True, null=True),
        ),
    ]