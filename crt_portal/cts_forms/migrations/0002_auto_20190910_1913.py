# Generated by Django 2.2.4 on 2019-09-10 19:13

import cts_forms.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0001_squashed_0034_auto_20190823_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='contact_family_name',
            new_name='contact_first_name',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='contact_given_name',
            new_name='contact_last_name',
        ),
        migrations.RemoveField(
            model_name='report',
            name='do_not_contact',
        ),
        migrations.RemoveField(
            model_name='report',
            name='relationship',
        ),
        migrations.RemoveField(
            model_name='report',
            name='who_reporting_for',
        ),
    ]
