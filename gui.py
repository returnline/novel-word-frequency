import tkinter as tk
from tkinter import filedialog, messagebox, ttk

# GUI 界面
def create_gui(process_files_func):
    root = tk.Tk()
    root.title("小说词频统计工具")

    # 输入文件夹
    tk.Label(root, text="输入文件夹:").grid(row=0, column=0, padx=10, pady=10)
    input_folder_var = tk.StringVar()
    tk.Entry(root, textvariable=input_folder_var, width=50).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(root, text="浏览", command=lambda: input_folder_var.set(filedialog.askdirectory())).grid(row=0, column=2, padx=10, pady=10)

    # 输出文件夹
    tk.Label(root, text="输出文件夹:").grid(row=1, column=0, padx=10, pady=10)
    output_folder_var = tk.StringVar()
    tk.Entry(root, textvariable=output_folder_var, width=50).grid(row=1, column=1, padx=10, pady=10)
    tk.Button(root, text="浏览", command=lambda: output_folder_var.set(filedialog.askdirectory())).grid(row=1, column=2, padx=10, pady=10)

    # 停用词库文件
    tk.Label(root, text="停用词库文件:").grid(row=2, column=0, padx=10, pady=10)
    stopwords_file_var = tk.StringVar(value="stopwords.txt")
    tk.Entry(root, textvariable=stopwords_file_var, width=50).grid(row=2, column=1, padx=10, pady=10)
    tk.Button(root, text="浏览", command=lambda: stopwords_file_var.set(filedialog.askopenfilename())).grid(row=2, column=2, padx=10, pady=10)

    # 词性过滤
    tk.Label(root, text="词性过滤 (空格分隔):").grid(row=3, column=0, padx=10, pady=10)
    pos_filter_var = tk.StringVar()
    tk.Entry(root, textvariable=pos_filter_var, width=50).grid(row=3, column=1, padx=10, pady=10)

    # 输出格式
    tk.Label(root, text="输出格式:").grid(row=4, column=0, padx=10, pady=10)
    output_format_var = tk.StringVar(value="txt")
    tk.OptionMenu(root, output_format_var, "txt", "csv", "json").grid(row=4, column=1, padx=10, pady=10)

    # 生成词云
    generate_wordcloud_var = tk.BooleanVar(value=True)
    tk.Checkbutton(root, text="生成词云", variable=generate_wordcloud_var).grid(row=5, column=1, padx=10, pady=10)

    # 自动下载停用词库
    download_stopwords_var = tk.BooleanVar(value=True)
    tk.Checkbutton(root, text="自动下载停用词库", variable=download_stopwords_var).grid(row=6, column=1, padx=10, pady=10)

    # 进度条
    progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
    progress.grid(row=7, column=0, columnspan=3, padx=10, pady=10)

    # 开始处理按钮
    tk.Button(root, text="开始处理", command=lambda: process_files_func(
        input_folder_var.get(),
        output_folder_var.get(),
        stopwords_file_var.get(),
        pos_filter_var.get().split() if pos_filter_var.get() else None,
        output_format_var.get(),
        generate_wordcloud_var.get(),
        download_stopwords_var.get(),
        progress
    )).grid(row=8, column=1, padx=10, pady=10)

    return root
