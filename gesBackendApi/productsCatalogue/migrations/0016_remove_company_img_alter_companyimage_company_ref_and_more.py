# Generated by Django 4.2.14 on 2024-08-12 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productsCatalogue', '0015_product_airflow_product_rpm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='img',
        ),
        migrations.AlterField(
            model_name='companyimage',
            name='company_ref',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='productsCatalogue.company'),
        ),
        migrations.AddField(
            model_name='company',
            name='img',
            field=models.ManyToManyField(blank=True, null=True, to='productsCatalogue.companyimage'),
        ),
    ]
