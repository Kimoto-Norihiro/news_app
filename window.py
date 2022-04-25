import os
import time

def window(window_size, title_list, content_list):
    i = 0
    n = len(title_list)
    while True:
        if i==n:
            i = 0
        sentence = ' ' * window_size + title_list[i] + '     ' + content_list[i] + ' ' * window_size
        len_sentence = len(sentence)
        for j in range(len_sentence-window_size):
            print('[ News ]')
            print(sentence[j:j+window_size-1])
            time.sleep(0.1)
            os.system('clear')
        i += 1
        

title_list = ['title'+ str(i) for i in range(2)]
content_list = ['hello world python news' + str(i) for i in range(2)]

window(50, title_list, content_list)