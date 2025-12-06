import os
from moviepy.editor import VideoFileClip

def convert_mp4_to_gif(source_folder, output_folder=None, target_fps=10, resize_width=480):
    """
    将文件夹内的所有 mp4 视频转换为 gif。
    
    :param source_folder: 包含 mp4 视频的文件夹路径
    :param output_folder: gif 输出路径（如果为 None，则保存在源文件夹中）
    :param target_fps: gif 的帧率（默认10，越低文件越小）
    :param resize_width: gif 的宽度（默认480像素，高度按比例缩放，None则不缩放）
    """
    
    # 检查源文件夹是否存在
    if not os.path.exists(source_folder):
        print(f"错误: 找不到文件夹 '{source_folder}'")
        return

    # 如果指定了输出文件夹，确保它存在
    if output_folder and not os.path.exists(output_folder):
        os.makedirs(output_folder)
        print(f"已创建输出文件夹: {output_folder}")

    # 获取文件夹内所有文件
    files = [f for f in os.listdir(source_folder) if f.lower().endswith('.mp4')]
    
    if not files:
        print("未找到 .mp4 文件。")
        return

    print(f"找到 {len(files)} 个视频文件，开始转换...")

    for filename in files:
        input_path = os.path.join(source_folder, filename)
        
        # 构建输出文件名
        gif_filename = os.path.splitext(filename)[0] + ".gif"
        if output_folder:
            output_path = os.path.join(output_folder, gif_filename)
        else:
            output_path = os.path.join(source_folder, gif_filename)

        print(f"正在处理: {filename} -> {gif_filename} ...")
        
        try:
            # 加载视频
            clip = VideoFileClip(input_path)
            
            # 1. 调整尺寸 (GIF如果不缩小，体积会非常大)
            if resize_width:
                clip = clip.resize(width=resize_width)
            
            # 2. 写入GIF (设置fps，fps越低生成速度越快，文件越小)
            # program='ffmpeg' 通常速度更快
            clip.write_gif(output_path, fps=target_fps, program='ffmpeg', verbose=False, logger=None)
            
            # 关闭资源
            clip.close()
            print(f"✅ 完成: {output_path}")
            
        except Exception as e:
            print(f"❌ 转换 {filename} 失败: {e}")

    print("\n所有任务已完成！")

# ==========================================
# 在这里修改你的配置
# ==========================================

if __name__ == "__main__":
    # 把这里的路径改成存放视频的实际文件夹路径
    # 例如 Windows: r"C:\Users\Name\Videos\MyShorts"
    # 例如 Mac/Linux: "./videos"
    my_video_folder = r"D:\Website\result" 
    
    # 可选：指定一个单独的文件夹存放生成的GIF，保持整洁
    my_output_folder = r"D:\Website\gif_result"

    convert_mp4_to_gif(
        source_folder=my_video_folder, 
        output_folder=my_output_folder,
        target_fps=12,      # 推荐 10-15，太高会导致文件巨大
        resize_width=480    # 推荐 360-600，如果不希望缩放大小，请改成 None
    )