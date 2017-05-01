from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from classes.models import Category, Lecture
from accounts.models import Profile


def classes(request):
    # カテゴリー、レクチャーすべてを取得して、渡す
    categories = Category.objects.all()
    lectures = Lecture.objects.all()

    return render(request,
                  'classes/classes.html',
                  {'categories': categories,
                   'lectures': lectures,
                   })


def lectures(request, klass_name):
    # URLで指定された講座と一致するクラスを取り出す
    lectures = Lecture.objects.filter(klass_name=klass_name).order_by('lecture_num')

    return render(request,
                  'classes/lectures.html',
                  {'lectures': lectures})


def lecture(request, klass_name, pk):
    # ログインしてないと、ホームへリダイレクト
    if not request.user.is_authenticated:
        messages.add_message(request, messages.INFO, 'ログインしてください')
        return redirect('/home')

    # URLで指定された番号と一致するIDのデータのみ取り出す
    the_lecture = get_object_or_404(Lecture, pk=pk)

    # 一度みたレクチャーを保存
    userid = request.user.id
    user = User.objects.get(id=userid)
    user_profile = Profile.objects.get(user=user)
    user_profile.watch_history.add(the_lecture)

    # 全レクチャーをレクチャー番号順に並べる
    lectures = Lecture.objects.filter(klass_name=klass_name).order_by('lecture_num')

    return render(request,
                  'classes/lecture.html',
                  {
                      'lectures': lectures,
                      'the_lecture': the_lecture
                  })



