from django.http import request
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PopUpForms
from .models import PopUp
# Create your views here.


@login_required()
def add_user(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.add_message(request, messages.SUCCESS,
                                 'User successfully created name: %s.' % (instance.username.title))
            return redirect('popups:home')
    else:
        form = UserCreationForm(request.POST or None)
    context = {
        'title': 'add user',
        'form': form
    }
    return render(request, 'registration/register_user.html', context)


@login_required()
def home(request):
    popup_cards = PopUp.objects.all()
    card_activity = PopUp.objects.all()[:10]
    form = PopUpForms(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('popups:home')
    else:
        form = PopUpForms()
    context = {
        "title": "card list",
        "form": form,
        "cards": popup_cards,
        "card_activity": card_activity
    }
    return render(request, 'home.html', context)


@login_required()
def create_card(request):
    form = PopUpForms(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('popups:home')
    else:
        form = PopUpForms()
    context = {
        "title": "add card",
        "form": form,
    }
    return render(request, 'create_card.html', context)


@login_required()
def card_details(request, ref_code):
    card = get_object_or_404(PopUp, ref_code=ref_code)
    form = PopUpForms(request.POST or None,
                      request.FILES or None, instance=card)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.updated_by = request.user
        instance.save()
        return redirect('popups:details', ref_code=instance.ref_code)
    context = {
        "title": "card update",
        "instance": card,
        "form": form
    }
    return render(request, "card_details.html", context)


@login_required()
def delete_card(request, *args, **kwargs):
    card_code = kwargs.get('ref_code')
    data = get_object_or_404(PopUp, ref_code=card_code)
    if request.method == "POST":
        data.delete()
        messages.add_message(request, messages.SUCCESS,
                             'Card successfully deleted.')
        return redirect('popups:home')
    context = {
        "title": "delete",
        "instance": data
    }
    return render(request, "delete.html", context)


def card_preview(request, *args, **kwargs):
    card_code = kwargs.get('ref_code')
    data = get_object_or_404(PopUp, ref_code=card_code)
    context = {
        "title": "delete",
        "instance": data
    }
    return render(request, "card_preview.html", context)
