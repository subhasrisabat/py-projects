from pytube import YouTube
yt = YouTube('https://youtu.be/kkc2Q6egJHY')
yt.streams.filter(progressive=True,file_extension='mp4').order_by(
    'resolution').desc().first().download()
