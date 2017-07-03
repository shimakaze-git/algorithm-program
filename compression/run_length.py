# -*- coding: utf-8 -*- 
import argparse

#テキストのランレングス圧縮を行う
def run_length(text):
    
    #圧縮されたテキスト
    compression_text = ''
    
    #一つ前の文字
    before_word = ''
    
    #文字の長さ
    word_length = 0
    
    for i,word in enumerate(text):
        
        #同じ文字が続くほど文字の長さのカウンターを回していく
        if ((0 < word_length) & (word_length < 9) & (before_word == word)):
            
            word_length += 1
            continue
        
        #文字の長さが0で無くなった場合に圧縮文字列に以前の文字と数を加える
        if(word_length != 0):
            compression_text += before_word
            compression_text += str(word_length)
        
        #以前の文字の変数に次の文字を加える
        before_word = word
        word_length = 1
    
    #ループの最後に一つ前の文字とその数を入れる
    if word_length != 0:
        compression_text += before_word
        compression_text += str(word_length)
        
    #圧縮された文字列を返す
    return compression_text
    
if __name__ == "__main__":
    
    # テキストを引数で取得する
    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    args = parser.parse_args()
    
    #引数のテキストを与え、文字列を圧縮
    comp_text = run_length(args.text)
    
    #圧縮された文字列を表示する
    print(comp_text)