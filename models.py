# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Attribute(models.Model):
    attributeid = models.IntegerField(db_column='attributeId', primary_key=True)  # Field name made lowercase.
    attributename = models.CharField(db_column='attributeName', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Attribute'


class Attributegroup(models.Model):
    attributegroupid = models.IntegerField(db_column='attributeGroupId', primary_key=True)  # Field name made lowercase.
    attributegroupname = models.CharField(db_column='attributeGroupName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    attributeid = models.ForeignKey(Attribute, models.DO_NOTHING, db_column='attributeId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AttributeGroup'


class Categoryproduct(models.Model):
    categoryid = models.AutoField(db_column='CategoryId', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=200)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CategoryProduct'


class Order(models.Model):
    orderid = models.IntegerField(db_column='orderId', primary_key=True)  # Field name made lowercase.
    orderuserid = models.ForeignKey('EcommerceUser', models.DO_NOTHING, db_column='orderUserId')  # Field name made lowercase.
    orderamount = models.IntegerField(db_column='orderAmount', blank=True, null=True)  # Field name made lowercase.
    ordertrackingnumber = models.IntegerField(db_column='orderTrackingNumber', blank=True, null=True)  # Field name made lowercase.
    orderaddress = models.CharField(db_column='OrderAddress', max_length=200, blank=True, null=True)  # Field name made lowercase.
    orderemail = models.CharField(db_column='orderEmail', max_length=45, blank=True, null=True)  # Field name made lowercase.
    orderdate = models.DateField(db_column='orderDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Order'


class Orderdetail(models.Model):
    detaild = models.IntegerField(primary_key=True)
    detailorderid = models.ForeignKey(Order, models.DO_NOTHING, db_column='detailOrderId')  # Field name made lowercase.
    detailproductid = models.ForeignKey('Product', models.DO_NOTHING, db_column='detailProductId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OrderDetail'


class Product(models.Model):
    productid = models.AutoField(db_column='productId', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=200)  # Field name made lowercase.
    productdesc = models.CharField(db_column='productDesc', max_length=400, blank=True, null=True)  # Field name made lowercase.
    productcategoryid = models.ForeignKey(Categoryproduct, models.DO_NOTHING, db_column='productCategoryId')  # Field name made lowercase.
    producttypeid = models.ForeignKey('Producttype', models.DO_NOTHING, db_column='productTypeId')  # Field name made lowercase.
    productimage = models.TextField(db_column='productImage', blank=True, null=True)  # Field name made lowercase.
    productprice = models.CharField(db_column='productPrice', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Product'


class Producttype(models.Model):
    typeid = models.AutoField(db_column='typeId', primary_key=True)  # Field name made lowercase.
    producttypename = models.CharField(db_column='productTypeName', max_length=200)  # Field name made lowercase.
    attributegroupid = models.ForeignKey(Attributegroup, models.DO_NOTHING, db_column='attributeGroupId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ProductType'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey('EcommerceUser', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('EcommerceUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EcommerceProfile(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    bio = models.TextField()
    image = models.CharField(max_length=200)
    user = models.ForeignKey('EcommerceUser', models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'ecommerce_profile'


class EcommerceStar(models.Model):

    class Meta:
        managed = False
        db_table = 'ecommerce_star'


class EcommerceUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=255)
    email = models.CharField(unique=True, max_length=254)
    is_active = models.IntegerField()
    is_staff = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    mobile = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ecommerce_user'


class EcommerceUserGroups(models.Model):
    user = models.ForeignKey(EcommerceUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ecommerce_user_groups'
        unique_together = (('user', 'group'),)


class EcommerceUserUserPermissions(models.Model):
    user = models.ForeignKey(EcommerceUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ecommerce_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Users(models.Model):
    userid = models.PositiveIntegerField(db_column='userId', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='firstName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='lastName', max_length=150, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    dob = models.DateField(blank=True, null=True)
    mobilenumber = models.CharField(db_column='mobileNumber', max_length=200)  # Field name made lowercase.
    city = models.CharField(max_length=150, blank=True, null=True)
    state = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    zip = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Wishlist(models.Model):
    wishlistid = models.IntegerField(db_column='wishlistId', primary_key=True)  # Field name made lowercase.
    wishlistuserid = models.IntegerField(db_column='wishlistUserId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'wishlist'
