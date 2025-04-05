import jieba
import jieba.posseg as pseg
from collections import Counter

# 使用 jieba 进行分词，并统计词频
def count_words(content, stopwords, pos_filter=None):
    words = pseg.cut(content)
    filtered_words = []
    for word, flag in words:
        if word not in stopwords and word.strip():
            if pos_filter is None or flag in pos_filter:
                filtered_words.append(word)
    word_counts = Counter(filtered_words)
    return word_counts
