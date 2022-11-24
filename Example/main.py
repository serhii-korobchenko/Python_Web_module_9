import argparse
import sys

from database.db import session
from database.repository import get_todos, create_todo, remove_todo, update_todo, get_user_by_login

parser = argparse.ArgumentParser(description='TODO App')
parser.add_argument("--action", "-a", help="Command: create, update, list, remove", required=True)
parser.add_argument("--id")
parser.add_argument("--title")
parser.add_argument("--desc")
parser.add_argument("--login")

args = vars(parser.parse_args())

action = args.get("action")
title = args.get("title")
description = args.get("desc")
login = args.get("login")
id_ = args.get("id")


def main(user):
    match action:
        case 'create':
            create_todo(title, description, user)
        case 'list':
            todos = get_todos(user)
            if todos:
                for t in todos:
                    print(t.id, t.title, t.description, t.user.login)
        case 'update':
            todo = update_todo(id_, title, description, user)
            if todo:
                print(todo.id, todo.title, todo.description, todo.user.login)
                print('Successful!')
            else:
                print('Not Found')
        case 'remove':
            result = remove_todo(id_, user)
            print(f'Result: {bool(result)}')
        case _:
            print('Unknown command!')


if __name__ == '__main__':
    user = get_user_by_login(login)
    if user:
        password = input('Password: ')
        if password == user.password:
            main(user)

        else:
            print('Wrong password!')

    session.close()
