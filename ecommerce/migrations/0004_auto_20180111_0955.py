# Generated by Django 2.0 on 2018-01-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_attribute_attributegroup_authgroup_authgrouppermissions_authpermission_categoryproduct_djangoadminlo'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('firstname', models.CharField(blank=True, db_column='firstName', max_length=150, null=True)),
                ('lastname', models.CharField(blank=True, db_column='lastName', max_length=150, null=True)),
                ('username', models.CharField(max_length=150)),
                ('dob', models.DateField(blank=True, null=True)),
                ('mobilenumber', models.CharField(db_column='mobileNumber', max_length=200)),
                ('city', models.CharField(blank=True, max_length=150, null=True)),
                ('state', models.CharField(blank=True, max_length=150, null=True)),
                ('country', models.CharField(blank=True, max_length=150, null=True)),
                ('zip', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]