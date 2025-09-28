import cv2
import os
from tqdm import tqdm  # 进度条工具（可选）

def resize_image_with_padding(
    image_path: str,
    output_path: str,
    target_size: tuple = (600, 600),
    fill_color: tuple = (0, 0, 0)  # 填充颜色（BGR格式，默认黑色）
):
    """
    调整图片尺寸为指定大小，通过填充黑边保持原始宽高比，避免拉伸变形
    """
    # 读取图片
    image = cv2.imread(image_path)
    if image is None:
        print(f"警告：无法读取图片 {image_path}")
        return

    h, w = image.shape[:2]
    target_h, target_w = target_size

    # 计算缩放比例
    scale = min(target_w / w, target_h / h)
    new_w = int(w * scale)
    new_h = int(h * scale)

    # 缩放图片
    resized = cv2.resize(image, (new_w, new_h), interpolation=cv2.INTER_AREA)

    # 计算填充边距
    pad_w = (target_w - new_w) // 2
    pad_h = (target_h - new_h) // 2
    # 上下左右填充（TOP, BOTTOM, LEFT, RIGHT）
    padded = cv2.copyMakeBorder(
        resized, pad_h, pad_h, pad_w, pad_w,
        cv2.BORDER_CONSTANT, value=fill_color
    )

    # 保存结果（自动覆盖同名文件，如需保留原始文件请修改输出路径）
    cv2.imwrite(output_path, padded)


def batch_resize_images(
    input_dir: str,
    output_dir: str,
    target_size: tuple = (600, 600),
    image_extensions: tuple = ('.jpg', '.jpeg', '.png', '.bmp')
):
    """
    批量处理文件夹内的图片
    """
    # 创建输出目录（若不存在）
    os.makedirs(output_dir, exist_ok=True)

    # 遍历输入目录下的所有文件
    image_files = [
        f for f in os.listdir(input_dir)
        if f.lower().endswith(image_extensions)
    ]

    for filename in tqdm(image_files, desc="处理进度"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        resize_image_with_padding(input_path, output_path, target_size)

    print(f"处理完成！共处理 {len(image_files)} 张图片，结果保存至 {output_dir}")


if __name__ == "__main__":
    # 配置参数
    input_folder = "/Users/cimorn/Documents/WebSite/IMSystem/images"   # 替换为你的输入文件夹路径
    output_folder = "/Users/cimorn/Documents/WebSite/IMSystem/images" # 替换为你的输出文件夹路径
    target_size = (800, 800)                 # 目标尺寸（宽, 高）

    # 运行批量处理
    batch_resize_images(input_folder, input_folder, target_size)