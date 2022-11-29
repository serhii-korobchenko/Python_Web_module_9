from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from models import Email, Record, Adress, Phone
from sqlalchemy import and_


engine = create_engine("sqlite:///cli_bot.db")
Session = sessionmaker(bind=engine)
session = Session()

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

email1 = session.query(Email).filter(Email.email_name == 'jchild2008@gmail.com')
email1.update({'email_name': 'super@gmail.com'})
session.commit()






