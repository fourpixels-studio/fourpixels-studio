from django.shortcuts import render

def applications_list(request):
    return render(request, 'apps/applications-list.html', {'title_tag': "Applications"})
