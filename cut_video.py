import os
import random
import math
from moviepy.editor import VideoFileClip, concatenate_videoclips
import configparser

# 读取配置文件
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

Output_Dir = config["Cut_VIDEO"]["Cut_Video_Output_Dir"]
Download_Dir = config["Web_API"]["Download_Path"]

# 遍历文件夹
def walkFile(file):
    filelist=[] # 保存文件绝对路径的列表   
    for root, dirs, files in os.walk(file):
    # root 表示当前正在访问的文件夹路径
    # dirs 表示该文件夹下的子目录名list
    # files 表示该文件夹下的文件list
    # 遍历文件
        for f in files:
            if (f.endswith('.mp4')):
                source_path = os.path.join(root, f)
                filelist.append(source_path)
    return filelist

def cut_videos(filelist):
    for item in filelist:  # 遍历每个绝对路径对应的文件
        clip = VideoFileClip(item)  # 创建 from moviepy.editor import VideoFileClip 对象
        middle = math.floor(clip.duration // 2)
        print(middle)
        endpoint1 = random.randint(0, middle)
        endpoint2 = random.randint(middle, math.floor(clip.duration))

        clip1 =VideoFileClip(item).subclip(0, endpoint1 - 0.5)
        clip2 =VideoFileClip(item).subclip(endpoint1,  middle)
        clip3 =VideoFileClip(item).subclip(middle,  endpoint2)
        clip4 =VideoFileClip(item).subclip(endpoint2 + 0.5)

        final_clip = concatenate_videoclips([clip1,clip2, clip3, clip4])
        output_path = os.path.join(Output_Dir, item.split('/')[-1])
        final_clip.write_videofile(output_path,audio_codec="aac")


def main():
    cut_videos(walkFile(Download_Dir))

if __name__ == '__main__':
    main()