from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.context_processors import request

from .models import *


def hello_view(request):
    return HttpResponse(
        """
        <h1>Bosh sahifa</h1>
        <hr>
        <p>Bugun django orqali view va url'larni o'rganyapmiz!</p>
        """
    )


def home_view(request):
    return render(request, 'home.html')


def talabalar_view(request):
    if request.method == "POST":
        Talaba.objects.create(
            ism=request.POST.get('ism'),
            guruh=request.POST.get('guruh'),
            kurs=request.POST.get('kurs'),
            kitob_soni=request.POST.get('kitob_soni')
        )
        return redirect('talabalar')
    talabalar = Talaba.objects.all()

    search = request.GET.get('search')
    if search is not None:
        talabalar = talabalar.filter(ism__contains=search)

    context = {
        'talabalar': talabalar,
        'search': search,
    }
    return render(request, 'talabalar.html', context)


def talaba_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        'talaba': talaba,
    }
    return render(request, 'talaba.html', context)


def talaba_delete_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    talaba.delete()
    return redirect('talabalar')


def bitiruvchilar_view(request):
    talabalar = Talaba.objects.filter(kurs=4)
    context = {
        'talabalar': talabalar,
    }
    return render(request, 'bitiruvchilar.html', context)


def mualliflar_view(request):
    if request.method == "POST":
        Muallif.objects.create(
            ism=request.POST.get('ism'),
            tirik=True if request.POST.get('tirik') == 'on' else False,
            jins=request.POST.get('jins'),
            t_sana=request.POST.get('t_sana'),
            kitob_soni=None if request.POST.get('kitob_soni') == '' else request.POST.get('kitob_soni'),
        )

        return redirect('mualliflar')
    mualliflar = Muallif.objects.all()
    context = {
        'mualliflar': mualliflar,
    }
    return render(request, 'mualliflar.html', context)


def muallif_delete_confirm_view(request, id):
    muallif = Muallif.objects.get(id=id)
    context = {
        'muallif': muallif,
    }
    return render(request, 'maullif-delete-confirm.html', context)


def muallif_delete_view(request, id):
    muallif = Muallif.objects.get(id=id)
    muallif.delete()
    return redirect('mualliflar')


def kitoblar_view(request):
    kitoblar = Kitob.objects.all()
    context = {
        'kitoblar': kitoblar,
        'mualliflar': Muallif.objects.all(),
    }
    return render(request, 'kitoblar.html', context)


def kitob_qoshish_view(request):
    if request.method == "POST":
        Kitob.objects.create(
            nom=request.POST.get('nom'),
            janr=request.POST.get('janr'),
            sahifa=0 if request.POST.get('sahifa') == "" else int(request.POST.get('sahifa')),
            muallif=Muallif.objects.get(id=request.POST.get('muallif_id')),
        )
        return redirect('kitoblar')
    context = {
        'mualliflar': Muallif.objects.all(),
    }
    return render(request, 'kitob-qoshish.html', context)

