# -*- coding: utf-8 -*- 
import argparse

#テキストのランレングス圧縮を行う
def run_length2(text):
    
    #圧縮されたテキスト
    compression_text = ''
    
    #一つ前の文字
    before_word = ''
    
    #文字の長さ
    word_length = 0
    
    for i,word in enumerate(text):
    
        #最初の位置の一文字目に行う処理
        if i == 0:
            
            word_length = 1
            #一文字前の文字を格納
            before_word = word
            
        #直前の文字と一致しているかを比較
        elif before_word == word:
            
            #直前の文字と一致しているならカウントをアップする
            word_length += 1
            
        
        if before_word != word:
            
            #圧縮文字列に以前の文字とその数を足す
            compression_text += (before_word+str(word_length))
            
            #文字の長さと文字の更新
            word_length = 1
            before_word = word
        
    #圧縮された文字列を返す
    return compression_text
    
if __name__ == "__main__":
    
    # テキストを引数で取得する
    parser = argparse.ArgumentParser()
    parser.add_argument("text")
    args = parser.parse_args()
    
    #引数のテキストを与え、文字列を圧縮
    comp_text = run_length2(args.text)
    
    #圧縮された文字列を表示する
    print(comp_text)