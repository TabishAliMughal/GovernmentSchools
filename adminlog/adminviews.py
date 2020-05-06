from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group , User
from authentication.user_handeling import unauthenticated_user, allowed_users, admin_only


@login_required(login_url='login')
@allowed_users(allowed_roles=['Admin'])
def ManageAllProfilesView(ProfilesView):
    user = ProfilesView.user.groups.values('name')
    teachers = Group.objects.get(name="Teachers")
    teachers = teachers.user_set.all()
    context = {
        'teachers': teachers ,
        'user': user ,
    }
    return render(ProfilesView,'Users/Admin/Profiles.html',context)