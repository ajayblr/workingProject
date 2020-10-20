# Generated by Django 3.0.6 on 2020-05-31 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_phase', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Testphase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_phase', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('execution_day', models.DateField()),
                ('planned_tc', models.IntegerField()),
                ('executed_tc', models.IntegerField()),
                ('passed_tc', models.IntegerField()),
                ('failed_tc', models.IntegerField()),
                ('trend_comments', models.CharField(max_length=30)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectdata.Project')),
                ('project_phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectdata.Phase')),
            ],
        ),
        migrations.CreateModel(
            name='Testexecution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planned_tc', models.IntegerField()),
                ('executed_tc', models.IntegerField()),
                ('passed_tc', models.IntegerField()),
                ('failed_tc', models.IntegerField()),
                ('blocked_tc', models.IntegerField()),
                ('not_applicable_tc', models.IntegerField()),
                ('not_complete_tc', models.IntegerField()),
                ('no_run_tc', models.IntegerField()),
                ('deferred_tc', models.IntegerField()),
                ('text_comments', models.CharField(max_length=30)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectdata.Project')),
                ('project_phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectdata.Phase')),
            ],
        ),
        migrations.CreateModel(
            name='Projectstatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completion_status', models.IntegerField()),
                ('text_comments', models.CharField(max_length=29)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectdata.Project')),
                ('test_phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectdata.Testphase')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification_description', models.CharField(max_length=100)),
                ('notification_date', models.DateField()),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectdata.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new', models.IntegerField()),
                ('assigned_to_fix', models.IntegerField()),
                ('in_progress', models.IntegerField()),
                ('feedback_required', models.IntegerField()),
                ('rfr_in_dev', models.IntegerField()),
                ('passed_in_dev', models.IntegerField()),
                ('rfr_in_test', models.IntegerField()),
                ('passed_in_test', models.IntegerField()),
                ('rfr_in_pre_prod', models.IntegerField()),
                ('additional_fix_required', models.IntegerField()),
                ('ready_for_closure', models.IntegerField()),
                ('closed', models.IntegerField()),
                ('deferred', models.IntegerField()),
                ('rejected', models.IntegerField()),
                ('defect_comments', models.CharField(max_length=30)),
                ('project_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectdata.Project')),
                ('project_phase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projectdata.Phase')),
            ],
        ),
    ]
