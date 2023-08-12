from pytube import YouTube

'''download function with videos(link streams) and video resolution as parameters
we get those values from another function'''
def download(videos,video_resolutions):
    '''while loop needed to make sure loop function continues
    until download is complete'''
    while True:
        i = 1
    #starts from 1 to make the choice input smooth and clear
    #video_resolution is a list of avaliable video resolutions
    #for loop needed to display choice
        for resolution in video_resolutions:
            print(f"{i}. {resolution}")
            i += 1
    
    #leetting user choose resolution
        choice = int(input("\nChoose A resolution please: "))
    #if statement to make sure user chooses between 1 and the last possible value i
        if 1 <=choice < i:
            #[choice-1] because python list indexes start from 0 and we started from 1
            resolutions_to_download = video_resolutions[choice -1]
            print(f"Downloading the video with download resolution {resolutions_to_download} ...")
            #added a custom path for my downloads
            videos[choice-1].download(output_path = '/home/mhri/Youtube')

            print("\nVideo was successfully downloaded.")
            break

        else:
            print("Invalid choice!!\n\n")

def get_resolutions_and_extensions(link):
    my_video = YouTube(link)
    video_resolutions = []
    videos = []


    for streams in my_video.streams.order_by('resolution').filter(only_video=True,adaptive=True,mime_type='video/mp4'):
        video_resolutions.append(streams.resolution)
        videos.append(streams)
    


    return videos,video_resolutions


url = input("Enter the youtube video URL:\n")

videos,video_resolutions = get_resolutions_and_extensions(link=url)
get_resolutions_and_extensions(link = url)

download(videos,video_resolutions)


'''could be improved immensely and will do so but im tired now'''

#1)add option for audio
#2)add option to try again if user makes a mistake
#3)add option to download more than one video at the same time
#4)custom messsage for other exceptions
#5)Turn into GUI
#6)use OOP