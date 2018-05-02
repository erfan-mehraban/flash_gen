from googletrans import Translator
from config import *

translator = Translator()
all_words = open(input_file_name).read().split("\n")
result = ""
for index, word in enumerate(all_words):
    if word.isspace() or word == '':
        continue
    word = translator.translate(word, dest=dest_lang, src=src_lang)
    result += result_format.format_map({
        "src" : word.origin,
        "dest": word.text
    })
    print (index+1,"/",len(all_words))
ouput_file = open(ouput_file_name, 'w')
ouput_file.write(result[:-2])
