'''
Author: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
Date: 2025-12-23 08:16:49
LastEditors: error: error: git config user.name & please set dead value or install git && error: git config user.email & please set dead value or install git & please set dead value or install git
LastEditTime: 2025-12-23 08:26:52
FilePath: \脚本\video2pic.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import cv2
import os
import threading

def video_to_frames(video_path, outPutDirName):
    times = 0
    
    # 提取视频的频率，每1帧提取一个
    frame_frequency = 2
    
	# 如果文件目录不存在则创建目录
    if not os.path.exists(outPutDirName):
        os.makedirs(outPutDirName)
        
    # 读取视频帧
    camera = cv2.VideoCapture(video_path)
    name=video_path.split('/')[-1].split('.')[0]
    print(name)
    while True:
        times = times + 1
        res, image = camera.read()
        if not res:
            print('not res , not image')
            break
        if times % frame_frequency == 0:
            # print(video_path)
            # pass
            print(f'{outPutDirName}/{name}_{str(times)}.jpg')
            cv2.imwrite(f'{outPutDirName}/{name}_{str(times)}.jpg', image)
            
    print('图片提取结束')
    camera.release()



if __name__ == "__main__":
    input_dir = r'../video/'       # 输入的video文件夹位置
    save_dir = r'../images/'         # 输出图片到当前目录video文件夹下
    count = 0   # 视频数
    # print(os.listdir(input_dir))
    for video_name in os.listdir(input_dir):
        video_path = os.path.join(input_dir, video_name)
        outPutDirName = os.path.join(save_dir, video_name[:-4])
        # print(video_path)
        threading.Thread(target=video_to_frames, args=(video_path, outPutDirName)).start()
        # video_to_frames(video_path,outPutDirName)
        count = count + 1
        print("%s th video has been finished!" % count)