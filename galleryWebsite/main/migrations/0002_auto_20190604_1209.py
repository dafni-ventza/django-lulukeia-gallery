# Generated by Django 2.1.7 on 2019-06-04 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artgallery',
            fields=[
                ('galleryid', models.AutoField(db_column='galleryID', primary_key=True, serialize=False)),
                ('galleryname', models.CharField(db_column='galleryName', max_length=50)),
                ('telephone', models.CharField(max_length=20)),
                ('e_mail', models.CharField(db_column='e-mail', max_length=30)),
            ],
            options={
                'db_table': 'artgallery',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Artmovement',
            fields=[
                ('artisticid', models.AutoField(db_column='artisticID', primary_key=True, serialize=False)),
                ('artisticname', models.CharField(db_column='artisticName', max_length=50)),
                ('smalldescription', models.CharField(blank=True, db_column='smallDescription', max_length=500, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('countrate', models.IntegerField(blank=True, db_column='countRate', null=True)),
            ],
            options={
                'db_table': 'artmovement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Isrented',
            fields=[
                ('paintid', models.ForeignKey(db_column='PaintID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.Paint')),
                ('dateofrnt', models.DateTimeField(blank=True, db_column='DateofRnt', null=True)),
            ],
            options={
                'db_table': 'isrented',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Likespaint',
            fields=[
                ('paintid', models.ForeignKey(db_column='paintID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.Paint')),
                ('rating', models.FloatField()),
            ],
            options={
                'db_table': 'likespaint',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MainPaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('keywords', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'main_paint',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Painter',
            fields=[
                ('painterid', models.AutoField(db_column='painterID', primary_key=True, serialize=False)),
                ('firstname', models.CharField(db_column='firstName', max_length=255)),
                ('lastname', models.CharField(db_column='lastName', max_length=255)),
                ('nickname', models.CharField(blank=True, db_column='nickName', max_length=50, null=True)),
                ('origins', models.CharField(max_length=100)),
                ('dateborn', models.CharField(db_column='dateBorn', max_length=20)),
                ('datedied', models.CharField(blank=True, db_column='dateDied', max_length=20, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('countrate', models.IntegerField(blank=True, db_column='countRate', null=True)),
            ],
            options={
                'db_table': 'painter',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('roomid', models.AutoField(db_column='roomID', primary_key=True, serialize=False)),
                ('timeperiod', models.CharField(blank=True, db_column='timePeriod', max_length=20, null=True)),
                ('artmovement', models.IntegerField(blank=True, db_column='artMovement', null=True)),
            ],
            options={
                'db_table': 'room',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(db_column='userID', primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='userName', max_length=30)),
                ('userpassword', models.CharField(db_column='userPassword', max_length=50)),
                ('userstatus', models.IntegerField(blank=True, db_column='userStatus', null=True)),
                ('user_email', models.CharField(blank=True, max_length=40, null=True)),
                ('displayname', models.CharField(db_column='displayName', max_length=30)),
                ('membershiplevel', models.IntegerField(blank=True, db_column='membershipLevel', null=True)),
                ('creditcardno', models.CharField(blank=True, db_column='creditCardNo', max_length=255, null=True)),
                ('balance', models.IntegerField(blank=True, null=True)),
                ('user_registered', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='paint',
            options={'managed': False},
        ),
        migrations.CreateModel(
            name='Likesartmovement',
            fields=[
                ('artisticid', models.ForeignKey(db_column='artisticID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.Artmovement')),
                ('rating', models.FloatField()),
            ],
            options={
                'db_table': 'likesartmovement',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Likespainter',
            fields=[
                ('painterid', models.ForeignKey(db_column='painterID', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='main.Painter')),
                ('rating', models.FloatField()),
            ],
            options={
                'db_table': 'likespainter',
                'managed': False,
            },
        ),
    ]
