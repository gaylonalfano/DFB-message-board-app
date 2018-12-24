# posts/admin.py
from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post)
# Django now knows to display our posts app and its
# database model Post on the admin page.
