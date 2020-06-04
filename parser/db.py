import sqlalchemy

# import pandas


engine = sqlalchemy.create_engine('sqlite:///../test.db')
connection = engine.connect()
metadata = sqlalchemy.MetaData()


posts = sqlalchemy.Table('post', metadata,
    sqlalchemy.Column('Id', sqlalchemy.Integer(), primary_key=True),
    sqlalchemy.Column('author', sqlalchemy.String(255), nullable=False),
    sqlalchemy.Column('content', sqlalchemy.TEXT),
    sqlalchemy.Column('time', sqlalchemy.Integer()),
    sqlalchemy.Column('bet', sqlalchemy.Integer()),
    sqlalchemy.Column('zahod', sqlalchemy.Integer()),
    sqlalchemy.Column('type', sqlalchemy.Integer()),
    sqlalchemy.Column('vk_link', sqlalchemy.TEXT()),
    sqlalchemy.Column('game', sqlalchemy.Integer()),
    sqlalchemy.Column('attachment_link', sqlalchemy.TEXT()),
    sqlalchemy.Column('hltv_link', sqlalchemy.TEXT()),
    sqlalchemy.Column('coef', sqlalchemy.TEXT()),
    )

post = sqlalchemy.Table('post', metadata, autoload=True, autoload_with=engine)


# metadata.create_all(engine)