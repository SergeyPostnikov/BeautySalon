from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from .payments import create_payment, get_payment_status
from django.urls import reverse
from random import shuffle
from assets.db import record, salons, services, reviews
from beauty.models import Master, Salon, Service


def serialize_masters(masters_qs):
    masters = []
    for master_obj in masters_qs:
        master = {
            'photo': master_obj.photo.url,
            'fullname': master_obj.fullname,
            'profession': master_obj.profession,
        }
        masters.append(master)


def payment(request, pk):

    #TODO запрос из базы данных Session по pk

    description = f"Оплата заказа № {record['id']} за {record['service_name']}."
    amount = record['price']

    # Создайте платеж в ЮKassa
    payment = create_payment(
        record['id'],
        amount,
        description,
        request.build_absolute_uri(
            reverse('payment_success', kwargs={'pk': record['id']})
        )
    )
    record['payment_id'] = payment.id

    # Перенаправьте пользователя на страницу оплаты
    return redirect(payment.confirmation.confirmation_url)


def payment_success(request, pk):

    #TODO запрос из базы данных Session по pk

    status = get_payment_status(record['payment_id'])

    if status == 'succeeded':
        # Найти заказ по payment_id и обновить его статус
        record['paid'] = True

    context = {
        'record': record,
    }
    return redirect('/')


def logout(request):
    auth_logout(request)
    return render(request, "index.html")


def index(request):
    flatten_services = []
    for service in services:
        flatten_services.extend(service['services'])
    shuffle(flatten_services)

    context = {
        'salons': salons,
        'services': flatten_services,
        'reviews': reviews,
        'masters': Master.objects.all()[:5]
    }
    return render(request, 'index.html', context=context)


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


def service(request):
    context = {
        'salons': Salon.objects.all(),
        'masters': Master.objects.all()[:5],
        'services': Service.objects.all()
    }
    return render(request, 'service.html', context=context)


def service_finally(request):
    print('Update page', request.method)

    if request.method == "POST":
        print(request.POST['name'])
        print(request.POST['phonenumber'])
        record['active'] = True
    else:
        record['active'] = False
    context = {
        'record': record,
    }
    return render(request, 'service_finally.html', context=context)