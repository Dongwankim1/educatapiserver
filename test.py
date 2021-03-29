from jamo import h2j,j2hcj

def get_jongsung_TF(sample_text):
    sample_text_list = list(sample_text)
    last_word = sample_text_list[-1]
    last_word_jamo_list = list(j2hcj(h2j(last_word)))
    last_jamo=last_word_jamo_list[-1]

    jongsung_TF = "T"


    if last_jamo in ['ㅏ', 'ㅑ', 'ㅓ', 'ㅕ', 'ㅗ', 'ㅛ', 'ㅜ', 'ㅠ', 'ㅡ', 'ㅣ', 'ㅘ', 'ㅚ', 'ㅙ', 'ㅝ', 'ㅞ', 'ㅢ', 'ㅐ,ㅔ', 'ㅟ', 'ㅖ', 'ㅒ']: 
       jongsung_TF = "F" return jongsung_TF

with open("/tmp/mecab-ko-dic-2.1.1-20180720/user-dic",'r',encoding='utf-8') as f:
    file_data = f.readline()

world_list = ['콩쥐']





for word in word_list:

