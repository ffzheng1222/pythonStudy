#!/usr/bin/python
# coding=utf-8


"""
参考文档：
    https://pypi.python.org/pypi/Flask-SQLAlchemy
    http://flask-sqlalchemy.pocoo.org/2.1/
    http://www.pythondoc.com/flask-sqlalchemy/config.html
    http://docs.sqlalchemy.org/en/latest/core/type_basics.html#generic-types
"""

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, flash, redirect, url_for, abort
from .forms import NewsForm
from datetime import datetime

app = Flask(__name__)
db = SQLAlchemy(app)


class News(db.Model):
    """ 新闻模型 """
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    img_url = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(2000), nullable=False)
    is_valid = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    news_type = db.Column(db.Enum('推荐', '百家', '本地', '图片'))

    # comments = db.relationship('Comments', backref='news',
    #                            lazy='dynamic')
    def __repr__(self):
        return '<News %r>' % self.title


@app.route('/')
def index():
    """ 新闻首页 """
    news_list = News.query.filter_by(is_valid=1)
    return render_template('index.html', news_list=news_list)


@app.route('/cat/<name>')
def cat(name):
    """ 新闻类别页面 """
    news_list = News.query.filter_by(is_valid=True, news_type=name)
    return render_template('cat.html', news_list=news_list)


@app.route('/detail/<int:pk>/')
def detail(pk):
    """ 新闻的详情 """
    new_obj = News.query.get(pk)
    return render_template('detail.html', new_obj=new_obj)


@app.route('/admin/')
@app.route('/admin/<int:page>/')
def admin(page=None):
    """ 新闻后台管理首页 """
    if not page:
        page = 1
    page_data = News.query.filter_by(is_valid=True).paginate(page, per_page=4)
    return render_template('/admin/index.html', page_data=page_data)


@app.route('/admin/add/', methods=['POST', 'GET'])
def add():
    """ 新增新闻 """
    form = NewsForm()
    if form.validate_on_submit():
        # 获取数据
        news_obj = News(
            title=form.title.data,
            content=form.content.data,
            img_url=form.img_url.data,
            news_type=form.news_type.data,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )
        # 保存数据
        db.session.add(news_obj)
        db.session.commit()
        # 用户提示新增成功
        flash('新增成功')
        # 跳转到首页
        return redirect(url_for('admin'))
    return render_template('/admin/add.html', form=form)


@app.route('/admin/update/<int:pk>/', methods=['POST', 'GET'])
def update(pk):
    """ 更新新闻 """
    news_obj = News.query.get(pk)
    if news_obj is None:
        abort(404)
    form = NewsForm(obj=news_obj)
    if form.validate_on_submit():
        # 获取数据
        news_obj.title = form.title.data
        news_obj.content = form.content.data
        news_obj.news_type = form.news_type.data
        news_obj.created_at = datetime.now()
        news_obj.updated_at = datetime.now()
        # 保存数据
        db.session.add(news_obj)
        db.session.commit()
        flash("修改成功")
        return redirect(url_for('admin'))
    return render_template('/admin/update.html', form=form)


@app.route('/admin/delete/<int:pk>', methods=['POST'])
def delete(pk):
    """ 删除新闻 """
    news_obj = News.query.get(pk)
    if not news_obj:
        return 'no'
    news_obj.is_valid = False
    db.session.add(news_obj)
    db.session.commit()
    return 'yes'


def flask_main():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/flask_news'
    app.config['SECRET_KEY'] = 'a random string'
    app.run(debug=True)


if __name__ == '__main__':
    flask_main()
