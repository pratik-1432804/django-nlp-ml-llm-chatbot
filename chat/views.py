from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from nlp.preprocess import preprocess_text   # ✅ ADD THIS

@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        body = json.loads(request.body)
        user_message = body.get("message", "")

        cleaned_text = preprocess_text(user_message)

        return JsonResponse({
            "original_message": user_message,
            "cleaned_message": cleaned_text,
            "reply": "NLP preprocessing working"
        })