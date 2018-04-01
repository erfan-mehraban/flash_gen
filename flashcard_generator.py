from googletrans import Translator
from config import *

translator = Translator()
all_words = open(input_file_name).read().split()
ouput_file = open(ouput_file_name, 'w')
translated_words = translator.translate(all_words, dest=dest_lang, src=src_lang)
for word in translated_words:
    ouput_file.write(result_format.format_map({
        "src" : word.origin,
        "dest": word.text
    }))