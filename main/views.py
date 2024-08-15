from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse

from .models import Chat, Message
from .forms import ChatForm
from main import api

import datetime
import pytz




def main(request):
    chats = Chat.objects.all()
    context = {'chats': chats}
    return render(request, 'main.html', context)


def chat_view(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    form = ChatForm()
    messages = chat.messages.all()
    chats = Chat.objects.all()
    context = {'chat': chat, 'form': form, 'messages': messages, 'chats': chats}
    return render(request, 'index.html', context)


def send_message(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)

    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_message = form.cleaned_data['message']
            yandex_response = api.get_response(user_message)

            Message.objects.create(chat=chat, sender='user', text=user_message)
            Message.objects.create(chat=chat, sender='GPT', text=yandex_response)

            return JsonResponse({'response': yandex_response})

    return JsonResponse({'response': 'Ошибка!'})


def create_chat(request):
    current_datetime = datetime.datetime.now()
    name = f"Chat {current_datetime.strftime('%Y.%m.%d - %H:%M')}"
    Chat.objects.create(name=name, created_at=current_datetime.strftime('%Y.%m - %H:%M'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_chat(request, chat_id):
    chat = get_object_or_404(Chat, id=chat_id)
    chat.delete()
    return redirect('main')
