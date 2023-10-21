from django.http import JsonResponse
from django.shortcuts import HttpResponse, render
from storages.backends.gcloud import GoogleCloudStorage

storage = GoogleCloudStorage()

# Create your views here.
def sendImg(request):
    if request.method == "POST":
        img = request.FILES["img"]

        try:
            path = storage.save(img.name, img)
            return JsonResponse({"storage_path": storage.url(path)}, status=201)
        except Exception as e:
            print(e)
            return HttpResponse("Couldn't save file to Google Cloud Storage", status=503)
