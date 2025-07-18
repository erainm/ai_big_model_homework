# Created by erainm on 2025/7/19 00:00.
# @Author erainm
# @Project: ai_big_model_homework
# @Description: TODO: 单词统计
"""
As your report on White Pollution indicates, regulations on the use of plastic bags have not been implemented effectively in some areas.
I am writing this letter to express my concern over the abuse of plastic bags and make some suggestions.
"""
class WordCount(object):
    def __init__(self, sentence):
        self.sentence = sentence
        self.word_count = {}
    def count_words(self):
        words = self.sentence.split()
        for word in words:
            if word in self.word_count:
                self.word_count[word] += 1
            else:
                self.word_count[word] = 1
    def print_word_counts(self):
        for word, count in self.word_count.items():
            print(f"{word}: {count}")
if __name__ == '__main__':
    sentence = """
As your report on White Pollution indicates, regulations on the use of plastic bags have not been implemented effectively in some areas.
I am writing this letter to express my concern over the abuse of plastic bags and make some suggestions.
"""
    word_count = WordCount(sentence)
    word_count.count_words()
    word_count.print_word_counts()