import re

# 主要功能是对 Markdown 文件的内容进行特定替换操作。
#  \(` 和 `\) 替换成 $，将 \[` 和 `\] 替换成 $$，同时删除所有的 **
# 最后，把处理好的内容保存到指定的输出文件中

# 参数
# input_file：这是一个字符串类型的参数，代表要处理的 Markdown 文件的路径。
# output_file：同样为字符串类型的参数，它表示处理完成后，将保存处理结果的文件路径。
# 如果该文件不存在，脚本会创建它；若文件已存在，原内容会被新处理后的内容覆盖。

def replace(input_file, output_file):
    try:
        # 以只读模式打开输入的Markdown文件，并使用UTF-8编码读取其内容
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()

        # 使用正则表达式将文件内容中的 \( 替换为 $
        # 正则表达式中的 \\ 用于转义字符，确保匹配的是 \( 这个确切的字符串
        content = re.sub(r'\\\(', '$', content)
        # 使用正则表达式将文件内容中的 \) 替换为 $
        content = re.sub(r'\\\)', '$', content)

        # 使用正则表达式将文件内容中的 \[ 替换为 $$
        content = re.sub(r'\\\[', '$$', content)
        # 使用正则表达式将文件内容中的 \] 替换为 $$
        content = re.sub(r'\\\]', '$$', content)

        # 使用正则表达式将文件内容中的 ** 全部删除
        content = re.sub(r'\*\*', '', content)

        # 以写入模式打开输出文件，并使用UTF-8编码将处理后的内容写入该文件
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(content)
        # 打印处理完成的提示信息，告知用户结果保存的文件路径
        print(f"处理完成，结果已保存到 {output_file}")
    except FileNotFoundError:
        # 若输入文件未找到，打印相应的错误提示信息
        print(f"错误: 文件 {input_file} 未找到。")
    except Exception as e:
        # 若出现其他未知错误，打印错误信息
        print(f"发生未知错误: {e}")
    

if __name__=="__main__":
    # 定义要转换的markdown文件路径​
    md_file_path ="/Users/cimorn/Desktop/test.md"
    # 文本文件输出路径​
    output_file_path = "test.txt"

    # 调用md_toc_generator模块中的函数进行文件转换​

    replace(md_file_path, md_file_path)
    # mf.generator(md_file_path, output_file_path,6)