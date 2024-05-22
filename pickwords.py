import pandas
import random

class Pick_word:
    def __init__(self):
        self.file_path = "data/french_words.csv"
        self.data = pandas.read_csv(self.file_path)
        self.word_dict=self.data.set_index('French')['English'].to_dict()
        # self.word_dict = self.data.to_dict(orient="records")

    def pick_random_word(self):
        # 从 "English" 列中随机选择一个值
        # 从字典的键中随机选择一个
        self.word_fr = self.random_key =random.choice(list(self.word_dict.keys()))
        # 获取随机选择的键对应的值
        self.word_en = self.word_dict[self.random_key]
        # 返回法语单词和对应的英语单词
        return self.word_fr, self.word_en
        # return self.word_en


# 获取随机选择的单词并打印
# print(Pick_word().pick_random_word())
