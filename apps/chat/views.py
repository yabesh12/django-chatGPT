from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import os

# ChatGPT api key
GPT_API_KEY = os.environ.get("GPT_API_KEY")

def chat(request):
    chats = Chat.objects.all()
    return render(request, 'chat.html', {
        'chats': chats,
    })

@csrf_exempt
def Ajax(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest': # Check if request is Ajax

        text = request.POST.get('text')
        print(text)
        openai.api_key = GPT_API_KEY
        res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"{text}"}
        ]
        )

        response = res.choices[0].message["content"]
        print(response)

        chat = Chat.objects.create(
            text = text,
            gpt = response
        )

        return JsonResponse({'data': response,})
    return JsonResponse({})

@csrf_exempt
def ajax_remove_data(request):
    chats = Chat.objects.all().delete()
    return render(request, 'chat.html')