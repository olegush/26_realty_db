from datetime import datetime
import shutil
import json
from app import db, DB_PATH
from models import Ad

try:
    db_postfix = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    db_backup = shutil.copyfile(DB_PATH, f'{DB_PATH}.backup_{db_postfix}')
    print(f'DB backup saved here: {db_backup}')
except Exception as e:
    print(f'Backup error: {e}')

try:
    ads = Ad.query.filter_by().update({'active': False})
    db.session.commit()
    with open('db/ads.json') as file:
        new_ads = json.loads(file.read())
    for new_ad in new_ads:
        new_ad_obj = Ad(**new_ad)
        merged = db.session.merge(new_ad_obj)
    commited = db.session.commit()
    print('{} new ads was exported with status "active". There are {} entries'
        ' totally in the database.'.format(len(new_ads), len(Ad.query.all())))
except Exception as e:
    print(f'Import error: {e}. Please restore you backup DB file and check your json file')
