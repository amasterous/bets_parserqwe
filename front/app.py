import datetime
from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
import sys
sys.path.append('../parser')
from app_init import app, Post, db
# import db
# DEBUG = True


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
        time = time.strftime('%d-%B-%Y %H:%M:%S')

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
                'hltv_link': ins.hltv_link,
                'coef': ins.coef,
            }
        )
    return POSTS


# функциональный машрурт
@app.route('/')
def index():
    asd = 'nul'
    # posts = Post.query.all()
    # for post in posts:
    #     post.bet = 'null'
    #     post.type = 0
    #     post.game = 0
    #     post.zahod = 0
    #     post.hltv_link = 'null'
    #     post.coef = 'null'
    # db.session.commit()

    return jsonify({
        'status': 'success',
        'context': 'hello',
        'asd': asd,
    })



# возвращает только ставки
@app.route('/bets')
def all_bets():
    res = Post.query.filter_by(type=1, game=0).order_by(Post.time.desc()).all()
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
            post.zahod = 2
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
            post.type = 2
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


@app.route('/posts/bet/csgo/hltv', methods=['POST'])
def hltv_link():
    data = request.get_json()
    post = Post.query.filter_by(id=data.get('post_id')).first()
    if post:
        post.hltv_link = data.get('hltv_link')
        db.session.commit()
        result = "hltv link added"

    return jsonify({
        'status': 'success',
        'result': result,
    })


@app.route('/posts/bet/amount', methods=['POST'])
def bet_amount():
    data = request.get_json()
    post = Post.query.filter_by(id=data.get('post_id')).first()
    if post:
        post.bet = data.get('amount')
        db.session.commit()
        result = "bet amount added"

    return jsonify({
        'status': 'success',
        'result': result,
    })


@app.route('/posts/bet/coef', methods=['POST'])
def bet_coef():
    data = request.get_json()
    post = Post.query.filter_by(id=data.get('post_id')).first()
    if post:
        post.coef = data.get('coef')
        db.session.commit()
        result = "bet coef added"
    
    return jsonify({
        'status': 'success',
        'result': result,
    })


@app.route('/stats/main')
def stats_main():
    posts_count = db.session.query(Post).count()
    bets_count = Post.query.filter_by(type=1).count()

    winbets_count = Post.query.filter_by(zahod=1).count()
    losebets_count = Post.query.filter_by(zahod=2).count()
    winrate = winbets_count/(winbets_count+losebets_count)*100
    winrate = "%.2f" % (winrate)

    # schitau avg coeffficient
    cefscount = Post.query.filter(Post.coef!='null').count()
    allcefs = Post.query.filter(Post.coef!='null').all()
    coefssum = 0
    for a in allcefs:
        coefssum += float(a.coef)
    avgcoef = "%.2f" % (coefssum/cefscount)

    # schitau avg betamount
    betscount = Post.query.filter(Post.bet!='null').count()
    allbets = Post.query.filter(Post.bet!='null').all()
    betssum = 0
    for a in allbets:
        betssum += int(a.bet)
    avgbetamount = "%d" % (betssum/betscount)


    return jsonify({
        'posts_count': posts_count,
        'bets_count': bets_count,
        'winbets_count': winbets_count,
        'losebets_count': losebets_count,
        'avgcoef': avgcoef,
        'winrate': winrate, 
        'avgbetamount': avgbetamount,
    })


if __name__ == '__main__':
    app.run()

