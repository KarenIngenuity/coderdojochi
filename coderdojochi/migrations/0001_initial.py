# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 16:12
from __future__ import unicode_literals

import coderdojochi.models
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='CDCUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(blank=True, choices=[(b'mentor', b'mentor'), (b'guardian', b'guardian')], max_length=10, null=True)),
                ('admin_notes', models.TextField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=40, null=True)),
                ('description', models.TextField(blank=True, help_text=b'Basic HTML allowed', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'courses',
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('amount', models.IntegerField()),
                ('verified', models.BooleanField(default=False)),
                ('receipt_sent', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'donation',
                'verbose_name_plural': 'donations',
            },
        ),
        migrations.CreateModel(
            name='EmailContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=255)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField(blank=True, help_text=b'Basic HTML allowed', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'email content',
                'verbose_name_plural': 'email content',
            },
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('asset_tag', models.CharField(max_length=255)),
                ('aquisition_date', models.DateTimeField()),
                ('condition', models.CharField(choices=[(b'working', b'Working'), (b'issue', b'Issue'), (b'unusable', b'Unusable')], max_length=255)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'equiptment',
                'verbose_name_plural': 'equiptment',
            },
        ),
        migrations.CreateModel(
            name='EquipmentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Guardian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('active', models.BooleanField(default=True)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('zip', models.CharField(blank=True, max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'guardian',
                'verbose_name_plural': 'guardians',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('address2', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Address 2')),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('zip', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('additional_info', models.TextField(blank=True, help_text=b'Basic HTML allowed', null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('external_enrollment_url', models.CharField(blank=True, help_text=b'When provided, local enrollment is disabled.', max_length=255, null=True)),
                ('public', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('bg_image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('announced_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coderdojochi.Location')),
            ],
            options={
                'verbose_name': 'meeting',
                'verbose_name_plural': 'meetings',
            },
        ),
        migrations.CreateModel(
            name='MeetingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=40, null=True)),
                ('description', models.TextField(blank=True, help_text=b'Basic HTML allowed', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'meeting type',
                'verbose_name_plural': 'meeting types',
            },
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('bio', models.TextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('background_check', models.BooleanField(default=False)),
                ('public', models.BooleanField(default=False)),
                ('avatar', stdimage.models.StdImageField(blank=True, upload_to=coderdojochi.models.generate_filename)),
                ('avatar_approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'mentors',
                'verbose_name_plural': 'mentors',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True)),
                ('ip', models.CharField(blank=True, max_length=255, null=True)),
                ('check_in', models.DateTimeField(blank=True, null=True)),
                ('alternate_guardian', models.CharField(blank=True, max_length=255, null=True)),
                ('affiliate', models.CharField(blank=True, max_length=255, null=True)),
                ('order_number', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('week_reminder_sent', models.BooleanField(default=False)),
                ('day_reminder_sent', models.BooleanField(default=False)),
                ('guardian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coderdojochi.Guardian')),
            ],
            options={
                'verbose_name': 'order',
                'verbose_name_plural': 'orders',
            },
        ),
        migrations.CreateModel(
            name='RaceEthnicity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_ethnicity', models.CharField(max_length=255)),
                ('visible', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'race ethnicity',
                'verbose_name_plural': 'race ethnicities',
            },
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('mentor_start_date', models.DateTimeField()),
                ('mentor_end_date', models.DateTimeField()),
                ('capacity', models.IntegerField(default=20)),
                ('mentor_capacity', models.IntegerField(blank=True, null=True)),
                ('additional_info', models.TextField(blank=True, help_text=b'Basic HTML allowed', null=True)),
                ('external_enrollment_url', models.CharField(blank=True, help_text=b'When provided, local enrollment is disabled.', max_length=255, null=True)),
                ('active', models.BooleanField(default=False, help_text=b'Session is active.')),
                ('public', models.BooleanField(default=False, help_text=b'Session is a public session.')),
                ('announced_date', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image_url', models.CharField(blank=True, max_length=255, null=True)),
                ('bg_image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('mentors_week_reminder_sent', models.BooleanField(default=False)),
                ('mentors_day_reminder_sent', models.BooleanField(default=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coderdojochi.Course')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coderdojochi.Location')),
                ('mentors', models.ManyToManyField(blank=True, related_name='session_mentors', to='coderdojochi.Mentor')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='session_teacher', to='coderdojochi.Mentor')),
                ('waitlist_mentors', models.ManyToManyField(blank=True, related_name='session_waitlist_mentors', to='coderdojochi.Mentor')),
            ],
            options={
                'verbose_name': 'session',
                'verbose_name_plural': 'sessions',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('birthday', models.DateTimeField()),
                ('gender', models.CharField(max_length=255)),
                ('school_name', models.CharField(max_length=255, null=True)),
                ('school_type', models.CharField(max_length=255, null=True)),
                ('medical_conditions', models.TextField(blank=True, null=True)),
                ('medications', models.TextField(blank=True, null=True)),
                ('photo_release', models.BooleanField(default=False, help_text=b"I hereby give permission to CoderDojoChi to use the student's image and/or likeness in promotional materials.", verbose_name=b'Photo Consent')),
                ('consent', models.BooleanField(default=False, help_text=b'I hereby give consent for the student signed up above to participate in CoderDojoChi.', verbose_name=b'General Consent')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('guardian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coderdojochi.Guardian')),
                ('race_ethnicity', models.ManyToManyField(blank=True, to='coderdojochi.RaceEthnicity')),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
            },
        ),
        migrations.AddField(
            model_name='session',
            name='waitlist_students',
            field=models.ManyToManyField(blank=True, related_name='session_waitlist_students', to='coderdojochi.Student'),
        ),
        migrations.AddField(
            model_name='order',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coderdojochi.Session'),
        ),
        migrations.AddField(
            model_name='order',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coderdojochi.Student'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='meeting_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coderdojochi.MeetingType'),
        ),
        migrations.AddField(
            model_name='meeting',
            name='mentors',
            field=models.ManyToManyField(blank=True, related_name='meeting_mentors', to='coderdojochi.Mentor'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='equipment_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coderdojochi.EquipmentType'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coderdojochi.Location'),
        ),
    ]
