import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from file_operations import download_default_stopwords, load_stopwords, read_novel, write_results_to_file
from text_processing import clean_content
from word_frequency import count_words
from wordcloud_generator import generate_wordcloud
from gui import create_gui
import logging

logging.basicConfig(
    level=logging.DEBUG,  # 日志级别
    format='%(asctime)s - %(levelname)s - %(message)s',  # 格式
    filename='log.log',    # 输出到文件
    filemode='w'           # 覆盖写入
)
logging.info("程序启动")

# 默认停用词库文件名
DEFAULT_STOPWORDS_FILE = 'stopwords.txt'

# 主处理函数
def process_files(input_folder, output_folder, stopwords_file, pos_filter, output_format, generate_wordcloud, download_stopwords, progress):
    if download_stopwords:
        if not os.path.exists(stopwords_file):
            if not download_default_stopwords(stopwords_file):
                messagebox.showerror("错误", "下载停用词库失败，请检查网络连接或手动下载。")
                return
    stopwords = load_stopwords(stopwords_file)
    if not stopwords:
        messagebox.showerror("错误", "加载停用词库失败，请检查文件路径。")
        return

    novel_files = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith('.txt')]
    progress['maximum'] = len(novel_files)
    progress['value'] = 0

    for file_path in novel_files:
        content = read_novel(file_path)
        if not content:
            continue
        content = clean_content(content)
        word_counts = count_words(content, stopwords, pos_filter)
        base_name = os.path.basename(file_path)
        output_file = os.path.join(output_folder, base_name.replace('.txt', f'_word_counts.{output_format}'))
        write_results_to_file(word_counts.most_common(), output_file, output_format)
        if generate_wordcloud:
            wordcloud_file = os.path.join(output_folder, base_name.replace('.txt', '_wordcloud.png'))
            generate_wordcloud(word_counts, wordcloud_file)
        progress.step(1)
    messagebox.showinfo("完成", "所有文件处理完成！")

# 启动 GUI
if __name__ == "__main__":
    root = create_gui(process_files)
    root.mainloop()
