import json
from app import db
from models import Ad

ads = Ad.query.filter_by().update({'active': False})
db.session.commit()

with open('db/ads.json') as file:
    new_ads = json.loads(file.read())

for new_ad in new_ads:
    new_ad_obj = Ad(**new_ad)
    db.session.merge(new_ad_obj)
db.session.commit()

print('{} new ads was exported with status "active". There are {} entries'
        ' totally in the database.'.format(len(new_ads), len(Ad.query.all())))
