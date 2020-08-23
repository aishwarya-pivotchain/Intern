from pytube import YouTube
import pandas as pd

SAVE_PATH = "E:/"
df = pd.read_csv('armed_robbery_videos_links - Sheet1.csv')
for i in df['Videos']:
    try:

        yt = YouTube(i)
    except:
        print("Connection Error")
    stream = yt.streams.first()
    try:
        # downloading the video
        print('Downloading')
        stream.download(SAVE_PATH)
        print('Downloaded')

    except:
        print("Some Error!")
print('Task Completed!')



