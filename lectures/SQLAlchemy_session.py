from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///sqlalchemy_example.db')
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

'''В качестве объекта, связующего состояние базы и описание базы, в Python
коде выступает Base, именно этот класс отвечает за "магию" синхронизации
таблиц в базе данных и их описания в Python классах Person и Address.'''

Base.metadata.create_all(engine)
Base.metadata.bind = engine

'''ORM подход более выразительный. Например, добавление новых записей
в таблицу — это просто создание новых объектов классов Person и Address:'''

new_person = Person(name="Bill")
session.add(new_person)

'''Обратите внимание, чтобы изменения вступили в силу, были записаны
в базу, обязательно надо выполнить commit.'''

session.commit()

new_address = Address(post_code='00000', person=new_person)
session.add(new_address)
session.commit()

'''Чтобы получить данные из базы, можно воспользоваться методом query:'''

for person in session.query(Person).all():
    print(person.name)


for item in session.query(Address).all():
    print(item.person.name, item.post_code)

