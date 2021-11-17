# chess_night

Running Chess Night results tabulation

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

`LICHESS_TOKEN=asdf123 ./chess_night.py`


