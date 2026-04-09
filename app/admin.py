from django.contrib import admin
from .models import LoginPage
from .models import RegisterPage
from.models import message



admin.site.register(LoginPage)
admin.site.register(RegisterPage)
admin.site.register(message)
