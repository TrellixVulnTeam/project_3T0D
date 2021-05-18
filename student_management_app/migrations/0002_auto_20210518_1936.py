# Generated by Django 3.0.7 on 2021-05-18 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='FacultyMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('department', models.CharField(blank=True, max_length=50)),
                ('designation', models.CharField(blank=True, max_length=50)),
                ('qualification', models.CharField(blank=True, max_length=500)),
                ('experience', models.CharField(blank=True, max_length=500)),
                ('awards', models.CharField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='HeroCarousal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alt_text', models.CharField(max_length=200, null=True)),
                ('carousal_image', models.ImageField(null=True, upload_to='banner/')),
                ('url_link', models.URLField(null=True)),
                ('status', models.CharField(choices=[('Featured', 'Featured'), ('Not Featured', 'Not Featured')], default='Not Featured', max_length=15)),
                ('caption', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(max_length=1000, null=True)),
                ('created_on', models.DateTimeField(null=True)),
                ('is_featured', models.CharField(choices=[('True', 'Yes'), ('False', 'No')], default='False', max_length=10, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='attendance',
            name='attendance_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='leavereportstaff',
            name='leave_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='leavereportstudent',
            name='leave_status',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='students',
            name='profile_pic',
            field=models.FileField(upload_to='profile/%Y/%m/%d'),
        ),
        migrations.CreateModel(
            name='StudentResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject_exam_marks', models.FloatField(default=0)),
                ('subject_assignment_marks', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.Students')),
                ('subject_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.Subjects')),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('featured_image', models.ImageField(null=True, upload_to='events/%Y/%m/%d')),
                ('content', models.TextField(max_length=1000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Publish', 'Publish')], default='Draft', max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student_management_app.Category')),
            ],
        ),
    ]
