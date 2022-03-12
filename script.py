import time
import csv
import json


def benchmark(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        t = end - start
        print('Время выполнения:', t)
        return result

    return wrapper


@benchmark
def test_script():
    with open("files/users.json", "r") as users_json:
        users = json.load(users_json)
        users_list = []
        for user in users:
            users_list.append(
                {'name': user['name'], 'gender': user['gender'], 'age': user['age'], 'address': user['address']})

    with open('files/books.csv', newline='') as books_csv:
        reader = csv.DictReader(books_csv)
        books_list = []
        for books in reader:
            books_list.append(books)

    result = []
    for i in users_list:
        result.append(
            {
                "name": i['name'],
                "gender": i['gender'],
                "age": i['age'],
                "address": i['address'],
                "books": []
            }
        )

    readers_count = len(result)
    user_index = 0
    for j in books_list:
        result[user_index]['books'].append(
            {
                "title": j['Title'],
                "author": j['Author'],
                "pages": int(j['Pages']),
                "genre": j['Genre']
            }
        )
        user_index += 1
        if user_index >= readers_count:
            user_index = 0

    with open('files/result.json', 'w') as file:
        result_json = json.dumps(result, indent=4)
        file.write(result_json)
