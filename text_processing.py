import re

# 清洗文本内容
def clean_content(content):
    content = re.sub(r'[^\u4e00-\u9fa5]', '', content)  # 只保留中文字符
    content = re.sub(r'\s+', ' ', content)             # 替换多余空格为一个空格
    return content
