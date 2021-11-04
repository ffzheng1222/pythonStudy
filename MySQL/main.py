#!/usr/bin/python
# coding=utf-8

from mysql.mysql_main import mysql_main
from flask_mysql_news import flask_news


def main():
    # mysql_main()
    flask_news.flask_main()


if __name__ == '__main__':
    main()
