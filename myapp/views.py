import json
import torch
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from PIL import Image
from transformers import AutoImageProcessor, AutoModelForImageClassification
import base64
import io

# Initialize the model and image processor
model_path = "sakshamkr1/deepfake_vit"  # Directory containing the model files
model = AutoModelForImageClassification.from_pretrained(model_path, use_safetensors=True)
image_processor = AutoImageProcessor.from_pretrained(model_path)

def preprocess_image(image_data):
    image = Image.open(io.BytesIO(image_data)).convert("RGB")
    inputs = image_processor(images=image, return_tensors="pt")
    return inputs

@csrf_exempt
def predict(request):
    if request.method == 'POST':
        # Read the image data from the request
        data = json.loads(request.body)
        image_data = base64.b64decode(data['image'])

        # Preprocess the image
        inputs = preprocess_image(image_data)

        # Make prediction
        with torch.no_grad():
            logits = model(**inputs).logits
        
        predicted_label = logits.argmax(-1).item()
        id2label = model.config.id2label

        return JsonResponse({"result": id2label[predicted_label]})
    else:
        return JsonResponse({"error": "Only POST method is allowed"}, status=405)

def upload(request):
    return render(request, 'upload.html')
