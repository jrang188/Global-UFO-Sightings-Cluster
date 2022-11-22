import pandas as pd
import requests as rq

month_year_list = [202001, 202002, 202003, 202004, 202005, 202006, 202007,
                   202008, 202009, 202010, 202011, 202012, 202101, 202102,
                   202103, 202104, 202105, 202106, 202107, 202108, 202109,
                   202110, 202111, 202112, 202201, 202202, 202203, 202204,
                   202205, 202206, 202207, 202208, 202209, 202210]

PATH = 'https://nuforc.org/webreports/ndxe'


def get_ufo_data(month_year):
    '''
    This function takes a month and year as a string, and returns
    a csv file of the UFO data for that month and year

    Parameters
    ----------
    month_year : int
        the month and year of the data you want to get

    '''
    page = PATH + str(month_year) + '.html'
    page = rq.get(page)

    df = pd.read_html(page.text, parse_dates=True)[0]

    output_path = './ufo_data/'
    filename = output_path + str(month_year) + '.csv'
    print("Saving file: " + filename)
    df.to_csv(filename, index=False)


def main():
    """
    Main Function
    """
    for month_year in month_year_list:
        get_ufo_data(month_year)


if __name__ == '__main__':
    main()
