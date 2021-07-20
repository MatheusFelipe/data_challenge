# Data Challenge
Data Processing Challenge

## Requirements

[Python 3+](https://www.python.org/downloads/)

## Challenge

Given a chart of accounts and a general ledger, returns a populated chart of accounts with the general ledger values

### Solution

The chart of accounts and general ledger on the input are parsed from .xlsx to a pandas DataFrame.

Then, we create a dictionary with keys being the accounts from the chart of accounts and values starting with zero.

First we read the keys from the chart and place them on the dictionary, and then we read the account and value pairs from the ledger, thus adding the value to the account in the dictionary.

After this step, we should have a dictionary with all leaves from the tree populated and the other nodes / keys are still zero.
So, we get and sort the accounts keys from the dictionary and, for each account X with zero value, we sum the values from the accounts X.\*, which should be the account's child accounts, and put the result in the account X.

The order of the accounts keys is important to avoid duplicate sum.

Finally, we take the accounts and values columns and generate an output, parsing the columns to a pandas DataFrame and then to .xlsx

### Install

```
pip install -r requirements.txt
```

### Run Solution

```
python index.py
```
