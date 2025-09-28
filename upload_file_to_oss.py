import os
import oss2
import time

# 需要下载oss2库
# pip install oss2


def aoss(bucket_name, subfolder, data_folder, flat):
    if flat == 0:
        mode = 'cover'
    else:
        mode = 'add'
    # 阿里云 OSS 配置信息
    access_key_id = 'LTAI5tSb27nBNCN37eoSRJHk'
    access_key_secret = '7OYnnFc7P6t6qaTWRlHtxxFkcpv3N2'
    # 修正 endpoint 配置
    endpoint = 'oss-cn-hongkong.aliyuncs.com'

    # 创建 OSS 客户端实例
    auth = oss2.Auth(access_key_id, access_key_secret)
    bucket = oss2.Bucket(auth, endpoint, bucket_name)

    def upload_folder(folder_path):
        if mode == 'cover':
            # 清空 bucket 里的所有文件
            for obj in oss2.ObjectIterator(bucket):
                bucket.delete_object(obj.key)
            print("已清空 bucket 中的所有文件。")

        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                # 计算文件在 OSS 中的目标路径
                oss_path = os.path.relpath(file_path, data_folder)
                # 添加子文件夹路径
                if subfolder:
                    oss_path = os.path.join(subfolder, oss_path)

                if mode == 'add' and bucket.object_exists(oss_path):
                    # 如果是 add 模式且文件已存在，先删除原文件
                    bucket.delete_object(oss_path)
                    print(f"已删除 OSS 中存在的文件: {oss_path}")

                try:
                    # 上传文件到 OSS
                    result = bucket.put_object_from_file(oss_path, file_path)
                    if result.status == 200:
                        print(f"文件 {file_path} 上传成功，OSS 路径: {oss_path}")
                    else:
                        print(f"文件 {file_path} 上传失败，状态码: {result.status}")
                except Exception as e:
                    print(f"文件 {file_path} 上传时出现错误: {e}")

    # 调用函数上传文件夹
    upload_folder(data_folder)


if __name__ == "__main__":
    bucket_name = "mcj-item"
    subfolder = ""
    data_folder = "/Users/cimorn/Documents/WebSite/IMSystem"
    flat = 0 # 0 表示覆盖模式，1 表示添加模式
    aoss(bucket_name, subfolder, data_folder, flat)
    