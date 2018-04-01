# Auto Ronaldos flashcard generator

This app automatically translate words line by line and then write it in a new file wich can import by [Ronaldos flashcard app].(https://rolandos.net/en/flashcards.html)


## Runnig code
first change config file as you want and then install dependencies:
``` bash
pip3 install -r requirements.txt
```
then for running app:
```bash
python3 flashcard_generator.py
```

### Notes
This app using google translator ([googletrans python package](https://pypi.python.org/pypi/googletrans)) so you need **internet access**.

Also dont touch ```result_format``` in config file if you dont know how to program!

## License

All codes are released under the MIT license.
