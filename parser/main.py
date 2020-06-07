import vk_api
import config
import db
import time
import os
import app_init


vk_session = vk_api.VkApi(config.LOGIN, config.PASSWORD)
vk_session.auth()

vk = vk_session.get_api()


def parse_posts(public_id, author, count=50):
    content = []
    posts = vk.wall.get(
        owner_id=public_id,
        count=count,
    )
    for post in posts['items']:
        pin = 0
        # чтобы не показывать закрепленный пост
        if 'is_pinned' in post:
            pin = 1
            continue
        vk_link = 'https://vk.com/public%s?w=wall%s_%s' % (
            str(post['owner_id'])[1:], post['owner_id'], post['id'])
        attachment_link = ''
        if 'attachments' in post:
            qwe = post['attachments'][0]['photo']['sizes'][-1]

            attachment_link = qwe['url']
            # print(attachment_link)
        content.append(
            {
                'post_id': post['id'],
                'author': author,
                'text': post['text'],
                'date': post['date'],
                'pin': pin,
                'vk_link': vk_link,
                'attachment_link': attachment_link,
            }
        )

    return content


while True:
    os.system("cls")
    print('checking...')
    malish_posts = parse_posts(config.MALISH_ID, 'malish')
    norch_posts = parse_posts(config.NORCH_ID, 'norch')
    gagarin_posts = parse_posts(config.GAGARIN_ID, 'gagarin')

    posts = [malish_posts, norch_posts, gagarin_posts]
    print('got posts')

    # def db_insert(massiv):
    #     query = db.sqlalchemy.insert(db.posts)
    #     values_list = []
    #     for posts in massiv:
    #         for m in posts:
    #             isset_check = db.sqlalchemy.select([db.post]).where(
    #                 db.post.columns.time == m['date'])
    #             res = db.connection.execute(isset_check).fetchall()
    #             if not res:
    #                 values_list.append(
    #                     {
    #                         'author': m['author'],
    #                         'content': m['text'],
    #                         'time': m['date'],
    #                         'zahod': '0',
    #                         'type': '0',
    #                         'vk_link': m['vk_link'],
    #                         'attachment_link': m['attachment_link'],
    #                         'game': '0',
    #                         'hltv_link': 'null',
    #                         'bet': 'null',
    #                         'coef': 'null',
    #                     }
    #                 )




    #     # print(values_list)
    #     if values_list:
    #         result = db.connection.execute(query, values_list)
    #         print('added, waiting')
    #     else:
    #         print('no new posts, waiting')
    #     # for r in result:
    #     #     print(r)

    def test_db_insert(massiv):
        values_list = []
        for posts in massiv: 
            for m in posts:
                row = app_init.Post.query.filter_by(time=m['date']) .first()
                if not row:
                    Post1 = app_init.Post(
                        'author': m['author'],
                        'content': m['text'],
                        'time': m['date'],
                        'zahod': '0',
                        'type': '0',
                        'vk_link': m['vk_link'],
                        'attachment_link': m['attachment_link'],
                        'game': '0',
                        'hltv_link': 'null',
                        'bet': 'null',
                        'coef': 'null',
                    )
                    values_list.append(Post1)
                    values_list.append(Post2)
                    values_list.append(Post3)
                else:
                    print('next..')

        if values_list:
            app_init.db.session.add_all(values_list)
            app_init.db.session.commit()
            print('added, waiting')
        else:
            print('no new posts, waiting')
        # db_insert(posts)
        # time.sleep(180)


test_db_insert()
# print(malish_posts)

# tim = 1588263467

# firstpost = db.Post(author='norch', content='hi everyone!', time='2345')
# db.session.add(firstpost)
# db.session.commit()

# asd = db.session.query(db.Post).filter(db.Post.time=='123')
# qwe = asd.first()

# if qwe:
#     print('yes')
# else:
#     print('no')

# for instance in db.session.query(Post).filter(Post.time==tim):
#     if not instance:
#         print('no')
#         break
#     else:
#         print('yse')
#     print(instance.author + ': ' + instance.content)
