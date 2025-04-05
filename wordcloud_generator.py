from wordcloud import WordCloud
import matplotlib.pyplot as plt
import logging

# 生成词云
def generate_wordcloud(word_counts, output_file):
    try:
        wordcloud = WordCloud(font_path='simhei.ttf', background_color='white').generate_from_frequencies(word_counts)
        plt.figure(figsize=(10, 8))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig(output_file)
        logging.info(f"词云已生成并保存到: {output_file}")
    except Exception as e:
        logging.error(f"生成词云失败: {output_file} - {e}")
