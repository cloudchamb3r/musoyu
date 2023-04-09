import requests
import json
import os

BASE_URI = 'http://ebook.cafe24app.com'

def write_json(filename, json_content):
    dirname = os.path.dirname(filename)
    os.makedirs(dirname, exist_ok=True)

    with open(filename, 'w', encoding='utf-8') as f: 
        f.write(json.dumps(json_content, ensure_ascii=False))

def main():
    book_list = json.loads(requests.get(f'{BASE_URI}/api/getBookList?use_at=Y').text)
    write_json("json/book_list.json",book_list)

    for book in book_list:
        book_seq = book["BOOK_SEQ"]
        book_name = book["BOOK_NM"]
        book_content = json.loads(requests.get(f'{BASE_URI}/api/getAllContList?id={book_seq}').text)
        write_json(f"json/book_{book_seq}_{book_name}.json", book_content)

if __name__ == '__main__':
    main()

