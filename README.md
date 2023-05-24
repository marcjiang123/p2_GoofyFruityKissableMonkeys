# p2 by GoofyFruityKissableMonkeys

## Roster:
Marc:
- PM
- APIs

Kevin:
- Front End (FEF, CSS, JS graphs)

Gordon:
- SQLite

Faiza:
- Flask

## Description:
Our website will compare the prices of avocados to the prices of stocks. It will be like a higher or lower game for the user to guess. One tab will have a “higher or lower” game with a random stock for each guess. On another tab, you can pick any stock (using API) and compare it to the price of avocados. The last tab will be a leaderboard of accounts with the highest high score.

Each user will have to create their own account to use the website. The account will track their high score

## Launch Code
1. Clone this repo using
```
git clone git@github.com:marcjiang123/p2_GoofyFruityKissableMonkeys.git
```
2. Navigate into the repo and create a virtual environment with
```
python3 -m venv <env_name>
```
3. Navigate into the venv folder with 
```
cd <env_name>
``` 
4. Activate the virtual environment with:
```
(Linux)
. bin/activate

(Windows Command Prompt)
Scripts\activate.bat
```
5. Install the requirements by running
```
pip install -r ../requirements.txt
```
6. Finally you can navigate to the app folder with "`cd ../app`" and run it with
```
python3 __init__.py
```
7. Open the given link in a browser and you are ready to go!

OR

GO TO [rocksareactuallysoft.live](http://rocksareactuallysoft.live)

## APIs

[Stock Symbol API](https://github.com/stuy-softdev/notes-and-code/blob/main/api_kb/411_on_stocksymbol.md)

## Data

### Description

1) Sales and prices of avocados from ~2015-2020. Includes many cities and statistics like total volume sold or total # of bags sold

### Source

[https://www.kaggle.com/datasets/timmate/avocado-prices-2020](https://www.kaggle.com/datasets/timmate/avocado-prices-2020)
