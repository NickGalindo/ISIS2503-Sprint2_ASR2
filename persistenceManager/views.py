from django.shortcuts import render

# Create your views here.
def sendImg(request):
    if request.method == "POST":
        img = request.FILES["img"]
        print(type(img))
        print(img.name)
