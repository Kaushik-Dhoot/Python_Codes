from pytube import YouTube

link = input("Enter the url :") #Url of video from youtube
file_name = input('Enter file name :') #file name to be saved
file_name = file_name+'.mkv'
directory = 'E:\Yt downloader python' # location where to be stored

yt = YouTube(link)
yd = yt.streams.get_highest_resolution()
yd.download(directory,file_name) 
