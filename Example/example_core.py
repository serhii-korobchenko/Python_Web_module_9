from sqlalchemy import Table, Column, Integer, String, ForeignKey, select
from sqlalchemy import create_engine
from sqlalchemy import MetaData


engine = create_engine('sqlite:///:memory:', echo=False)

metadata = MetaData()


users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('fullname', String),
)

addresses = Table('addresses', metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer, ForeignKey('users.id')),
    Column('email_address', String, nullable=False)
)

metadata.create_all(engine)

if __name__ == '__main__':
    with engine.connect() as conn:
        print('Додаємо користувача')
        ins_user = users.insert().values(fullname='Andrii Bobanych')
        print(str(ins_user))
        result_user = conn.execute(ins_user)

        users_select = select(users)
        print(str(users_select))
        result = conn.execute(users_select)
        for row in result:
            print(row)

        print('Додаємо користувачу адрес')
        ins_address = addresses.insert().values(email_address='andr2000@gmail.com', user_id=result_user.lastrowid)
        print(str(ins_address))
        conn.execute(ins_address)

        address_select = select(addresses)
        result = conn.execute(address_select)
        for row in result:
            print(row)

        print('Знайти адрес з користувачем')
        address_select = select(addresses.c.email_address, users.c.fullname).join(users)
        print(address_select)
        result = conn.execute(address_select)
        for row in result:
            print(row)
            