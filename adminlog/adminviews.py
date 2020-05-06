from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only
from .models import *
from user.models import *
from main.models import *
from institution.models import *

