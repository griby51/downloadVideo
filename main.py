from pytube import YouTube

link = input("Enter the link of the video: ")
yt = YouTube(link)
print("Title: ", yt.title)
print("Number of views: ", yt.views)
yd = yt.streams.get_highest_resolution()
yd.download(filename="video.mp4")