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
    ads = db.session.query(Ad).filter(Ad.active == True)
    ads_ids = set([ad.id for ad in ads])
    with open('db/ads.json') as file:
        new_ads = json.loads(file.read())
    new_ads_ids = set((new_ad['id'] for new_ad in new_ads))
    ads_ids_to_deactivate = ads_ids.difference(new_ads_ids)
    ads = db.session.query(Ad).filter(Ad.id.in_(ads_ids_to_deactivate)).update({'active': False}, synchronize_session=False)
    db.session.commit()
    print(f'{len(ads_ids_to_deactivate)} ads were deactivated.')
    for new_ad in new_ads:
        db.session.merge(Ad(**new_ad))
    db.session.commit()
    print('{} new ads were upserted with status "active". \n'
            'There are {} entries totally in the database.'.format(len(new_ads), len(Ad.query.all())))
except Exception as e:
    print(f'Import error: {e}. Please restore you backup DB file and check your json file')
