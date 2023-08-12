from pytube import YouTube

def download(videos,video_resolutions):
    while True:
        i = 1

        for resolution in video_resolutions:
            print(f"{i}. {resolution}")
            i += 1

        choice = int(input("\nChoose A resolution please: "))

        if 1 <=choice < i:
            resolutions_to_download = video_resolutions[choice -1]
            print(f"Downloading the video with download resolution {resolutions_to_download} ...")

            videos[choice-1].download()

            print("\nVideo was successfully downloaded.")
            break

        else:
            print("Invalid choice!!\n\n")

def get_resolutions_and_extensions(link):
    my_video = YouTube(link)
    video_resolutions = []
    videos = []


    for streams in my_video.streams.order_by('resolution').filter(only_video=True,adaptive=True):
        video_resolutions.append(streams.resolution)
        videos.append(streams)
    


    return videos,video_resolutions



   


url = input("Enter the youtube video URL:\n")

videos,video_resolutions = get_resolutions_and_extensions(link=url)
get_resolutions_and_extensions(link = url)

download(videos,video_resolutions)