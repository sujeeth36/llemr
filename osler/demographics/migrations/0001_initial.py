# Generated by Django 3.0.5 on 2020-05-16 05:05

from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChronicCondition',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Demographics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateField(blank=True, null=True)),
                ('has_insurance', models.BooleanField(blank=True, null=True)),
                ('ER_visit_last_year', models.BooleanField(blank=True, null=True, verbose_name='Visited ER in the Past Year')),
                ('last_date_physician_visit', models.DateField(blank=True, null=True, verbose_name="Date of Patient's Last Visit to Physician or ER")),
                ('lives_alone', models.BooleanField(blank=True, null=True)),
                ('dependents', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Number of Dependents')),
                ('currently_employed', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EducationLevel',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='IncomeRange',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ResourceAccess',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Resource accesses',
            },
        ),
        migrations.CreateModel(
            name='TransportationOption',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='WorkStatus',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'Work statuses',
            },
        ),
        migrations.CreateModel(
            name='HistoricalDemographics',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('creation_date', models.DateField(blank=True, null=True)),
                ('has_insurance', models.BooleanField(blank=True, null=True)),
                ('ER_visit_last_year', models.BooleanField(blank=True, null=True, verbose_name='Visited ER in the Past Year')),
                ('last_date_physician_visit', models.DateField(blank=True, null=True, verbose_name="Date of Patient's Last Visit to Physician or ER")),
                ('lives_alone', models.BooleanField(blank=True, null=True)),
                ('dependents', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Number of Dependents')),
                ('currently_employed', models.BooleanField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('annual_income', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='demographics.IncomeRange')),
                ('education_level', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='demographics.EducationLevel')),
            ],
            options={
                'verbose_name': 'historical demographics',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
