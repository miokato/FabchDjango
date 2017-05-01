from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from social.pipeline.partial import partial
from accounts.models import Profile
from django.db.models.query import EmptyQuerySet

@partial
def save_profile(backend, strategy, uid, details, social,  user, response, *args, **kwargs):
    # save user_profile
    print('hello')
    _user = User.objects.get(id=user.id)

    if Profile.objects.filter(user=_user).exists():
        pass
    else:
        profile = Profile(user=_user)
        profile.save()


    # ログインしたらフラッシュメッセージでお知らせ
    messages.add_message(strategy.request, messages.INFO, 'ログインしました')
    redirect('accounts.views.profile')
