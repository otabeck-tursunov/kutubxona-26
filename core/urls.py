from django.contrib import admin
from django.urls import path

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view),
    path('', home_view, name='home'),
    path('talabalar/', talabalar_view, name='talabalar'),
    path('talabalar/<int:talaba_id>/', talaba_view),
    path('talabalar/<int:talaba_id>/delete/', talaba_delete_view),
    path('bitiruvchilar/', bitiruvchilar_view, name='bitiruvchilar'),
    path('mualliflar/', mualliflar_view, name='mualliflar'),
    path('mualliflar/<int:id>/delete-confirm/', muallif_delete_confirm_view),
    path('mualliflar/<int:id>/delete/', muallif_delete_view),
    path('kitoblar/', kitoblar_view, name='kitoblar'),
    path('kitob-qoshish/', kitob_qoshish_view),
]
