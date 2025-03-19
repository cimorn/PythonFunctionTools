| T1 | T2 | T2 | T2 | T2 |
| --- | --- | --- | --- | --- |
| [1. ipynb_to_markdown.py](#1-ipynb_to_markdownpy) | [1.1. 功能](#11-功能) | [1.2. 依赖](#12-依赖) | [1.3. 使用](#13-使用)<br>  [1.3.1. 命令行](#131-命令行)<br>  [1.3.2. 程序写入](#132-程序写入) | [1.4. 错误处理](#14-错误处理) |
| [2. md_toc_generator.py](#2-md_toc_generatorpy) | [2.1. 功能](#21-功能) | [2.2. 依赖](#22-依赖) | [2.3. 使用](#23-使用)<br>  [2.3.1. 命令行](#231-命令行)<br>  [2.3.2. 程序写入](#232-程序写入) | [2.4. 错误处理](#24-错误处理) |
| [源码](#源码) |  |  |  |  |


# 1. ipynb_to_markdown.py

## 1.1. 功能

> 把 Jupyter Notebook（`.ipynb`）文件转换为 Markdown（`.md`）文件

> 借助 `nbformat` 库读取 `.ipynb` 文件，再利用 `nbconvert` 库中的 `MarkdownExporter` 类将其转换为 Markdown 格式，最后把转换后的内容写入到指定的文件中。


## 1.2. 依赖

- `nbformat`：用于读取和处理 Jupyter Notebook 文件格式

- `nbconvert`：用于把 Notebook 对象转换为 Markdown 格式

> 安装依赖

```bash
pip install nbformat nbconvert
```

## 1.3. 使用

### 1.3.1. 命令行

 `.ipynb` 文件路径和输出文件路径：把转换后的 Markdown 内容写入到指定的输出文件中

```bash
python script_name.py ipynb_file_path output_file_path
```

### 1.3.2. 程序写入

> 建立一个`main.py`并写入

```python
# 导入ipynb_to_markdown模块
import ipynb_to_markdown as itm
# 要转换的ipynb文件路径
ipynb_file_path = "test.ipynb"
# 输出的markdown文件路径（可选，若不指定，将自动生成同名文件）
output_file_path = "test.md"
# 调用模块中的convert_ipynb_to_markdown函数
itm.convert(ipynb_file_path, output_file_path)
```

## 1.4. 错误处理

在关键操作处添加了 `try-except` 语句，用于捕获可能出现的异常：

- 文件读取错误：如果指定的 `.ipynb` 文件不存在，会输出相应的错误信息。

- 格式转换错误：在将 Notebook 对象转换为 Markdown 格式时出现错误，会输出错误信息。

- 文件写入错误：在将转换后的 Markdown 文本写入文件时出现错误，会输出错误信息。


---


# 2. md_toc_generator.py

## 2.1. 功能

> 当用户输入Markdown文件路径、输出文件路径以及指定列数时，程序会根据列数的不同生成不同形式的目录
> 
> 若列数为0，程序将生成普通文本格式的目录，各级标题根据其级别进行相应的缩进展示
> 
> 若列数大于0，程序会生成表格形式的目录，表格的第一列展示一级标题，后续列展示二级标题，并且三级及以上标题会换行缩进显示在对应的二级标题单元格内
> 
> 程序还具备读取Markdown文件内容、过滤代码块中的标题、生成锚点链接等功能，最终将生成的目录保存到指定的输出文件中

## 2.2. 依赖

> 此程序依赖于Python的内置库，无需额外安装第三方库。主要使用了`with open`语句来处理文件的读取和写入操作

## 2.3. 使用

### 2.3.1. 命令行

`.md`文件路径以及输出文件路径，这样程序会把转换后的txt内容写入到指定的输出文件中。

```bash
python script_name.py md_file_path output_file_path
```

### 2.3.2. 程序写入

导入模块，然后调用`generator(md_file_path, output_file_path, column_num)`函数

```python
from your_module import generator
md_file_path = "your_md_file.md"
output_file_path = "output.txt"
column_num = 2
generator(md_file_path, output_file_path, column_num)
```

## 2.4. 错误处理

> 若指定的Markdown文件不存在，程序会捕获`FileNotFoundError`异常，并输出`错误: 文件 {md_file_path} 未找到。`的错误提示信息

> 若在程序执行过程中发生其他未知错误，程序会捕获`Exception`异常，并输出`发生未知错误: {e}`的错误提示



# 源码
::github{repo="cimorn/PythonFunctionTools"}

GitHub：[ItemManageSystem](https://github.com/cimorn/PythonFunctionTools)