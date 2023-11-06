# Generated by Django 4.0.4 on 2023-10-25 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LatexUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latex_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='LaTeX name')),
                ('latex_affiliation', models.CharField(blank=True, max_length=255, null=True, verbose_name='LaTeX affiliation')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('about_me', models.TextField(blank=True, null=True, verbose_name='About me')),
                ('orcid_id', models.CharField(blank=True, max_length=255, null=True, verbose_name='ORCCID ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
