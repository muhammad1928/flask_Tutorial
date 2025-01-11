from app import db

class Person(db.Model):
    # table name
    __tablename__ = 'people'
    # columns in the table with their data types and constraints
    pid = db.Column(db.Integer, primary_key=True)
    name_ = db.Column(db.Text(100), nullable=False) # name of the person with a max of 100 characters and cannot be null
    age = db.Column(db.Integer, nullable=False) # age of the person and cannot be
    job = db.Column(db.Text(100), nullable=False) # job of the person with a max of 100 characters and cannot be null

    def __repr__(self):
        return f"Person with name ('{self.name_}', '{self.age}', '{self.job}')"