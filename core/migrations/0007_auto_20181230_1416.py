# Generated by Django 2.0.3 on 2018-12-30 16:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20181230_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disciplina',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 30, 14, 16, 46, 419631)),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='DtEntrega',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 30, 14, 16, 46, 435231)),
        ),
        migrations.AlterField(
            model_name='mensagem',
            name='DTEnvio',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 30, 14, 16, 46, 435231)),
        ),
        migrations.AlterField(
            model_name='solicitacaomatricula',
            name='DTSolicitacao',
            field=models.DateTimeField(default=datetime.datetime(2018, 12, 30, 14, 16, 46, 435231)),
        ),
    ]
