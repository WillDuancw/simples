from pymyorm.database import Database
from pymyorm.transaction import Transaction as t
from config import db
from models.user import User


def update_user():
    try:
        t.begin()
        User.find().where(name='ping').update(money=0)
        t.rollback()
        # t.commit()
    except Exception as e:
        t.rollback()
        raise e


def create_user():
    fp = open('user.txt', 'r')
    try:
        User.find().truncate()
        t.begin()
        for line in fp:
            line = line.strip('\r\n')
            name, phone, money = line.split()
            model = User()
            model.name = name
            model.phone = phone
            model.money = money
            model.save()
        update_user()
        t.commit()
    except Exception as e:
        t.rollback()
        raise e
    fp.close()


if __name__ == '__main__':
    Database.connect(**db)
    try:
        t.begin()
        create_user()
        t.commit()
    except Exception as e:
        t.rollback()
        raise e
