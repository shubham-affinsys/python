
import sqlalchemy
from sqlalchemy import create_engine,text , Column, Integer, String, select
from sqlalchemy.orm import Session, declarative_base

Base = declarative_base()
db_url="postgresql://shubham:9504@localhost:5432/shubham"

class DibDB(Base):
    __tablename__ = "dibDb"

    user_id = Column(Integer,primary_key=True)
    name = Column(String)


def connn():
    # creating connection using engine
    try:
        engine = create_engine(db_url)
        # connection = engine.connect()
        # connection.close()

        with engine.connect() as conn:
            # create_table="CREATE TABLE dibDB (user_id int,user_query_count int)"
            # conn.execute(text(create_table))
            conn.execute(
                text("INSERT INTO dibDB (user_id,user_query_count) VALUES (:user_id,:user_query_count)"),
                [{"user_id":49421,"user_query_count":23},{"user_id":56789,"user_query_count":30}],
            )

            conn.commit()

            data = conn.execute(text("select user_id,user_query_count from dibDB"))
            data_dict = dict()
            for data_dict in data.mappings():
                user_id = data_dict["user_id"]
                user_query_count = data_dict["user_query_count"]
            print(data_dict)

        
        query = text("SELECT user_query_count FROM dibDB WHERE user_id= :user_id")
        with Session(engine) as session:
            data = session.execute(query,{"user_id":56789}).scalar()
            print("user queries:",data)
        query = text("UPDATE dibDB SET user_query_count=:user_query_count WHERE user_id=:user_id")
        values = [
                {
                    "user_id":49421,
                    "user_query_count":0
                },
                {   
                    "user_id":56789,
                    "user_query_count":0
                }
            ]
        # try:
        #     data = session.execute(query,values)
        #     session.commit()
        # except:
        #     session.rollback()
        #     raise
        # else:
        #     session.commit()

        with Session(engine) as session:
            with session.begin() :
                # all statements will be executed and at last commited if no exceptions
                session.execute(query,values)
                session.execute(query,values)
                session.execute(query,values)
                print("all queries executed")
            # session is closed outside session.begin  by calling session.close()



    except Exception as e:
        print("cannot connect to DB",e)

import pprint
def delete():
    try:
        engine = create_engine("postgresql://shubham:9504@localhost:5432/shubham")
        
        with Session(engine) as session:
            session.begin()
            print("data defore deletion:")
            query = text("SELECT * FROM dibDB ")
            result = session.execute(query)
            data  = result.all()
            pprint.pprint(data)

            query = text("DELETE  FROM dibDB WHERE user_id=:user_id")
            session.execute(query,{"user_id":56789})
            session.commit()

            print("data after deletion")
            query = text("SELECT * FROM dibDB ")
            result = session.execute(query)
            data  = result.all()
            pprint.pprint(data)

    except Exception as ex:
        print("Not able to connect",ex)


def insert():
    try:
        engine = create_engine(db_url)
        with Session(engine) as session:
            insert_query = text("INSERT INTO dibDB (user_id,user_name,user_rmn) VALUES (:user_id,:user_name,:user_rmn)")
            insert_values = [
                {
                    "user_id":123,
                    "user_name":"shubh",
                    "user_rmn":1234567890
                },
                {
                    "user_id":456,
                    "user_name":"abc",
                    "user_rmn":987654321
                }
            ]
            try:
                session.execute(insert_query,insert_values)
            except Exception as e:
                session.rollback()
                print("Error while inserting data",e)

    except Exception as ex:
        print("cabnnot connect to db ",ex)

def create_table():
    try:
        engine = create_engine(db_url)
        with Session(engine) as session:
            query = text("CREATE TABLE user (user_id INT,user_name VARCAHR(50), user_rmn BIGINT)")
            session.execute(query)
            session.commit()
            print("table created")

    except Exception as ex:
        print("error while connecting to db",ex)

create_table()