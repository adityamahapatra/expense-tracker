from contextlib import contextmanager

import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

import expense_tracker.src.constants as constants

Base = declarative_base()


class Expenses(Base):
    __tablename__ = "expenses"
    id = db.Column(
        db.Integer, nullable=False, autoincrement=True, primary_key=True
    )
    category = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=True)
    notes = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Expenses(category={self.category}, amount={self.amount}, " \
               f"date={self.date}, notes={self.notes})>"


engine = db.create_engine(constants.DATABASE, echo=False)
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)


@contextmanager
def connexion():
    session = Session()
    try:
        yield session
    except SQLAlchemyError as error:
        print(f"{error.__class__.__name__}: {error}")
        session.rollback()
        raise
    else:
        session.commit()
    finally:
        session.close()


def fetch_all_records():
    pass


def add_expense_entry(connection, table, category, amount, date, note):
    result = connection.execute(
        table.insert(),
        {
            "category": category,
            "amount": amount,
            "date": date,
            "notes": note if note else "",
        }
    )
    return result
