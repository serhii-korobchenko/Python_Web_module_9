from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from models import Email, Record, Adress, Phone
from sqlalchemy import and_
from sqlalchemy.schema import MetaData
from sqlalchemy import or_




def look_up_DB (text):
    engine = create_engine("sqlite:///cli_bot.db")
    Session = sessionmaker(bind=engine)
    session = Session()


    """
    SELECT r.name, r.created, p.phone_name
    FROM records r
    LEFT JOIN phones p ON r.id = p.rec_id
    """
    result = session.query\
        (Record.name, Record.created, Phone.phone_name, Email.email_name) \
        .select_from(Record)\
        .join(Email) \
        .join(Adress) \
        .join(Phone).all()

    print (result)











"""
    Знайти 5 студентів з найбільшим середнім балом по всім предметам
    :return:
    """
# result = session.query
#     (Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
#     .select_from(Grade).\
#     join(Student).\
#     group_by(Student.id).\
#     order_by(desc('avg_grade')).\
#     imit(5).all()
# return result


# SELECT s.name_student, round (avg(g.grade), 2) AS avg_grade
# FROM grades g
# LEFT JOIN students s ON s.id = g.student_id
# GROUP BY s.id
# ORDER BY avg_grade DESC
# LIMIT 5;



def add_records_DB(name, phone):
    engine = create_engine("sqlite:///cli_bot.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    phone1 = Phone(phone_name=phone)
    rec1 = Record(name=name, phone=[phone1])
    session.add(rec1)
    session.commit()
    session.close()

def change_phone_DB(name, new_phone):
    engine = create_engine("sqlite:///cli_bot.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    phone1 = session.query(Phone).filter(Phone.rec_id == str(session.query(Record.id).filter(Record.name == name).first()[0]))
    phone1.update({'phone_name': new_phone})
    session.commit()
    session.close()

def add_phone_DB(name, phone):
    engine = create_engine("sqlite:///cli_bot.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    phone1 = Phone(phone_name=phone, rec_id=str(session.query(Record.id).filter(Record.name == name).first()[0]))
    session.add(phone1)
    session.commit()
    session.close()

def del_phone_DB(name, phone):
    engine = create_engine("sqlite:///cli_bot.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    phone1 = session.query(Phone).filter(and_(Phone.phone_name == phone, Phone.rec_id==str(session.query(Record.id).filter(Record.name == name).first()[0])))
    phone1.delete()
    session.commit()
    session.close()

def del_rec_DB(name):
    engine = create_engine("sqlite:///cli_bot.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    rec1 = session.query(Record).filter(Record.name == name)
    rec1.delete()
    session.commit()
    session.close()

def add_email_DB(name, email):
    engine = create_engine("sqlite:///cli_bot.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    email1 = Email(email_name=email, rec_id=str(session.query(Record.id).filter(Record.name == name).first()[0]))
    session.add(email1)
    session.commit()
    session.close()

def change_email_DB(name, new_email):
    engine = create_engine("sqlite:///cli_bot.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    email1 = session.query(Email).filter(Email.rec_id == str(session.query(Record.id).filter(Record.name == name).first()[0]))
    email1.update({'email_name': new_email})
    session.commit()
    session.close()

def add_adress_DB(name, adress):
    engine = create_engine("sqlite:///cli_bot.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    adress1 = Adress(adress_name=adress, rec_id=str(session.query(Record.id).filter(Record.name == name).first()[0]))
    session.add(adress1)
    session.commit()
    session.close()

def change_adress_DB(name, new_adress):
    engine = create_engine("sqlite:///cli_bot.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    adress1 = session.query(Adress).filter(Adress.rec_id == str(session.query(Record.id).filter(Record.name == name).first()[0]))
    adress1.update({'adress_name': new_adress})
    session.commit()
    session.close()


#add Serhii 0675261531
# email1 = Email(email_name='jchild2008@gmail.com')
# adress1 = Adress(adress_name='Kyiv. Zodchih st.')
# phone1 = Phone(phone_name='0675261532')

#TRACK_ACTIONS

# #1 STEP - Create 'Serhii" record and add phone - 0675261531
# phone1 = Phone(phone_name='0675261531')
# rec1 = Record(name="Serhii", phone=[phone1])
# session.add(rec1)
# session.commit()

# #2 STEP - Create 'Serhii" record and add phone - 0675261531
# phone1 = Phone(phone_name='0675261531')
# rec1 = Record(name="Andrii", phone=[phone1])
# session.add(rec1)
# session.commit()

# #3 STEP - add email and adress to Serhii
#
# email1 = Email(email_name='jchild2008@gmail.com', rec_id=str(session.query(Record.id).filter(Record.name == "Serhii").first()[0]))
# adress1 = Adress(adress_name='Kyiv. Zodchih st.', rec_id=str(session.query(Record.id).filter(Record.name == "Serhii").first()[0]))
# session.add(email1)
# session.add(adress1)
# session.commit()

# #4 STEP - add same email to Serhii
#
# email1 = Email(email_name='jchild2008@gmail.com', rec_id=str(session.query(Record.id).filter(Record.name == "Serhii").first()[0]))
# session.add(email1)
# session.commit()


# #5 STEP - delete same email from Serhii
# email1 = session.query(Email).filter(Email.email_name == 'jchild2008@gmail.com')
# email1.delete()
# session.commit()

# #6 STEP - add email to Serhii again
#
# email1 = Email(email_name='jchild2008@gmail.com', rec_id=str(session.query(Record.id).filter(Record.name == "Serhii").first()[0]))
# session.add(email1)
# session.commit()


#6 STEP - update email to Serhii

# email1 = session.query(Email).filter(Email.email_name == 'jchild2008@gmail.com')
# email1.update({'email_name': 'super@gmail.com'})
# session.commit()



if __name__ == '__main__':
    # add_records_DB('Andrii', '888888888')
    # change_phone_DB('Bumba', '111111111')
    # add_phone_DB('Bumba', '2222222222')
    # del_phone_DB('Bumba', '2222222222')
    # del_rec_DB('Andrii')
    # add_email_DB('Bumba', '1@1.1')
    # change_email_DB('Bumba', '2@2.2')
    # add_adress_DB('Bumba', 'Vinica')
    # change_adress_DB('Bumba', 'Lviv')
    look_up_DB ('Ser')





