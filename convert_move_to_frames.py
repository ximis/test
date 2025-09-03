import cv2
import os

def extract_all_frames(video_path, output_dir="frames"):
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    
    # 检查视频是否成功打开
    if not cap.isOpened():
        print("无法打开视频文件")
        return
    
    # 获取视频的帧率（FPS）和总帧数
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # 逐帧读取
    frame_count = 0
    while True:
        success, frame = cap.read()
        if not success:
            break
        
        # 计算当前帧的毫秒时间
        ms_time = (frame_count / fps) * 1000
        
        # 保存帧为图片
        output_path = os.path.join(output_dir, f"frame_{frame_count:06d}_{int(ms_time)}ms.jpg")
        cv2.imwrite(output_path, frame)
        
        # 打印帧号和对应的毫秒时间
        print(f"帧 {frame_count}: {ms_time:.2f}ms")
        
        frame_count += 1
    
    # 释放视频对象
    cap.release()
    print(f"提取完成，共 {frame_count} 帧")

# 示例调用
video_path = "example.mp4"  # 替换为你的视频路径
extract_all_frames(video_path)
