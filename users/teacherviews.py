from django.shortcuts import render



def ManageTeacherProfileView(ProfileView):
    user = ProfileView.user.groups.values('name')
    print(user)
    context = {
        'user': user ,
    }
    return render(ProfileView,'Users/Teacher/Profile.html',context)