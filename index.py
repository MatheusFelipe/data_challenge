import pandas as pd
import re
from functools import reduce

def get_data(chart_file_path, ledger_file_path):
    chart_data_frame = pd.read_excel(chart_file_path)
    ledger_data_frame = pd.read_excel(ledger_file_path)

    return [chart_data_frame, ledger_data_frame]

def transform_data(chart_data_frame, ledger_data_frame):
    chart_dict = {}

    for index, row in chart_data_frame.iterrows():
        chart_dict[str(row.account)] = 0

    for index, row in ledger_data_frame.iterrows():
        chart_dict[str(row.account)] += float(row.value)

    chart_accounts = sorted(chart_dict.keys())
    accounts_column = []
    values_column = []

    for account in chart_accounts:
        if chart_dict[account] == 0:
            pattern = re.compile('{}\\..*'.format(account))
            child_keys = list(filter(lambda x: pattern.match(x), chart_accounts))
            chart_dict[account] = reduce((lambda acc, curr: acc + chart_dict[curr]), child_keys, 0)
        accounts_column.append(account)
        values_column.append(chart_dict[account])

    output = pd.DataFrame.from_dict({ 'account': accounts_column, 'value': values_column })
    output.to_excel('output.xlsx', index=False)

if __name__ == "__main__":
    [chart_data_frame, ledger_data_frame] = get_data('./input/chart_of_accounts.xlsx', './input/general_ledger.xlsx')
    transform_data(chart_data_frame, ledger_data_frame)
