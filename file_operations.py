import os
import requests
import csv
import json
import logging

# 默认停用词库文件名
DEFAULT_STOPWORDS_FILE = 'stopwords.txt'

# 提供多个下载选项
DOWNLOAD_OPTIONS = [
    ("哈工大停用词库", "https://gitcode.com/Open-source-documentation-tutorial/b7917/raw/branch/master/stopwords/hit_stopwords.txt"),
    ("百度停用词库", "https://gitcode.com/open-source-toolkit/29de9/raw/branch/master/stopwords/baidu_stopwords.txt"),
    ("中文大全版停用词库", "https://gitcode.com/open-source-toolkit/ec473/raw/branch/master/stopwords/cn_all_stopwords.txt")
]

# 下载默认停用词库
def download_default_stopwords(stopwords_file):
    print("请选择停用词库下载来源：")
    for idx, (name, _) in enumerate(DOWNLOAD_OPTIONS, start=1):
        print(f"{idx}. {name}")

    choice = input("请输入选项编号（默认为1）：") or "1"
    choice = int(choice) - 1

    if 0 <= choice < len(DOWNLOAD_OPTIONS):
        url = DOWNLOAD_OPTIONS[choice][1]
        try:
            response = requests.get(url)
            response.raise_for_status()  # 确保请求成功
            with open(stopwords_file, 'w', encoding='utf-8') as f:
                f.write(response.text)
            logging.info(f"下载默认停用词库成功，保存为 {stopwords_file}")
            return True
        except requests.exceptions.RequestException as e:
            logging.error(f"下载停用词库失败: {e}")
            return False
    else:
        logging.error("无效的选项编号，下载失败。")
        return False

# 加载停用词库
def load_stopwords(stopwords_file):
    stopwords = set()
    try:
        with open(stopwords_file, 'r', encoding='utf-8') as f:
            for line in f:
                stopwords.add(line.strip())
        logging.info(f"加载停用词库成功: {stopwords_file}")
        return stopwords
    except FileNotFoundError:
        logging.error(f"停用词库文件未找到: {stopwords_file}")
        return None

# 读取小说内容
def read_novel(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        logging.info(f"读取文件成功: {file_path}")
        return content
    except Exception as e:
        logging.error(f"读取文件失败: {file_path} - {e}")
        return ""

# 将结果写入文件
def write_results_to_file(results, output_file, output_format='txt'):
    try:
        if output_format == 'txt':
            with open(output_file, 'w', encoding='utf-8') as file:
                for word, count in results:
                    file.write(f'{word}: {count}\n')
        elif output_format == 'csv':
            with open(output_file, 'w', encoding='utf-8', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Word', 'Count'])
                writer.writerows(results)
        elif output_format == 'json':
            with open(output_file, 'w', encoding='utf-8') as file:
                json.dump(dict(results), file, ensure_ascii=False, indent=4)
        logging.info(f"统计结果已写入文件: {output_file}")
    except Exception as e:
        logging.error(f"写入文件失败: {output_file} - {e}")
