import sqlalchemy

# import pandas


engine = sqlalchemy.create_engine('sqlite:///../test.db')
connection = engine.connect()
metadata = sqlalchemy.MetaData()


posts = sqlalchemy.Table('posts', metadata,
    sqlalchemy.Column('Id', sqlalchemy.Integer(), primary_key=True),
    sqlalchemy.Column('author', sqlalchemy.String(255), nullable=False),
    sqlalchemy.Column('content', sqlalchemy.TEXT),
    sqlalchemy.Column('time', sqlalchemy.Integer()),
    sqlalchemy.Column('bet', sqlalchemy.Integer()),
    sqlalchemy.Column('zahod', sqlalchemy.Integer())
    )

post = sqlalchemy.Table('posts', metadata, autoload=True, autoload_with=engine)


# metadata.create_all(engine)