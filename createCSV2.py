import gc
import os
import logging
import requests
import pandas as pd
import math
import csv
import numpy as np
import warnings
from requests.exceptions import HTTPError

warnings.filterwarnings('ignore')

# configure logger
logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a', format='%(levelname)s - %(message)s')
url = 'https://api.covid19india.org/states_daily.json'


states_dict = {}  # Dictionary for all the states as key and values set to empty list
states_list = []  # List of all the states
status_list = []  # Status type list
dates_list = []  # Dates as per provided in api
case_type = 'Confirmed'  # default case_type


def get_states_daily_data(source=url):
    try:
        response = requests.get(url)
        json_data = response.json()
        if json_data.get('states_daily', None) is not None:
            data = json_data['states_daily']
        # raise for status
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred {http_err}')
        logging.error(f'HTTP error occurred {http_err}')
    except Exception as err:
        print(f'Other error occurred {err}')
        logging.error(f'HTTP error occurred {err}')
    else:
        logging.debug(f'Get request completed successfully with code {response.status_code}')
        return data


def init_data_frame(states_daily_dict=None):

    # intialize data frame
    states_daily_df = pd.DataFrame(states_daily_dict)
    logging.debug(f'Set data frame from states_daily_dict ')
    # print(states_daily_dict)

    # set variables
    set_vars(states_daily_df=states_daily_df)
    return states_daily_df


def set_vars(states_daily_df=None):

    try:
        global status_list, dates_list

        if isinstance(states_daily_df, pd.DataFrame):
            set_states_var(states_daily_list=states_daily_df.columns.tolist())
            status_list = states_daily_df.status.unique().tolist()
            # status_list = unique_status.copy()
            logging.info(f'status_list set')
            #print(f'status_list {status_list}')

            dates_list = states_daily_df.date.unique().tolist()
            # dates_list = unique_dates.copy()
            logging.info(f'dates_list set')
            #print(f'dates_list {dates_list}')
    except TypeError as type_error:
        logging.error(f'Expecting data frame object {type_error}')


def set_states_var(states_daily_list=None):

    try:
        global states_list, states_dict
        if isinstance(states_daily_list, list):
            # remove date and status from list
            states_daily_list.remove('date')
            states_daily_list.remove('status')
            states_list = states_daily_list.copy()
            # print(f'state_list {states_list}')
            logging.debug(f'set states_list')

            for state in states_list:
                states_dict[state] = []
            logging.info(f'set state_dict')
            # print(f'state_dict {states_dict}')
    except TypeError as type_error:
        logging.error(f'Expecting list type data {type_error}')


def push_values_in_state_dict(daily_df=None, case_type=None):

    logging.debug(f'push values in states_key')
    try:
        if isinstance(daily_df, pd.DataFrame):
            if case_type is None:
                raise ValueError
            for date in dates_list:
                rslt_df = daily_df[(daily_df['date'] == date) & (daily_df['status'] == case_type)]
                rslt_df.drop(['date', 'status'], axis=1, inplace=True)
                insert_values_in_state_dict(rslt_df)
    except TypeError as type_err:
        logging.debug(f'Expecting pandas data frame')
    except ValueError as value_err:
        logging.debug(f'Expecting case_type')


def insert_values_in_state_dict(rslt_df=None):

    global states_dict
    try:
        if isinstance(rslt_df, pd.DataFrame):
            result_df = rslt_df.to_dict('records')[0]
            # print(f'result_df {result_df}')
            for key in states_dict:
                if result_df.get(key, None) is not None:
                    states_dict[key].append(result_df.get(key))
            # print(states_dict['mh'])
    except TypeError as type_err:
        logging.error(f'Expecting pd.Dataframe type')


def replace_states_dict_keys(states_dict=None):
    global case_type
    try:
        if states_dict is None:
            raise ValueError

        states_keys = ['ANDAMAN AND NICOBAR', 'ANDHRA PRADESH', 'ARUNACHAL PRADESH', 'ASSAM', 'BIHAR', 'CHANDIGARH',
                       'CHATTISGARH', 'DAMAN AND DEU', 'DELHI', 'DADRA AND NAGAR HAVELI', 'GOA', 'GUJRAT', 'HIMACHAL PRADESH',
                       'HARAYANA', 'JHARKHAND', 'JAMMU AND KASHMIR', 'KARNATAKA', 'KERALA', 'LADAKH', 'LAKSHADWEEP',
                       'MAHARASHTRA', 'MEGHALAYA', 'MANIPUR', 'MADHYA PRADESH', 'MIZORAM', 'NAGALAND', 'ORISSA', 'PUNJAB',
                       'PUDUCHERRY', 'RAJASTHAN', 'SIKKIM', 'TELENGANA', 'TAMILNADU', 'TRIPURA', 'INDIA', 'UNKNOWNS', 'UTTAR PRADESH', 'UTTARAKHAND',
                       'WEST BENGAL']
        if case_type == 'Confirmed':
            for i in range(len(states_keys)):
                states_keys[i] = states_keys[i].title()
        # changing keys of dictionary
        final_dict = dict(zip(states_keys, list(states_dict.values())))
        return final_dict
    except ValueError as value_err:
        logging.error(f'stated_dict cant be None {value_err}')


def download_daily_data():
    global states_dict
    states_daily_dict = get_states_daily_data(source=url)
    # print(states_daily_dict)

    # intialize data frame for further processing
    states_daily_df = init_data_frame(states_daily_dict=states_daily_dict)

    # append values in keys for states_dict
    push_values_in_state_dict(daily_df=states_daily_df, case_type=case_type)

    # replace states dict with keys
    states_dict = replace_states_dict_keys(states_dict)

    # convert dict into dataframe
    final_states_daily_df = pd.DataFrame.from_dict(states_dict, orient='index', columns=dates_list)

    # print(final_states_daily_df.head())
    file_name = case_type + '.csv'
    try:
        if os.path.exists('downloads') is False:
            os.makedirs('downloads')
        path = os.path.join('downloads', file_name)
        with open(path, "w") as file:
            final_states_daily_df.to_csv(file, index=True, header=True)
    except OSError as os_err:
        logging.error(f'Error creating directory {os_err}')
    finally:
        gc.collect()


def getCummulative():
    global case_type
    data = pd.read_csv("./downloads/{0}.csv".format(case_type))
    headers = list(data.columns)
    data = np.array(data)
    for i in range(len(data)):
        for j in range(1,len(data[i])):
            if math.isnan(data[i][j]):
                data[i][j] = 0
    for i in range(len(data)):
        for j in range(2,len(data[i])):
            data[i][j] = int(data[i][j] + data[i][j-1])

    data = list(data)
    p = data.pop(34)
    data.insert(0,p)
    p = np.array(headers)
    k = [p]
    k.extend(data)
    with open(f'./Datasets/{case_type}.csv', 'w+', newline ='') as file:     
        write = csv.writer(file) 
        write.writerows(k) 

def answer():
    download_daily_data()
    getCummulative()
    print('done')

