# Generated by Django 4.0 on 2022-01-02 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201114_1258'),
        ('referral', '0003_verbose_name_20210118_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followuprequest',
            name='completion_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(app_label)s_%(class)s_completed', to='users.user', verbose_name='completion author'),
        ),
    ]
