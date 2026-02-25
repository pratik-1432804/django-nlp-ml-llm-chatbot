from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        body = json.loads(request.body)
        user_message = body.get("message", "")

        return JsonResponse({
            "user_message": user_message,
            "reply": "Hello! Chat API is working."
        })