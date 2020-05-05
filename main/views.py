from django.shortcuts import render

# Create your views here.
def ManageMainView(DisplayView):
    group = DisplayView.user.groups.values('name')
    context = {
        'group': group ,
    }
    return render(DisplayView,'Users/Main/Main.html',context)