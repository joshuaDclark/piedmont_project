# Generated by Django 2.0.13 on 2019-06-07 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailedAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DetailedQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_question', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='MultichoiceAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multichoice_answer', models.CharField(max_length=100, verbose_name='Choice')),
            ],
        ),
        migrations.CreateModel(
            name='MultichoiceQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multichoice_question', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=130)),
                ('first_name', models.CharField(max_length=130)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('zip_code', models.CharField(max_length=5)),
                ('phone', models.CharField(max_length=10)),
                ('date_created', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SimpleChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SimpleQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(blank=True, null=True, verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='simplechoice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Questionaire.SimpleQuestion'),
        ),
        migrations.AddField(
            model_name='multichoiceanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Questionaire.MultichoiceQuestion'),
        ),
        migrations.AddField(
            model_name='detailedanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Questionaire.SimpleQuestion'),
        ),
    ]
