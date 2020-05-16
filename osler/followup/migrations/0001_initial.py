# Generated by Django 3.0.5 on 2020-05-16 05:05

from django.db import migrations, models
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactResult',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('attempt_again', models.BooleanField(default=False, help_text='True if outcome means the pt should be contacted again.')),
                ('patient_reached', models.BooleanField(default=True, help_text='True if outcome means they reached the patient')),
            ],
        ),
        migrations.CreateModel(
            name='GeneralFollowup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalGeneralFollowup',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('written_datetime', models.DateTimeField(blank=True, editable=False)),
                ('last_modified', models.DateTimeField(blank=True, editable=False)),
                ('comments', models.TextField(blank=True, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical general followup',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalLabFollowup',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('written_datetime', models.DateTimeField(blank=True, editable=False)),
                ('last_modified', models.DateTimeField(blank=True, editable=False)),
                ('comments', models.TextField(blank=True, null=True)),
                ('communication_success', models.BooleanField(help_text='Were you able to communicate the results?')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical lab followup',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalReferralFollowup',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('written_datetime', models.DateTimeField(blank=True, editable=False)),
                ('last_modified', models.DateTimeField(blank=True, editable=False)),
                ('comments', models.TextField(blank=True, null=True)),
                ('has_appointment', models.BooleanField(help_text='Does the patient have an appointment?')),
                ('pt_showed', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Not yet', 'Not yet')], help_text='Did the patient show up to the appointment?', max_length=7, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical referral followup',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalVaccineFollowup',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('written_datetime', models.DateTimeField(blank=True, editable=False)),
                ('last_modified', models.DateTimeField(blank=True, editable=False)),
                ('comments', models.TextField(blank=True, null=True)),
                ('subsq_dose', models.BooleanField(verbose_name='Has the patient committed to coming back for another dose?')),
                ('dose_date', models.DateField(blank=True, help_text='When does the patient want to get their next dose (if applicable)?', null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
            ],
            options={
                'verbose_name': 'historical vaccine followup',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='LabFollowup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('communication_success', models.BooleanField(help_text='Were you able to communicate the results?')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NoAptReason',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='NoShowReason',
            fields=[
                ('name', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='ReferralFollowup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('has_appointment', models.BooleanField(help_text='Does the patient have an appointment?')),
                ('pt_showed', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No'), ('Not yet', 'Not yet')], help_text='Did the patient show up to the appointment?', max_length=7, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VaccineFollowup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('written_datetime', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('subsq_dose', models.BooleanField(verbose_name='Has the patient committed to coming back for another dose?')),
                ('dose_date', models.DateField(blank=True, help_text='When does the patient want to get their next dose (if applicable)?', null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
