from django.apps import AppConfig


class AuthenticationAppConfig(AppConfig):
    name = 'ecommerce'
    label = 'ecommerce'
    verbose_name = 'Ecommerce'
    print("creating profile")

    def ready(self):
        import ecommerce.Exceptions.signals

# This is how we register our custom app config with Django. Django is smart
# enough to look for the `default_app_config` property of each registered app
# and use the correct app config based on that value.
default_app_config = 'ecommerce.AuthenticationAppConfig'