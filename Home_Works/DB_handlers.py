from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from models import Email, Record, Adress, Phone
from sqlalchemy import and_
from sqlalchemy.schema import MetaData




def look_up_DB (text):
    engine = create_engine("sqlite:///cli_bot.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    #result = session.query(Record).options(joinedload(Record.phone)).all()
    result = session.query(Record).join(Phone)

    print(result)

    for person in result:
        print(person.name)





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





