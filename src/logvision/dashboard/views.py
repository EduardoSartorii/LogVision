from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def home_page(request):
    username = request.user.username
    return render(request, 'home.html',{'username': username})