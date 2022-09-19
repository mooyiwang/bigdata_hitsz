import re

import jieba




if __name__ == '__main__':

    file_in = open('D:/Code/big_data/bigdata/hw1/essay/pure_text.txt', 'r', encoding='utf-8')
    file_out = open('D:/Code/big_data/bigdata/hw1/essay/text_tokenized.txt', 'w', encoding='utf-8')
    lines = file_in.readlines()
    i = 0
    for line in lines:
        i += 1
        segs = jieba.cut(line, cut_all=False)
        seg = ' '.join(segs)
        print(i)
        file_out.write(seg)


    file_in.close()
    file_out.close()



