# novel-word-frequency
# 小说词频统计工具

一个基于 Python 的小说词频统计工具，支持中文分词、词频统计、词云生成等功能。

## 功能
- 支持中文分词和词频统计
- 支持自定义停用词库
- 支持多种输出格式（txt, csv, json）
- 支持生成词云
- 提供图形用户界面（GUI）

## 使用方法
### 1. **安装依赖库**：
   ```bash
   pip install -r requirements.txt
   ```



### 2. 运行程序：

```bash
   python main.py
   ```



### 3. 在 GUI 中设置参数：

• 输入文件夹：选择包含小说文件的文件夹

• 输出文件夹：选择保存结果的文件夹

• 停用词库文件：选择停用词库文件（如果需要自动下载，可以勾选“自动下载停用词库”）

• 词性过滤：输入需要过滤的词性（空格分隔）

• 输出格式：选择输出文件的格式（txt,csv,json）

• 生成词云：勾选以生成词云图像

• 自动下载停用词库：勾选以自动下载停用词库


### 4. 开始处理：

• 点击“开始处理”按钮，程序将处理所有小说文件，并将结果保存到指定的输出文件夹。

# 项目结构

• `main.py`：主程序入口

• `text_processing.py`：文本处理功能

• `word_frequency.py`：词频统计功能

• `file_operations.py`：文件操作功能

• `gui.py`：GUI 界面

• `wordcloud_generator.py`：词云生成

• `requirements.txt`：依赖库

• `README.md`：项目说明


依赖库

• jieba：用于中文分词

• requests：用于下载停用词库

• tqdm：用于显示进度条

• wordcloud：用于生成词云

• matplotlib：用于绘制词云图像


许可证
本项目采用 MIT 许可证。请参阅[LICENSE](LICENSE)文件获取详细信息。


联系方式
如果有任何问题或建议，请通过以下方式联系：

• 电子邮件：3592631534@qq.com
