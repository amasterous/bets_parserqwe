from flask import Flask, jsonify
from flask_cors import CORS
import sys
sys.path.append('../parser')
# import db
from app_init import app, Post, db
import datetime
DEBUG = True
app.config['DEBUG'] = True


CORS(app)
GAMES = [
    ['0', 'default'],
    ['1', 'dota'],
    ['2', 'csgo']
]


def makeposts(data):
    POSTS = []
    for ins in data:
        time = datetime.datetime.fromtimestamp(ins.time)
        time = time.strftime('%Y-%d-%m %H:%M:%S')
        
        POSTS.append(
            {
                'id': ins.id,
                'author': ins.author,
                'content': ins.content,
                'time': time,
                'bet': ins.bet,
                'zahod': ins.zahod,
                'type': ins.type,
                'vk_link': ins.vk_link,
                'attachment_link': ins.attachment_link,
                'game': ins.game,
            }
        )
    return POSTS


# функциональный машрурт
@app.route('/')
def index():
    # posts = Post.query.all()
    # for post in posts:
    #     post.game=0
    # db.session.commit()
    return jsonify({
        'status': 'success',
        'context': 'hello',
    })

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


# возвращает только ставки
@app.route('/bets')
def all_bets():
    res = Post.query.filter_by(type=1).order_by(Post.time.desc()).all()
    POSTS = makeposts(res)
    return jsonify({
        'status': 'success',
        'posts': POSTS,
    })

@app.route('/dota')
def all_dota():
    res = Post.query.filter_by(game=1).order_by(Post.time.desc()).all()
    POSTS = makeposts(res)
    return jsonify({
        'status': 'success',
        'posts': POSTS,
    })

@app.route('/csgo')
def all_csgo():
    res = Post.query.filter_by(game=2).order_by(Post.time.desc()).all()
    POSTS = makeposts(res)
    return jsonify({
        'status': 'success',
        'posts': POSTS,
    })

# возвращает все посты
@app.route('/trash')
def all_trash():
    res = Post.query.filter_by(type=0).order_by(Post.time.desc()).all()
    POSTS = makeposts(res)
    return jsonify({
        'status': 'success',
        'posts': POSTS,
    })


# машрут возвращает посты с типом post
@app.route('/posts', methods=['GET'])
def all_posts():
    res = Post.query.filter_by(type=2).order_by(Post.time.desc()).all()
    POSTS = makeposts(res)
    return jsonify({
        'status': 'success',
        'posts': POSTS,
    })


# маршрут чтобы поставить ставке тип win
@app.route('/posts/win/<post_id>', methods=['GET'])
def post_win(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post:
        if post.zahod == 0:
            post.zahod = 1
            result = 'updated! (from none to win)'
        elif post.zahod == 2:
            post.zahod = 1
            result = 'updated (from lose to win)'
        else:
            result = 'it was win bet already'
    else:
        result = 'no such post'

    db.session.commit()
    # posts = Post.query.all()
    # for post in posts:
    #     if post.zahod == 1:
    #         post.zahod = 0

    # db.session.commit()
    # for p in post:
    #     zahod = p.zahod
    return jsonify({
        'status': 'success',
        'result': result,
    })


# маршрут для того чтобы поставить ставке тип lose
@app.route('/posts/lose/<post_id>', methods=['GET'])
def post_lose(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post:
        if post.zahod == 0:
            post.zahod = 2
            result = 'updated! (from none to lose)'
        elif post.zahod == 1:
            post.zahod =2
            result = 'updated (from win to lose)'
        else:
            result = 'it was lose bet already'
    else:
        result = 'no such post'

    db.session.commit()
    # posts = Post.query.all()
    # for post in posts:
    #     if post.zahod == 1:
    #         post.zahod = 0

    # db.session.commit()
    # for p in post:
    #     zahod = p.zahod
    return jsonify({
        'status': 'success',
        'result': result,
    })


# маршрут для того чтобы поставить посту тип post 
@app.route('/posts/post/<post_id>', methods=['GET'])
def post_post(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post:
        if post.type == 0:
            post.type = 2
            result = 'updated! (from none to post)'
        elif post.type == 1:
            post.type =2
            result = 'updated (from bet to post)'
        else:
            result = 'it was post  already'
    else:
        result = 'no such post'

    db.session.commit()
    # posts = Post.query.all()
    # for post in posts:
    #     if post.zahod == 1:
    #         post.zahod = 0

    # db.session.commit()
    # for p in post:
    #     zahod = p.zahod
    return jsonify({
        'status': 'success',
        'result': result,
    })

# маршрут для того чтобы поставить посту тип bet
@app.route('/posts/bet/<post_id>', methods=['GET'])
def post_bet(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post:
        if post.type == 0:
            post.type = 1
            result = 'updated! (from none to bet)'
        elif post.type == 2:
            post.type = 1
            result = 'updated (from post to bet)'
        else:
            result = 'it was bet  already'
    else:
        result = 'no such post'

    db.session.commit()
    # posts = Post.query.all()
    # for post in posts:
    #     if post.zahod == 1:
    #         post.zahod = 0

    # db.session.commit()
    # for p in post:
    #     zahod = p.zahod
    return jsonify({
        'status': 'success',
        'result': result,
    })



@app.route('/posts/bet/dota/<post_id>', methods=['GET'])
def bet_dota(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post:
        if post.game == 0:
            post.game = 1
            result = 'updated (from none to dota)'
        elif post.game == 2:
            post.game = 1
            result = 'updated (from csgo to dota)'
        else:
            result = 'it was dota already'
    else:
        result = 'no such post'
    
    db.session.commit()

    return jsonify({
        'status': 'success', 
        'result': result,
    })


@app.route('/posts/bet/csgo/<post_id>', methods=['GET'])
def bet_csgo(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if post:
        if post.game == 0:
            post.game = 2
            result = 'updated (from none to csgo)'
        elif post.game == 1:
            post.game = 2
            result = 'updated (from dota to csgo)'
        else:
            result = 'it was csgo already'
    else:
        result = 'no such post'
    
    db.session.commit()

    return jsonify({
        'status': 'success', 
        'result': result,
    })










if __name__ == '__main__':
    app.run()

