import nbformat
# 导入nbformat库，用于读取和处理Jupyter Notebook文件格式
# pip install nbformat
from nbconvert import MarkdownExporter
# 从nbconvert库中导入MarkdownExporter类，用于将Notebook对象转换为Markdown格式
# pip install nbconvert
import sys
# 导入sys模块，用于处理命令行参数

def convert(ipynb_file_path, output_file_path=None):
    """
    功能：
    把 Jupyter Notebook 文件转换为 Markdown 文件

    参数:
    ipynb_file_path (str): 输入的 ipynb 文件的路径。
    output_file_path (str): 输出的 markdown 文件的路径。

    """
    try:
        # 使用with语句打开指定路径的.ipynb文件，以只读模式（'r'）和utf-8编码读取
        with open(ipynb_file_path, 'r', encoding='utf-8') as f:
            # 使用nbformat.read方法读取文件内容，并指定格式版本为4，将结果存储为notebook对象
            notebook = nbformat.read(f, as_version=4)
    except FileNotFoundError:
        print(f"错误：未找到指定的文件 {ipynb_file_path}。")
        return
    except Exception as e:
        print(f"读取文件时发生未知错误：{e}")
        return

    try:
        # 创建MarkdownExporter对象，用于执行转换操作
        exporter = MarkdownExporter()
        # 使用exporter的from_notebook_node方法将notebook对象转换为Markdown格式的文本
        # markdown变量存储转换后的Markdown文本，_表示忽略的第二个返回值（通常是资源字典，这里暂不使用）
        markdown, _ = exporter.from_notebook_node(notebook)
    except Exception as e:
        print(f"转换为Markdown格式时发生错误：{e}")
        return

    # 如果未指定输出文件路径
    if output_file_path is None:
        # 通过分割输入的.ipynb文件路径字符串，去掉扩展名部分，再加上.md扩展名，生成同名的Markdown文件路径
        output_file_path = ipynb_file_path.rsplit('.', 1)[0] + '.md'

    try:
        # 使用with语句打开生成的输出文件路径，以写入模式（'w'）和utf-8编码写入
        with open(output_file_path, 'w', encoding='utf-8') as f:
            # 将转换后的Markdown文本写入到输出文件中
            f.write(markdown)
        print(f"成功将 {ipynb_file_path} 转换为 {output_file_path}。")
    except Exception as e:
        print(f"写入文件时发生错误：{e}")

if __name__ == "__main__":
    # 检查命令行参数个数，如果参数个数小于2（即只输入了脚本名，未输入.ipynb文件路径）
    if len(sys.argv) < 2:
        # 打印使用说明，提示用户正确的命令行输入格式
        print("Usage: python script_name.py ipynb_file_path [output_file_path]")
        # 退出程序，返回状态码1表示异常退出
        sys.exit(1)
    # 获取命令行参数中的第一个参数，即要转换的.ipynb文件路径
    ipynb_file = sys.argv[1]
    # 如果命令行参数个数为3（即输入了脚本名、.ipynb文件路径和输出文件路径）
    if len(sys.argv) == 3:
        # 获取命令行参数中的第三个参数，即指定的输出Markdown文件路径
        output_file = sys.argv[2]
    else:
        # 否则，将输出文件路径设为None，后续会自动生成同名的Markdown文件路径
        output_file = None

    # 调用convert_ipynb_to_markdown函数，传入获取到的.ipynb文件路径和输出文件路径（可能为None），执行转换操作
    convert(ipynb_file, output_file)