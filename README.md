# Chess Night

Running Chess Night results tabulation:

```
            __                            _       __    __
      _____/ /_  ___  __________   ____  (_)___ _/ /_  / /_
     / ___/ __ \/ _ \/ ___/ ___/  / __ \/ / __ `/ __ \/ __/
    / /__/ / / /  __(__  |__  )  / / / / / /_/ / / / / /_
    \___/_/ /_/\___/____/____/  /_/ /_/_/\__, /_/ /_/\__/
                                        /____/

Querying games between Superfloss and superross
4 games
Querying games between Superfloss and supermitch
1 games
Querying games between Superfloss and jollyra
0 games
Querying games between superross and supermitch
1 games
Querying games between superross and jollyra
0 games
Querying games between supermitch and jollyra
0 games
Found 6 total games

Results:
========

Tony vs Mitch (10+5) - Winner: Mitch
Ross vs Tony (10+5) - Winner: Tony
Mitch vs Ross (10+5) - Winner: Mitch
Tony vs Ross (5+3) - Winner: Tony
Ross vs Tony (3+5) - Winner: Ross
Ross vs Tony (3+1) - Winner: Tony
```

## Setup

First optionally install `pyenv`, or install Python directly.

```
pyenv install 3.9.5
git clone git@github.com:supermitch/chess_night.git
cd chess_night
pyenv local 3.9.5
python -m venv venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

## Authorization

1. Go to https://lichess.org/account/oauth/token
2. Click `+` or the link https://lichess.org/account/oauth/token/create
3. Add token description, e.g. `chess night api token`
4. Do not turn on any permission switches, no additional perms required!
5. Click `Submit`
6. Save your access token somewhere, e.g. 1Password

## Execution

Add your access token as an environment variable when running the script:

`LICHESS_TOKEN=<api token> ./chess_night.py`

## References

- Berserk docs: https://berserk.readthedocs.io/en/master/usage.html
- Berser GitHub: https://github.com/rhgrant10/berserk
- Lichess API docs: https://lichess.org/api

