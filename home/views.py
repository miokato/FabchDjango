from django.shortcuts import render, get_object_or_404
from classes.models import Lecture
from datetime import datetime
from dateutil import relativedelta


def home(request):
    # 今月アップロードされたすべてのクラスの一つ目の動画を取得
    now = datetime.now()
    one_month_ago = now - relativedelta.relativedelta(months=1)
    lectures = Lecture.objects.filter(lecture_num=1, pub_date__gt=one_month_ago)
    return render(request, 'home/home.html', {'lectures': lectures})




