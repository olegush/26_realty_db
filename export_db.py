import json
from db.database import db_session, init_db
from db.models import Ad

init_db()

with open('db/ads.json') as file:
    data = json.loads(file.read())

for ad in data:
    ad_to_db = Ad(**ad)
    db_session.add(ad_to_db)
    db_session.commit()
    print('Entry ', ad_to_db, ' added')

print('\n\nAll entries in database:\n', Ad.query.all())
