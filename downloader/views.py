from django.shortcuts import render
from django.http import HttpResponse
from pytube import YouTube

def home(request):
    return render(request, 'home.html')

def download_video(request):
    if request.method == 'POST':
        url = request.POST.get('url')
        try:
            yt = YouTube(url)
            stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
            stream.download()
            return HttpResponse(f"Downloaded: {yt.title}")
        except Exception as e:
            return HttpResponse(f"Error: {str(e)}")
    return HttpResponse("Invalid request")
