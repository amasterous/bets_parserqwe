import db


query = db.sqlalchemy.select([db.post])

res = db.connection.execute(query).fetchall()



POSTS = []



for ins in res:
    POSTS.append(
        {
            'author': ins[1],
            'content': ins[2],
            'time': str(ins[3])
        }
    )
    # print('id: ' + str(ins[0]))
    # print('author: ' + ins[1])
    # print('content: ' + ins[2])
    # print('time: ' + str(ins[3]))


print(POSTS)