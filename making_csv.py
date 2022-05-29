import time
import numpy as np
import pandas as pd
from requests import session
from shikimori_api import Shikimori
session = Shikimori()
api = session.get_api()
pd.set_option("display.max_rows", 999)
users = ['not_zoomqg', '!ja1z!ja1z!ja1z!ja1z', 'Modland', 'Teyllay', '-%7B']

for user_index in users:
    while True:
        try:
            print(f"Getting {user_index}'s data...")
            user_request = api.users(user_index).anime_rates.GET(status='completed', limit=5000)
            np_anilist = np.array([user_request[0]['anime']['russian'], user_request[0]['score']])
            for i in range(1, len(user_request)):
                np_anilist = np.append(np_anilist, [user_request[i]['anime']['russian'], user_request[i]['score']])
            np_anilist = np.rot90(np_anilist.reshape((len(user_request), 2)), 3)

            if user_index == '-%7B':
                username = 'qeortix'
            else:
                username = user_index

            anilist_series = pd.Series(np_anilist[1], index=np_anilist[0], name=username)
            anilist_series = anilist_series[~anilist_series.index.duplicated()]

            if users.index(user_index) == 0:
                anilist_df = pd.concat([anilist_series], axis=1)
            else:
                anilist_df = pd.concat([anilist_df, anilist_series], axis=1)
            print(f"Done with {username}'s anilist")
            time.sleep(1)
            break
        except:
            print('fuck...')
            time.sleep(5)
            continue

anilist_df.index.name = 'title'
print(anilist_df)

anilist_df.to_csv('anilist.csv', na_rep='NULL')