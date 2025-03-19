def generator(md_file_path, output_file_path, column_num):
    """
    功能：
    该函数用于将 Markdown 文件中的标题提取出来，根据 column_num 的值生成不同格式的目录，
    并将目录保存到指定的输出文件中。

    参数:
    md_file_path (str): 输入的 Markdown 文件的路径。
    output_file_path (str): 输出的目录文件的路径。
    column_num (int): 表格的列数。当 column_num 为 0 时，生成普通文本目录；
                      当 column_num 大于 0 时，生成表格形式的目录。
    """
    try:
        # 以 UTF-8 编码打开指定路径的 Markdown 文件，并以只读模式读取其内容
        with open(md_file_path, 'r', encoding='utf-8') as file:
            content = file.readlines()

        # 用于存储所有标题信息的列表，每个元素是一个元组，包含标题级别和标题链接
        toc = []
        # 标记当前是否处于代码块中的布尔变量，初始为 False 表示不在代码块中
        in_code_block = False

        # 遍历 Markdown 文件的每一行内容
        for line in content:
            # 检查当前行是否以三个反引号开头，这是 Markdown 代码块的起始或结束标记
            if line.startswith('```'):
                # 切换代码块状态，如果之前不在代码块，现在进入；如果之前在代码块，现在退出
                in_code_block = not in_code_block
                # 跳过后续标题检查逻辑，直接处理下一行
                continue

            # 若当前不在代码块中，并且当前行以 '#' 开头，则认为是标题行
            if not in_code_block and line.startswith('#'):
                # 计算标题的级别，通过统计 '#' 的数量确定
                level = line.count('#')
                # 去除标题行开头的 '#' 符号以及前后的空白字符，得到纯标题文本
                title = line.lstrip('#').strip()
                # 生成用于锚点链接的标题，将标题中的空格替换为 '-'，并转换为小写，同时去除点号
                anchor = title.replace(' ', '-').replace('.', '').lower()
                # 生成包含标题级别和标题链接的元组，添加到 toc 列表中
                toc_item = (level, f"[{title}](#{anchor})")
                toc.append(toc_item)

        if column_num == 0:
            # 当 column_num 为 0 时，生成普通文本目录
            toc_plain = []
            for level, item in toc:
                # 根据标题级别添加相应数量的空格缩进
                toc_plain.append(" " * (level - 1) + item)
            # 将普通文本目录列表转换为字符串，每个标题占一行
            final_output = "\n".join(toc_plain)
        else:
            # 当 column_num 大于 0 时，生成表格形式的目录
            table = []
            current_row = []
            first_level_title = None
            current_second_level_index = 0

            for level, item in toc:
                if level == 1:
                    # 遇到一级标题时
                    if current_row:
                        # 若当前行已有内容，补齐列数
                        while len(current_row) < column_num:
                            current_row.append("")
                        # 将当前行添加到表格中
                        table.append(current_row)
                    # 开启新的一行，放入一级标题
                    current_row = [item]
                    # 记录当前一级标题
                    first_level_title = item
                    # 重置二级标题索引
                    current_second_level_index = 0
                elif level == 2:
                    # 遇到二级标题时
                    if len(current_row) >= column_num:
                        # 若当前行已满，补齐列数并保存当前行
                        while len(current_row) < column_num:
                            current_row.append("")
                        table.append(current_row)
                        # 开启新的一行，放入一级标题
                        current_row = [first_level_title]
                    # 将二级标题添加到当前行
                    current_row.append(item)
                    # 更新二级标题索引
                    current_second_level_index = len(current_row) - 1
                elif level > 2:
                    # 遇到三级及以上标题时
                    # 计算缩进量，根据标题级别减去 2 得到
                    indent = "  " * (level - 2)
                    # 如果当前行有对应的二级标题位置
                    if current_second_level_index < len(current_row):
                        # 将子标题添加到对应的二级标题后面，并添加换行符和缩进
                        current_row[current_second_level_index] += f"<br>{indent}{item}"

            if current_row:
                # 处理最后一行，补齐列数
                while len(current_row) < column_num:
                    current_row.append("")
                # 将最后一行添加到表格中
                table.append(current_row)

            # 生成表格的表头，包含一级标题和指定数量的二级标题列名
            table_md = "| " + " | ".join(["T1"] + [f"T2" for i in range(column_num - 1)]) + " |\n"
            # 生成表格的分隔线，用于区分表头和表格内容
        
            table_md += "| " + " | ".join(["---"] * column_num) + " |\n"
            for row in table:
                # 遍历表格的每一行，将其转换为 Markdown 表格的行格式，并添加到 table_md 中
                table_md += "| " + " | ".join(row) + " |\n"

            final_output = table_md

        # 以 UTF-8 编码打开指定的输出文件，并以写入模式将最终生成的目录内容写入
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(final_output)

        print(f"目录已成功生成并保存到 {output_file_path}")
    except FileNotFoundError:
        print(f"错误: 文件 {md_file_path} 未找到。")
    except Exception as e:
        print(f"发生未知错误: {e}")
    