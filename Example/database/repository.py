from sqlalchemy import and_

from database.db import session
from database.models import User, Todo


def get_user_by_login(login):
    user = session.query(User).filter(User.login == login).first()
    return user


def create_todo(title, description, user):
    todo = Todo(title=title, description=description, user=user)
    session.add(todo)
    session.commit()


def get_todos(user):
    todos = session.query(Todo).filter(Todo.user == user).all()
    return todos


def update_todo(id_, title, description, user):
    todo = session.query(Todo).filter(and_(Todo.id == id_, Todo.user == user))
    todo.update({'title': title, 'description': description})
    session.commit()
    return todo.first()


def remove_todo(id_, user):
    todo = session.query(Todo).filter(and_(Todo.id == id_, Todo.user == user))
    todo.delete()
    session.commit()
    return todo
