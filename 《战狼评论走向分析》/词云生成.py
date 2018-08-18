from wordcloud import WordCloud
import jieba
import numpy
from PIL import Image
jieba.add_word('战狼2')


file = open('tyc.txt', encoding='gbk')
my_file = file.read()
file.close()
f_my_file = my_file.split('\n')
stopword = {}.fromkeys(f_my_file, 0)
def ayanise_txt(text):
    res = jieba.cut(text)
    word = ' '.join(res)
    return word


with open('demo.txt', encoding='utf-8') as f:
    text = f.read()
    res = ayanise_txt(text)
    backgroud_pic = numpy.array(Image.open('China.jpg'))

    my_word_cloud = WordCloud(background_color='white', font_path='FZLTXIHK.TTF', max_words=100, stopwords=stopword, mask=backgroud_pic).generate(res)
    image = my_word_cloud.to_image()
    image.show()
    my_word_cloud.to_file('pic.jpg')

