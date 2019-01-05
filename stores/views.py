from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import StorePrimaryInfoForm, PolicyForm
from .models import Store


@login_required
def create_store(request):
    if request.method == 'POST':
        form = StorePrimaryInfoForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            store.profile = request.user.profile
            store.save()
            return redirect('add_store_details', store_id=store.pk)

    form = StorePrimaryInfoForm()
    return render(request, 'stores/create_store/create_store_level1.html', {'form': form})


def validate_store_name(request):
    name = request.GET.get('store_name', None)
    validate = {'is_taken': Store.objects.filter(name__iexact=name).exists()}
    if validate['is_taken']:
        validate['error_message'] = 'فروشگاه با این نام وجود دارد.'

    return JsonResponse(validate)


def add_store_details(request, store_id):
    if request.method == 'POST':
        store = Store.objects.get(id=store_id)
        store.description = request.POST['description']
        store.save()
        return redirect('add_store_policy', store_id=store_id)
    return render(request, 'stores/create_store/create_store_level2.html', {'store_id': store_id})


def add_store_logo(request, store_id):
    store = Store.objects.get(id=store_id)
    if request.method == 'POST':
        store.logo = request.FILES['file']
        store.save()
        return JsonResponse({})


def add_store_cover(request, store_id):
    store = Store.objects.get(id=store_id)
    if request.method == 'POST':
        store.cover_image = request.FILES['file']
        store.save()
        return JsonResponse({})


def add_store_policy(request, store_id):
    store = Store.objects.get(id=store_id)
    if request.method == 'POST':
        form = PolicyForm(request.POST)
        if form.is_valid():
            policy = form.save(commit=False)
            policy.store = store
            policy.save()
            return redirect('signup')
    form = PolicyForm()
    return render(request, 'stores/create_store/create_store_level3.html', {'form': form})
