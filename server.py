import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, render_template, request, send_from_directory
import sqlite3

from db.models import Ad


app = Flask(__name__)

ADS_PER_PAGE = 10
NEW_BUILDING_YEARS = 5


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


@app.route('/', methods=['GET'])
def ads_list():

    ads = Ad.query.filter(Ad.active==True).order_by(Ad.id.desc())

    oblast_district = ''
    min_price = ''
    max_price = ''
    new_building = ''
    page = 1

    if request.args:
        page = int(request.args['page'])
        args = request.args.to_dict()
        if 'oblast_district' in args and args['oblast_district'] != '':
            ads = ads.filter(Ad.oblast_district == args['oblast_district'])
            oblast_district = args['oblast_district']
        if 'new_building' in args and args['new_building'] != '':
            ads = ads.filter(datetime.now().year - Ad.construction_year < NEW_BUILDING_YEARS)
            new_building = 'checked'
        if 'min_price' in args and args['min_price'] != '':
            ads = ads.filter(Ad.price >= args['min_price'])
            min_price = args['min_price']
        if 'max_price' in args and args['max_price'] != '':
            ads = ads.filter(Ad.price <= args['max_price'])
            max_price = args['max_price']

    ads_count = ads.count()
    pages_count = ads_count // ADS_PER_PAGE + bool(ads_count % ADS_PER_PAGE)

    ads = ads.limit(ADS_PER_PAGE).offset(ADS_PER_PAGE * (page - 1))

    return render_template(
                'ads_list.html',
                ads=ads,
                page_current=page,
                pages_count=pages_count,
                ads_count=ads_count,
                oblast_district=oblast_district,
                new_building=new_building,
                min_price=min_price,
                max_price=max_price)


if __name__ == "__main__":
    load_dotenv()
    host = os.environ.get('HOST')
    port = int(os.environ.get('PORT', 5000))
    app.run(host=host, port=port)
