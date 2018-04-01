from googletrans import Translator
from config import *

translator = Translator()
all_words = open(input_file_name).read().split()
translated_words = translator.translate(all_words, dest=dest_lang, src=src_lang)
result = ""
for word in translated_words:
    result += result_format.format_map({
        "src" : word.origin,
        "dest": word.text
    })
ouput_file = open(ouput_file_name, 'w')
ouput_file.write(result[:-2])