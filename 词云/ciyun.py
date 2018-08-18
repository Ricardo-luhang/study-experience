from wordcloud import WordCloud
import jieba
import numpy
import PIL.Image as Image
jieba.add_word('路明非')



file = open('tyc.txt', encoding='gbk')
my_file = file.read()
file.close()
f_my_file = my_file.split('\n')
stopwords = {}.fromkeys(f_my_file, 0)
def chinese_jieba(text):
    wordlist_jieba = jieba.cut(text, HMM=True)
    wl_space_split = " ".join(wordlist_jieba)
    return wl_space_split





with open("lz.txt",encoding="utf-8") as fp:
    text = fp.read()
    cn_text = chinese_jieba(text)
    mask_pic = numpy.array(Image.open("lah.jpg"))

    wordcloud = WordCloud(background_color="white", font_path="FZLTXIHK.TTF",max_words=100,stopwords=stopwords,mask=mask_pic).generate(cn_text)
    image = wordcloud.to_image()
    # image.show()
    wordcloud.to_file("pic.jpg")