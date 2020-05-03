from django.shortcuts import render

# Create your views here.
def ManageMainView(DisplayView):
    user = DisplayView.user.groups.values('name')
    context = {

        'user': user ,
    }
    return render(DisplayView,'Users/Main/Main.html',context)