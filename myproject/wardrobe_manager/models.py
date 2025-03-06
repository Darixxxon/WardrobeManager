# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Bases(models.Model):
    brand = models.CharField(db_column='Brand', max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    length = models.CharField(db_column='Length', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    style = models.CharField(db_column='Style', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    colour_1 = models.CharField(db_column='Colour_1', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    colour_2 = models.CharField(db_column='Colour_2', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dir = models.CharField(db_column='Dir', max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    new = models.BooleanField(db_column='New', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Bases'
    
    def __str__(self):
        return 'Base'
    
    def properties(self):
        return f"""
        brand:          {self.brand}
        size:           {self.size}
        length:         {self.length}
        type:           {self.type}
        style:          {self.style}
        colour_1:       {self.colour_1}
        colour_2:       {self.colour_2}
        """


class Coats(models.Model):
    brand = models.CharField(db_column='Brand', max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    style = models.CharField(db_column='Style', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    colour_1 = models.CharField(db_column='Colour_1', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    colour_2 = models.CharField(db_column='Colour_2', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dir = models.CharField(db_column='Dir', max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    new = models.BooleanField(db_column='New', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Coats'
    
    def __str__(self):
        return 'Coat'
    
    def properties(self):
        return f"""
        brand:          {self.brand}
        size:           {self.size}
        colour_2:       {self.colour_2}
        type:           {self.type}
        colour_1:       {self.colour_1}
        style:          {self.style}
        """


class Combinations(models.Model):
    shoes = models.ForeignKey('Shoes', models.DO_NOTHING, blank=True, null=True)
    pants = models.ForeignKey('Pants', models.DO_NOTHING, blank=True, null=True)
    base = models.ForeignKey(Bases, models.DO_NOTHING, blank=True, null=True)
    overtop = models.ForeignKey('Overtops', models.DO_NOTHING, blank=True, null=True)
    coat = models.ForeignKey(Coats, models.DO_NOTHING, blank=True, null=True)
    hat = models.ForeignKey('Hats', models.DO_NOTHING, blank=True, null=True)
    reviewed = models.BooleanField(blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Combinations'


class Hats(models.Model):
    brand = models.CharField(db_column='Brand', max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    colour_1 = models.CharField(db_column='Colour_1', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    colour_2 = models.CharField(db_column='Colour_2', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dir = models.CharField(db_column='Dir', max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    new = models.BooleanField(db_column='New', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Hats'
    
    def __str__(self):
        return 'Hat'
    
    def properties(self):
        return f"""
        brand:          {self.brand}
        size:           {self.size}
        type:           {self.type}
        colour_1:       {self.colour_1}
        colour_2:       {self.colour_2}
        """


class Overtops(models.Model):
    brand = models.CharField(db_column='Brand', max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    style = models.CharField(db_column='Style', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    colour_1 = models.CharField(db_column='Colour_1', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    colour_2 = models.CharField(db_column='Colour_2', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dir = models.CharField(db_column='Dir', max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    new = models.BooleanField(db_column='New', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Overtops'
    
    def __str__(self):
        return 'Base'
    
    def properties(self):
        return f"""
        brand:          {self.brand}
        size:           {self.size}
        type:           {self.type}
        style:          {self.style}
        colour_1:       {self.colour_1}
        colour_2:       {self.colour_2}
        """


class Pants(models.Model):
    brand = models.CharField(db_column='Brand', max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    length = models.CharField(db_column='Length', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    style = models.CharField(db_column='Style', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    colour_1 = models.CharField(db_column='Colour_1', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    colour_2 = models.CharField(db_column='Colour_2', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dir = models.CharField(db_column='Dir', max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    new = models.BooleanField(db_column='New', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Pants'
    
    def __str__(self):
        return 'Coat'
    
    def properties(self):
        return f"""
        brand:          {self.brand}
        size:           {self.size}
        length:         {self.length}
        type:           {self.type}
        style:          {self.style}
        colour_1:       {self.colour_1}
        colour_2:       {self.colour_2}
        """


class Shoes(models.Model):
    brand = models.CharField(db_column='Brand', max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    size = models.CharField(db_column='Size', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=100, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    colour_1 = models.CharField(db_column='Colour_1', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    colour_2 = models.CharField(db_column='Colour_2', max_length=50, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dir = models.CharField(db_column='Dir', max_length=255, db_collation='Polish_CI_AS', blank=True, null=True)  # Field name made lowercase.
    new = models.BooleanField(db_column='New', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Shoes'
    
    def __str__(self):
        return 'Coat'
    
    def properties(self):
        return f"""
        brand:          {self.brand}
        model:          {self.model}
        size:           {self.size}
        type:           {self.type}
        colour_1:       {self.colour_1}
        colour_2:       {self.colour_2}
        """


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='Polish_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='Polish_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='Polish_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='Polish_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='Polish_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='Polish_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='Polish_CI_AS')
    email = models.CharField(max_length=254, db_collation='Polish_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='Polish_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='Polish_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='Polish_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='Polish_CI_AS')
    model = models.CharField(max_length=100, db_collation='Polish_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='Polish_CI_AS')
    name = models.CharField(max_length=255, db_collation='Polish_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='Polish_CI_AS')
    session_data = models.TextField(db_collation='Polish_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
