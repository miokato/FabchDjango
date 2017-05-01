from django.shortcuts import render, redirect
from datetime import datetime
from dateutil import relativedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from classes.models import Lecture
from accounts.models import Profile


def login(request):
    return render(request, 'accounts/login.html')


@login_required
def profile(request):
    # お気に入り
    # プロフィール詳細
    # 視聴履歴
    userid = request.user.id
    user = User.objects.get(id=userid)
    user_profile = Profile.objects.get(user=user)
    watched_lectures = Lecture.objects\
        .filter(profile__id=user_profile.id)\
        .order_by('klass_name','lecture_num')

    return render(request,
                  'accounts/profile.html',
                  {'user': request.user,'watched_lectures': watched_lectures})


def logout(request):
    auth_logout(request)
    messages.add_message(request, messages.INFO, 'ログアウトしました')

    return redirect('/home')
