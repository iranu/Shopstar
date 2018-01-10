
import jwt

from datetime import datetime, timedelta

from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models

class UserManager(BaseUserManager):
    """
    Django requires that custom users define their own Manager class. By
    inheriting from `BaseUserManager`, we get a lot of the same code used by
    Django to create a `User`.

    All we have to do is override the `create_user` function which we will use
    to create `User` objects.
    """

    def create_user(self, username, email, password=None):
        """Create and return a `User` with an email, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    # Each `User` needs a human-readable unique identifier that we can use to
    # represent the `User` in the UI. We want to index this column in the
    # database to improve lookup performance.
    username = models.CharField(db_index=True, max_length=255, unique=True)

    # We also need a way to contact the user and a way for the user to identify
    # themselves when logging in. Since we need an email address for contacting
    # the user anyways, we will also use the email for logging in because it is
    # the most common form of login credential at the time of writing.
    email = models.EmailField(db_index=True, unique=True)

    # When a user no longer wishes to use our platform, they may try to delete
    # their account. That's a problem for us because the data we collect is
    # valuable to us and we don't want to delete it. We
    # will simply offer users a way to deactivate their account instead of
    # letting them delete it. That way they won't show up on the site anymore,
    # but we can still analyze the data.
    is_active = models.BooleanField(default=True)

    # The `is_staff` flag is expected by Django to determine who can and cannot
    # log into the Django admin site. For most users this flag will always be
    # false.
    is_staff = models.BooleanField(default=False)

    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp reprensenting when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    # More fields required by Django when specifying a custom user model.

    # The `USERNAME_FIELD` property tells us which field we will use to log in.
    # In this case we want it to be the email field.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        """
        Returns a string representation of this `User`.

        This string is used when a `User` is printed in the console.
        """
        return self.email

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token ()

    def get_full_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically this would be the user's first and last name. Since we do
        not store the user's real name, we return their username instead.
        """
        return self.username

    def get_short_name(self):
        """
        This method is required by Django for things like handling emails.
        Typically, this would be the user's first name. Since we do not store
        the user's real name, we return their username instead.
        """
        return self.username

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')


class Star(models.Model):
    jazz = models.CharField


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

    def __str__(self):

        return self.attributename

    class Meta:
        managed = False
        db_table = 'Attribute'


class Attributegroup(models.Model):
    attributegroupid = models.IntegerField(db_column='attributeGroupId', primary_key=True)  # Field name made lowercase.
    attributegroupname = models.CharField(db_column='attributeGroupName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    attributeid = models.ForeignKey (Attribute, models.DO_NOTHING, db_column='attributeId')  # Field name made lowercase.

    def __str__(self):

        return self.attributegroupname

    class Meta:
        managed = False
        db_table = 'AttributeGroup'


class Categoryproduct(models.Model):
    categoryid = models.AutoField(db_column='CategoryId', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=200)  # Field name made lowercase.

    def __str__(self):

        return self.categoryname

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

    def __str__(self):

        return 'Orderid=' + str(self.orderid)

    class Meta:
        managed = False
        db_table = 'Order'


class Orderdetail(models.Model):
    detaild = models.IntegerField(primary_key=True)
    detailorderid = models.ForeignKey(Order, models.DO_NOTHING, db_column='detailOrderId')  # Field name made lowercase.
    detailproductid = models.ForeignKey('Product', models.DO_NOTHING, db_column='detailProductId')  # Field name made lowercase.

    def __str__(self):

        return 'Detailid=' + str(self.detaild)

    class Meta:
        managed = False
        db_table = 'OrderDetail'

class Producttype(models.Model):
    typeid = models.AutoField(db_column='typeId', primary_key=True)  # Field name made lowercase.
    producttypename = models.CharField(db_column='productTypeName', max_length=200)  # Field name made lowercase.
    attributegroupid = models.ForeignKey(Attributegroup, models.DO_NOTHING, db_column='attributeGroupId')  # Field name made lowercase.

    def __str__(self):
        return 'Producttypeid=' + str(self.typeid)

    class Meta:
        managed = False
        db_table = 'ProductType'


class Product(models.Model):
    productid = models.AutoField(db_column='productId', primary_key=True)  # Field name made lowercase.
    productname = models.CharField(db_column='productName', max_length=200)  # Field name made lowercase.
    productdesc = models.CharField(db_column='productDesc', max_length=45, blank=True, null=True)  # Field name made lowercase.
    productcategoryid = models.ForeignKey(Categoryproduct, models.DO_NOTHING, db_column='productCategoryId')  # Field name made lowercase.
    producttypeid = models.ForeignKey(Producttype, models.DO_NOTHING, db_column='productTypeId')  # Field name made lowercase.
    productimage = models.TextField (db_column='productImage', blank=True, null=True)  # Field name made lowercase.
    productprice = models.CharField (db_column='productPrice', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.productname

    class Meta:
        managed = False
        db_table = 'Product'

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


class TimestampedModel(models.Model):
    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp reprensenting when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

        # By default, any model that inherits from `TimestampedModel` should
        # be ordered in reverse-chronological order. We can override this on a
        # per-model basis as needed, but reverse-chronological is a good
        # default ordering for most models.
        #ordering = ['-created_at', '-updated_at’]


class Profile(TimestampedModel):
    # As mentioned, there is an inherent relationship between the Profile and
    # User models. By creating a one-to-one relationship between the two, we
    # are formalizing this relationship. Every user will have one -- and only
    # one -- related Profile model.
    user = models.OneToOneField(
        'ecommerce.User', on_delete=models.CASCADE
    )

    # Each user profile will have a field where they can tell other users
    # something about themselves. This field will be empty when the user
    # creates their account, so we specify `blank=True`.
    bio = models.TextField(blank=True)

    # In addition to the `bio` field, each user may have a profile image or
    # avatar. This field is not required and it may be blank.
    image = models.URLField(blank=True)

    # A timestamp representing when this object was created.
    created_at = models.DateTimeField(auto_now_add=True)

    # A timestamp reprensenting when this object was last updated.
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username