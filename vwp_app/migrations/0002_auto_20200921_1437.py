# Generated by Django 3.0.3 on 2020-09-21 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vwp_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tblbankinfo',
            name='partner_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tblbankinfo',
            name='route_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tblinvestment',
            name='bankinfo_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tblinvestment',
            name='buy_back_rate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tblinvestment',
            name='days',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tblinvestment',
            name='distribution',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='tblinvestment',
            name='equity',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='tblinvestment',
            name='invest_amt',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tblinvestment',
            name='partner_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tblinvestment',
            name='property_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tblinvestment',
            name='ret_rate',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='tblinvestment',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='tblinvestment',
            name='term',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tbllog',
            name='lg_date_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='tblproperty',
            name='close_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='tblproperty',
            name='purch_price',
            field=models.DecimalField(decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AddField(
            model_name='tblusers',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='tblusers',
            name='term_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='tbllog',
            name='lg_action',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tbllog',
            name='lg_user_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tblproperty',
            name='add_city',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tblproperty',
            name='add_site',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tblproperty',
            name='add_state',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tblproperty',
            name='add_zip',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
