import os
from datetime import datetime
from urllib.parse import urlencode
import sqlite3
import logging

from dotenv import load_dotenv
from flask import Flask, render_template, request, send_from_directory, abort
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

ADS_PER_PAGE = 10
NEW_BUILDING_YEARS = 5


from models import Ad


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/', methods=['GET'])
def ads_list():
    ads = Ad.query.filter(Ad.active==True).order_by(Ad.id.desc())
    oblast_district = ''
    min_price = ''
    max_price = ''
    new_building = ''
    args = request.args.to_dict()

    try:
        current_page = int(args['current_page'])
    except (KeyError, ValueError) as  e:
        current_page = 1

    try:
        if args['oblast_district']:
            ads = ads.filter(Ad.oblast_district == args['oblast_district'])
            oblast_district = args['oblast_district']
    except KeyError as  e:
        pass

    try:
        if args['new_building']:
            ads = ads.filter(datetime.now().year - Ad.construction_year < NEW_BUILDING_YEARS)
            new_building = 'checked'
    except KeyError as  e:
        pass

    try:
        if int(args['min_price']):
            ads = ads.filter(Ad.price >= int(args['min_price']))
            min_price = args['min_price']
    except (KeyError, ValueError) as  e:
        pass

    try:
        if int(args['max_price']):
            ads = ads.filter(Ad.price <= args['max_price'])
            max_price = args['max_price']
    except (KeyError, ValueError) as  e:
        pass

    ads = ads.paginate(current_page, ADS_PER_PAGE, True)
    payload = urlencode(
                {'oblast_district': oblast_district,
                'new_building': new_building,
                'min_price': min_price,
                'max_price': max_price})
    return render_template(
                'index.html',
                ads=ads,
                oblast_district=oblast_district,
                new_building=new_building,
                min_price=min_price,
                max_price=max_price,
                params=payload)
