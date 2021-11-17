#!/usr/bin/env python
import datetime as dt
import itertools
import os
from operator import itemgetter

import berserk


class Lichess:
    def __init__(self, api_token=None):
        if not api_token:
            raise ValueError('API token is required')
        self.client = berserk.Client(berserk.TokenSession(api_token))
        self.export_by_player = self.client.games.export_by_player  # Shortcut


def main():
    print(R"""
            __                            _       __    __
      _____/ /_  ___  __________   ____  (_)___ _/ /_  / /_
     / ___/ __ \/ _ \/ ___/ ___/  / __ \/ / __ `/ __ \/ __/
    / /__/ / / /  __(__  |__  )  / / / / / /_/ / / / / /_
    \___/_/ /_/\___/____/____/  /_/ /_/_/\__, /_/ /_/\__/
                                        /____/
    """)

    lichess = Lichess(os.environ.get('LICHESS_TOKEN'))

    users = {
        'Superfloss': 'Tony',
        'superross': 'Ross',
        'supermitch': 'Mitch',
        'jollyra': 'Nigel',
    }

    start = int(dt.datetime(2021, 11, 8).timestamp()) * 1000
    end = int(dt.datetime(2021, 11, 10).timestamp()) * 1000

    all_games = []
    for user_a, user_b in itertools.combinations(users.keys(), 2):
        print(f'Querying games between {user_a} and {user_b}')
        games = lichess.export_by_player(
            user_a,
            vs=user_b,
            since=start,
            until=end,
            rated='true',  # [sic] Bug in berserk
            # sort='dateAsc',  # Bug in berserk, doesn't exist yet
        )
        games = list(games)
        print(f'{len(games)} games')
        all_games.extend(games)

    print(f'Found {len(all_games)} total games')

    print('\nResults:\n========\n')

    for game in sorted(all_games, key=itemgetter('createdAt')):
        minutes = game['clock']['initial'] // 60
        increment = game['clock']['increment']
        clock = f'{minutes}+{increment}'

        white = game['players']['white']['user']['name']
        white = users[white]
        black = game['players']['black']['user']['name']
        black = users[black]

        if game['winner'] == 'white':
            winner = white
        else:
            winner = black
        # TODO: Draw

        # created = game['createdAt']
        print(f'{white} vs {black} ({clock}) - Winner: {winner}')

    print('\n\n')


if __name__ == '__main__':
    main()
