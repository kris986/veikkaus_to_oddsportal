#!/usr/bin/env python3
import urllib
from time import sleep
# from xvfbwrapper import Xvfb

from selenium import webdriver
from external.veikkaus_base import VeikkausBase
from internal.oddsportal_base import OddsportalBase
# from build_xlsx import write_to_excel
from selenium.webdriver.chrome.options import Options

from post_to_xlsx import update_xlsl_file

veikkaus_base = VeikkausBase()
oddssportal_base = OddsportalBase()
# vdisplay = Xvfb()

# version for Linux
# def run_driver():
#     chrome_options = Options()
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-setuid-sandbox")
#     driver = webdriver.Chrome(chrome_options=chrome_options)
#     return driver


# version for Windows
def run_driver():
    # init driver with options if script will run on Win Corporate version or Pro
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-features=RendererCodeIntegrity')
    driver = webdriver.Chrome(options=options)

    # driver = webdriver.Chrome()
    return driver


def go_to_url(driver, page_url, pref_url=''):
    url = urllib.parse.urljoin(page_url, pref_url)
    print('Driver run')
    driver.get(url)
    sleep(2)
    return driver


if __name__ == "__main__":
    # vdisplay.start()
    veikkaus_url = 'https://www.veikkaus.fi/fi/pitkaveto?sportId=10&selectedLeagues=10-all'
    oddsportal_url = "https://www.oddsportal.com"
    # driver = run_driver()
    try:
    #     go_to_url(driver, veikkaus_url)
    #     print('Started collect data on veikkaus...')
    #     data_dict = veikkaus_base.collect_tennis_data(driver)
    #     print('Ended collect data on veikkaus')
    #     go_to_url(driver, oddsportal_url)
    #     print('Started collect data on oddsportal...')
    #     data_dict = oddssportal_base.collect_data_by_dict(driver, data_dict)
    #     print('Ended collect data on oddsportal')
        data_dict = {
            'E.Bouchard - C.Garcia': [{'veikkaus': {'odds_1': '---', 'odds_2': '1,45'}}, {'time': '99 Jan'},
                                      {'bet365': {'col_1': '2.50', 'odds_1': '2.50', 'col_2': '1.50', 'odds_2': '1.50'}},
                                      {'William Hill': {'col_1': '2.38', 'odds_1': '2.60', 'col_2': '1.57', 'odds_2': '1.50'}},
                                      {'1xBet': {'col_1': '2.58', 'odds_1': '2.69', 'col_2': '1.49', 'odds_2': '1.47'}},
                                      {'Pinnacle': {'col_1': '2.74', 'odds_1': '2.61', 'col_2': '1.52', 'odds_2': '1.55'}}],
            # 'Strycova - A.Riske': [{'veikkaus': {'odds_1': '2,25', 'odds_2': '1,58'}}, {'time': '08 Jan 2020, 02:00'},
            #                        {'bet365': {'col_1': '2.25', 'odds_1': '2.10', 'col_2': '1.57', 'odds_2': '1.66'}},
            #                        {'William Hill': {'col_1': '2.30', 'odds_1': '2.10', 'col_2': '1.62', 'odds_2': '1.73'}},
            #                        {'1xBet': {'col_1': '2.32', 'odds_1': '1.73', 'col_2': '1.59', 'odds_2': '2.12'}},
            #                        {'Pinnacle': {'col_1': '2.39', 'odds_1': '1.93', 'col_2': '1.65', 'odds_2': '1.95'}}],
            # 'S.Rogers - G.Muguruza': [{'veikkaus': {'odds_1': '2,75', 'odds_2': '1,40'}}, {'time': '08 Jan 2020, 04:00'},
            #                           {'bet365': {'col_1': '2.75', 'odds_1': '2.75', 'col_2': '1.40', 'odds_2': '1.40'}},
            #                           {'William Hill': {'col_1': '2.75', 'odds_1': '2.75', 'col_2': '1.44', 'odds_2': '1.44'}},
            #                           {'1xBet': {'col_1': '2.82', 'odds_1': '2.76', 'col_2': '1.42', 'odds_2': '1.43'}},
            #                           {'Pinnacle': {'col_1': '2.91', 'odds_1': '3.14', 'col_2': '1.47', 'odds_2': '1.41'}}],
            # 'D.Collins - Y.Putintseva': [{'veikkaus': {'odds_1': '1,98', 'odds_2': '1,75'}}, {'time': '08 Jan 2020, 03:30'},
            #                              {'bet365': {'col_1': '1.90', 'odds_1': '2.00', 'col_2': '1.80', 'odds_2': '1.72'}}, {
            #                                  'William Hill': {'col_1': '2.00', 'odds_1': '2.00', 'col_2': '1.80',
            #                                                   'odds_2': '1.80'}},
            #                              {'1xBet': {'col_1': '1.90', 'odds_1': '1.87', 'col_2': '1.83', 'odds_2': '1.95'}},
            #                              {'Pinnacle': {'col_1': '2.09', 'odds_1': '2.06', 'col_2': '1.83', 'odds_2': '1.83'}}],
            'Bautista-Agut - Soeda': [{'veikkaus': {'odds_1': '1,07', 'odds_2': '6,60'}}],
            'D.Thiem - H.Hurkacz': [{'veikkaus': {'odds_1': '1,60', 'odds_2': '2,20'}}, {'time': '08 Jan 2020, 01:50'},
                                    {'bet365': {'col_1': '1.57', 'odds_1': '1.50', 'col_2': '2.25', 'odds_2': '2.50'}},
                                    {'William Hill': {'col_1': '1.62', 'odds_1': '1.50', 'col_2': '2.30', 'odds_2': '2.60'}},
                                    {'1xBet': {'col_1': '1.71', 'odds_1': '1.57', 'col_2': '2.21', 'odds_2': '2.49'}},
                                    {'Pinnacle': {'col_1': '1.71', 'odds_1': '1.53', 'col_2': '2.25', 'odds_2': '2.64'}}],
            # 'S.Kenin - N.Osaka': [{'veikkaus': {'odds_1': '2,30', 'odds_2': '1,55'}}, {'time': '09 Jan 2020, 02:00'},
            #                       {'bet365': {'col_1': '2.37', 'odds_1': '2.62', 'col_2': '1.53', 'odds_2': '1.44'}},
            #                       {'William Hill': {'col_1': '2.30', 'odds_1': '2.75', 'col_2': '1.62', 'odds_2': '1.44'}},
            #                       {'1xBet': {'col_1': '2.35', 'odds_1': '2.38', 'col_2': '1.61', 'odds_2': '1.59'}},
            #                       {'Pinnacle': {'col_1': '2.37', 'odds_1': '2.63', 'col_2': '1.65', 'odds_2': '1.54'}}],
            # 'Bondarenko - Kr.Pliskova': [{'veikkaus': {'odds_1': '2,50', 'odds_2': '1,48'}}, {'time': '09 Jan 2020, 04:00'},
            #                              {'bet365': {'col_1': '2.62', 'odds_1': '2.75', 'col_2': '1.50', 'odds_2': '1.44'}}, {
            #                                  'William Hill': {'col_1': '2.50', 'odds_1': '2.50', 'col_2': '1.53',
            #                                                   'odds_2': '1.53'}},
            #                              {'1xBet': {'col_1': '2.56', 'odds_1': '2.31', 'col_2': '1.57', 'odds_2': '1.62'}},
            #                              {'Pinnacle': {'col_1': '2.65', 'odds_1': '2.60', 'col_2': '1.55', 'odds_2': '1.56'}}],
            # 'E.Rybakina - E.Mertens': [{'veikkaus': {'odds_1': '2,70', 'odds_2': '1,40'}}, {'time': '09 Jan 2020, 04:00'},
            #                            {'bet365': {'col_1': '2.75', 'odds_1': '3.20', 'col_2': '1.44', 'odds_2': '1.36'}},
            #                            {'William Hill': {'col_1': '2.75', 'odds_1': '3.10', 'col_2': '1.44', 'odds_2': '1.36'}},
            #                            {'1xBet': {'col_1': '2.83', 'odds_1': '3.17', 'col_2': '1.48', 'odds_2': '1.38'}},
            #                            {'Pinnacle': {'col_1': '2.86', 'odds_1': '3.21', 'col_2': '1.48', 'odds_2': '1.40'}}],
            # 'S.Wawrinka - A.Bedene': [{'veikkaus': {'odds_1': '1,29', 'odds_2': '3,30'}}, {'time': '09 Jan 2020, 09:00'},
            #                           {'bet365': {'col_1': '1.30', 'odds_1': '1.28', 'col_2': '3.50', 'odds_2': '3.75'}},
            #                           {'William Hill': {'col_1': '1.29', 'odds_1': '1.29', 'col_2': '3.60', 'odds_2': '3.60'}},
            #                           {'1xBet': {'col_1': '1.29', 'odds_1': '1.30', 'col_2': '3.56', 'odds_2': '3.70'}},
            #                           {'Pinnacle': {'col_1': '1.34', 'odds_1': '1.32', 'col_2': '3.63', 'odds_2': '3.78'}}],
            'C.Wozniacki - L.Davis': [{'veikkaus': {'odds_1': '1,34', 'odds_2': '3,00'}}, {'time': '09 Jan 2020, 00:00'},
                                      {'bet365': {'col_1': '1.36', 'odds_1': '1.44', 'col_2': '3.00', 'odds_2': '2.62'}},
                                      {'William Hill': {'col_1': '1.36', 'odds_1': '1.44', 'col_2': '3.10', 'odds_2': '2.75'}},
                                      {'1xBet': {'col_1': '1.41', 'odds_1': '1.47', 'col_2': '3.03', 'odds_2': '2.69'}},
                                      {'Pinnacle': {'col_1': '1.41', 'odds_1': '1.42', 'col_2': '3.14', 'odds_2': '3.06'}}],
            'ATP  Australian Open': [{'veikkaus': {'odds_1': ' - ', 'odds_2': ' - '}},
                                     {'Pinnacle': {'col_1': '1.71', 'odds_1': '1.53', 'col_2': '2.25', 'odds_2': '2.64'}}],
            'WTA  Australian Open': [{'veikkaus': {'odds_1': '100500', 'odds_2': ' - '}}, {'time': '09 Jan 2020, 00:00'}]}
        print('Creating excel file')
        update_xlsl_file(data_dict)
        print('Parsing is finished')
    except Exception as e:
        print(e)
    finally:
        # driver.close()
        # vdisplay.stop()
        quit()

# data_dict = {
#     'E.Bouchard - C.Garcia': [{'veikkaus': {'odds_1': '2,50', 'odds_2': '1,45'}}, {'time': '08 Jan 2020, 01:50'},
#                               {'bet365': {'col_1': '2.50', 'odds_1': '2.50', 'col_2': '1.50', 'odds_2': '1.50'}},
#                               {'William Hill': {'col_1': '2.38', 'odds_1': '2.60', 'col_2': '1.57', 'odds_2': '1.50'}},
#                               {'1xBet': {'col_1': '2.58', 'odds_1': '2.69', 'col_2': '1.49', 'odds_2': '1.47'}},
#                               {'Pinnacle': {'col_1': '2.74', 'odds_1': '2.61', 'col_2': '1.52', 'odds_2': '1.55'}}],
#     'Strycova - A.Riske': [{'veikkaus': {'odds_1': '2,25', 'odds_2': '1,58'}}, {'time': '08 Jan 2020, 02:00'},
#                            {'bet365': {'col_1': '2.25', 'odds_1': '2.10', 'col_2': '1.57', 'odds_2': '1.66'}},
#                            {'William Hill': {'col_1': '2.30', 'odds_1': '2.10', 'col_2': '1.62', 'odds_2': '1.73'}},
#                            {'1xBet': {'col_1': '2.32', 'odds_1': '1.73', 'col_2': '1.59', 'odds_2': '2.12'}},
#                            {'Pinnacle': {'col_1': '2.39', 'odds_1': '1.93', 'col_2': '1.65', 'odds_2': '1.95'}}],
#     'S.Rogers - G.Muguruza': [{'veikkaus': {'odds_1': '2,75', 'odds_2': '1,40'}}, {'time': '08 Jan 2020, 04:00'},
#                               {'bet365': {'col_1': '2.75', 'odds_1': '2.75', 'col_2': '1.40', 'odds_2': '1.40'}},
#                               {'William Hill': {'col_1': '2.75', 'odds_1': '2.75', 'col_2': '1.44', 'odds_2': '1.44'}},
#                               {'1xBet': {'col_1': '2.82', 'odds_1': '2.76', 'col_2': '1.42', 'odds_2': '1.43'}},
#                               {'Pinnacle': {'col_1': '2.91', 'odds_1': '3.14', 'col_2': '1.47', 'odds_2': '1.41'}}],
#     'D.Collins - Y.Putintseva': [{'veikkaus': {'odds_1': '1,98', 'odds_2': '1,75'}}, {'time': '08 Jan 2020, 03:30'},
#                                  {'bet365': {'col_1': '1.90', 'odds_1': '2.00', 'col_2': '1.80', 'odds_2': '1.72'}}, {
#                                      'William Hill': {'col_1': '2.00', 'odds_1': '2.00', 'col_2': '1.80',
#                                                       'odds_2': '1.80'}},
#                                  {'1xBet': {'col_1': '1.90', 'odds_1': '1.87', 'col_2': '1.83', 'odds_2': '1.95'}},
#                                  {'Pinnacle': {'col_1': '2.09', 'odds_1': '2.06', 'col_2': '1.83', 'odds_2': '1.83'}}],
#     'Bautista-Agut - Soeda': [{'veikkaus': {'odds_1': '1,07', 'odds_2': '6,60'}}],
#     'D.Thiem - H.Hurkacz': [{'veikkaus': {'odds_1': '1,60', 'odds_2': '2,20'}}, {'time': '08 Jan 2020, 01:50'},
#                             {'bet365': {'col_1': '1.57', 'odds_1': '1.50', 'col_2': '2.25', 'odds_2': '2.50'}},
#                             {'William Hill': {'col_1': '1.62', 'odds_1': '1.50', 'col_2': '2.30', 'odds_2': '2.60'}},
#                             {'1xBet': {'col_1': '1.71', 'odds_1': '1.57', 'col_2': '2.21', 'odds_2': '2.49'}},
#                             {'Pinnacle': {'col_1': '1.71', 'odds_1': '1.53', 'col_2': '2.25', 'odds_2': '2.64'}}],
#     'Djokovic - C.Garin': [{'veikkaus': {'odds_1': '1,01', 'odds_2': '10,50'}}],
#     'A.Blinkova - Z.Diyas': [{'veikkaus': {'odds_1': '1,75', 'odds_2': '1,98'}}, {'time': '08 Jan 2020, 04:00'},
#                              {'bet365': {'col_1': '1.80', 'odds_1': '1.57', 'col_2': '1.90', 'odds_2': '2.25'}},
#                              {'William Hill': {'col_1': '1.67', 'odds_1': '1.91', 'col_2': '2.20', 'odds_2': '1.91'}},
#                              {'1xBet': {'col_1': '1.74', 'odds_1': '1.64', 'col_2': '2.03', 'odds_2': '2.28'}},
#                              {'Pinnacle': {'col_1': '1.85', 'odds_1': '1.68', 'col_2': '2.06', 'odds_2': '2.30'}}],
#     'R.Nadal - Y.Nishioka': [{'veikkaus': {'odds_1': '1,02', 'odds_2': '9,60'}}, {'time': '08 Jan 2020, 04:30'},
#                              {'bet365': {'col_1': '1.01', 'odds_1': '1.01', 'col_2': '13.00', 'odds_2': '15.00'}},
#                              {'William Hill': {'col_1': '1.02', 'odds_1': '1.02', 'col_2': '17.00', 'odds_2': '17.00'}},
#                              {'1xBet': {'col_1': '1.01', 'odds_1': '1.01', 'col_2': '17.00', 'odds_2': '22.00'}},
#                              {'Pinnacle': {'col_1': '1.01', 'odds_1': '1.01', 'col_2': '23.06', 'odds_2': '22.42'}}],
#     'S.Stosur - M.Keys': [{'veikkaus': {'odds_1': '3,90', 'odds_2': '1,21'}}, {'time': '08 Jan 2020, 05:00'},
#                           {'bet365': {'col_1': '4.00', 'odds_1': '4.33', 'col_2': '1.22', 'odds_2': '1.20'}},
#                           {'William Hill': {'col_1': '4.00', 'odds_1': '4.00', 'col_2': '1.25', 'odds_2': '1.25'}},
#                           {'1xBet': {'col_1': '3.78', 'odds_1': '3.84', 'col_2': '1.26', 'odds_2': '1.27'}},
#                           {'Pinnacle': {'col_1': '4.33', 'odds_1': '4.43', 'col_2': '1.26', 'odds_2': '1.24'}}],
#     'S.Peng - E.Alexandrova': [{'veikkaus': {'odds_1': '2,55', 'odds_2': '1,45'}}, {'time': '08 Jan 2020, 05:30'},
#                                {'bet365': {'col_1': '2.62', 'odds_1': '2.62', 'col_2': '1.44', 'odds_2': '1.44'}},
#                                {'William Hill': {'col_1': '2.60', 'odds_1': '2.60', 'col_2': '1.50', 'odds_2': '1.50'}},
#                                {'1xBet': {'col_1': '2.69', 'odds_1': '3.07', 'col_2': '1.45', 'odds_2': '1.39'}},
#                                {'Pinnacle': {'col_1': '2.78', 'odds_1': '2.70', 'col_2': '1.51', 'odds_2': '1.52'}}],
#     'Wang Qiang - A.Sasnovich': [{'veikkaus': {'odds_1': '1,60', 'odds_2': '2,18'}}],
#     'M.Cilic - G.Pella': [{'veikkaus': {'odds_1': '1,50', 'odds_2': '2,40'}}, {'time': '08 Jan 2020, 07:30'},
#                           {'bet365': {'col_1': '1.53', 'odds_1': '1.30', 'col_2': '2.37', 'odds_2': '3.40'}},
#                           {'William Hill': {'col_1': '1.44', 'odds_1': '1.40', 'col_2': '2.75', 'odds_2': '2.90'}},
#                           {'1xBet': {'col_1': '1.59', 'odds_1': '1.47', 'col_2': '2.44', 'odds_2': '2.74'}},
#                           {'Pinnacle': {'col_1': '1.60', 'odds_1': '1.38', 'col_2': '2.49', 'odds_2': '3.26'}}],
#     'A.Anisimova - D.Kasatkina': [{'veikkaus': {'odds_1': '1,45', 'odds_2': '2,55'}}, {'time': '08 Jan 2020, 08:30'},
#                                   {'bet365': {'col_1': '1.40', 'odds_1': '1.40', 'col_2': '2.75', 'odds_2': '2.75'}}, {
#                                       'William Hill': {'col_1': '1.50', 'odds_1': '1.44', 'col_2': '2.60',
#                                                        'odds_2': '2.75'}},
#                                   {'1xBet': {'col_1': '1.45', 'odds_1': '1.46', 'col_2': '2.74', 'odds_2': '2.74'}},
#                                   {'Pinnacle': {'col_1': '1.54', 'odds_1': '1.49', 'col_2': '2.66', 'odds_2': '2.79'}}],
#     'B.Paire - L.Harris': [{'veikkaus': {'odds_1': '1,68', 'odds_2': '2,08'}}],
#     'B.Coric - D.Schwartzman': [{'veikkaus': {'odds_1': '2,08', 'odds_2': '1,68'}}, {'time': '08 Jan 2020, 09:00'},
#                                 {'bet365': {'col_1': '2.10', 'odds_1': '1.72', 'col_2': '1.66', 'odds_2': '2.00'}}, {
#                                     'William Hill': {'col_1': '2.10', 'odds_1': '1.80', 'col_2': '1.73',
#                                                      'odds_2': '2.00'}},
#                                 {'1xBet': {'col_1': '2.17', 'odds_1': '1.74', 'col_2': '1.73', 'odds_2': '2.10'}},
#                                 {'Pinnacle': {'col_1': '2.18', 'odds_1': '1.88', 'col_2': '1.74', 'odds_2': '2.00'}}],
#     'G.Monfils - K.Anderson': [{'veikkaus': {'odds_1': '1,90', 'odds_2': '1,80'}}, {'time': '08 Jan 2020, 10:00'},
#                                {'bet365': {'col_1': '1.90', 'odds_1': '1.90', 'col_2': '1.80', 'odds_2': '1.80'}},
#                                {'William Hill': {'col_1': '1.91', 'odds_1': '1.91', 'col_2': '1.91', 'odds_2': '1.91'}},
#                                {'1xBet': {'col_1': '1.99', 'odds_1': '1.83', 'col_2': '1.88', 'odds_2': '2.00'}},
#                                {'Pinnacle': {'col_1': '2.00', 'odds_1': '1.84', 'col_2': '1.87', 'odds_2': '2.04'}}],
#     'A.Metreveli - F.Roncadelli': [{'veikkaus': {'odds_1': '1,06', 'odds_2': '7,20'}}, {'time': '08 Jan 2020, 10:30'},
#                                    {'bet365': {'col_1': '1.07', 'odds_1': '1.14', 'col_2': '7.50', 'odds_2': '5.00'}}, {
#                                        'William Hill': {'col_1': '1.08', 'odds_1': '1.08', 'col_2': '7.50',
#                                                         'odds_2': '7.50'}},
#                                    {'1xBet': {'col_1': '1.06', 'odds_1': '1.31', 'col_2': '10.50', 'odds_2': '3.52'}}, {
#                                        'Pinnacle': {'col_1': '1.08', 'odds_1': '1.79', 'col_2': '9.42',
#                                                     'odds_2': '2.10'}}],
#     'N.Basilashvili - P.Cuevas': [{'veikkaus': {'odds_1': '1,38', 'odds_2': '2,80'}}, {'time': '08 Jan 2020, 12:00'},
#                                   {'bet365': {'col_1': '1.40', 'odds_1': '1.36', 'col_2': '2.75', 'odds_2': '3.00'}}, {
#                                       'William Hill': {'col_1': '1.44', 'odds_1': '1.40', 'col_2': '2.75',
#                                                        'odds_2': '2.90'}},
#                                   {'1xBet': {'col_1': '1.47', 'odds_1': '1.41', 'col_2': '2.78', 'odds_2': '2.88'}},
#                                   {'Pinnacle': {'col_1': '1.45', 'odds_1': '1.47', 'col_2': '2.88', 'odds_2': '2.83'}}],
#     'P.Niklas-Salm. - P.Vives Marcos': [{'veikkaus': {'odds_1': '1,37', 'odds_2': '2,85'}}],
#     'M.Kukushkin - A.Rublev': [{'veikkaus': {'odds_1': '3,55', 'odds_2': '1,25'}}, {'time': '08 Jan 2020, 13:30'},
#                                {'bet365': {'col_1': '3.75', 'odds_1': '3.75', 'col_2': '1.25', 'odds_2': '1.25'}},
#                                {'William Hill': {'col_1': '3.50', 'odds_1': '3.30', 'col_2': '1.30', 'odds_2': '1.33'}},
#                                {'1xBet': {'col_1': '3.74', 'odds_1': '3.70', 'col_2': '1.30', 'odds_2': '1.26'}},
#                                {'Pinnacle': {'col_1': '3.97', 'odds_1': '3.88', 'col_2': '1.29', 'odds_2': '1.30'}}],
#     'Skupski/Skupsk - Kontinen/Skugo': [{'veikkaus': {'odds_1': '1,95', 'odds_2': '1,75'}}],
#     'F.Verdasco - F.Krajinovic': [{'veikkaus': {'odds_1': '2,25', 'odds_2': '1,55'}}, {'time': '08 Jan 2020, 15:00'},
#                                   {'bet365': {'col_1': '2.25', 'odds_1': '1.90', 'col_2': '1.57', 'odds_2': '1.80'}}, {
#                                       'William Hill': {'col_1': '2.30', 'odds_1': '1.91', 'col_2': '1.62',
#                                                        'odds_2': '1.91'}},
#                                   {'1xBet': {'col_1': '2.32', 'odds_1': '1.90', 'col_2': '1.63', 'odds_2': '1.82'}},
#                                   {'Pinnacle': {'col_1': '2.40', 'odds_1': '2.09', 'col_2': '1.63', 'odds_2': '1.81'}}],
#     'M.Fucsovics - C.Ilkel': [{'veikkaus': {'odds_1': '1,16', 'odds_2': '4,60'}}, {'time': '08 Jan 2020, 15:00'},
#                               {'bet365': {'col_1': '1.16', 'odds_1': '1.14', 'col_2': '5.00', 'odds_2': '5.50'}},
#                               {'William Hill': {'col_1': '1.17', 'odds_1': '1.17', 'col_2': '5.00', 'odds_2': '5.00'}},
#                               {'1xBet': {'col_1': '1.18', 'odds_1': '1.14', 'col_2': '4.92', 'odds_2': '5.55'}},
#                               {'Pinnacle': {'col_1': '1.19', 'odds_1': '1.17', 'col_2': '5.39', 'odds_2': '5.65'}}],
#     'L.Djere - PH.Herbert': [{'veikkaus': {'odds_1': '3,00', 'odds_2': '1,34'}}],
#     'M.Kecmanovic - J-W.Tsonga': [{'veikkaus': {'odds_1': '2,65', 'odds_2': '1,43'}}, {'time': '08 Jan 2020, 16:30'},
#                                   {'bet365': {'col_1': '2.62', 'odds_1': '3.00', 'col_2': '1.44', 'odds_2': '1.36'}}, {
#                                       'William Hill': {'col_1': '2.60', 'odds_1': '2.75', 'col_2': '1.50',
#                                                        'odds_2': '1.44'}},
#                                   {'1xBet': {'col_1': '2.59', 'odds_1': '2.97', 'col_2': '1.53', 'odds_2': '1.38'}},
#                                   {'Pinnacle': {'col_1': '2.66', 'odds_1': '3.02', 'col_2': '1.53', 'odds_2': '1.43'}}],
#     'M.Raonic - C.Moutet': [{'veikkaus': {'odds_1': '1,28', 'odds_2': '3,35'}}, {'time': '08 Jan 2020, 18:00'},
#                             {'bet365': {'col_1': '1.28', 'odds_1': '1.28', 'col_2': '3.50', 'odds_2': '3.50'}},
#                             {'William Hill': {'col_1': '1.30', 'odds_1': '1.30', 'col_2': '3.50', 'odds_2': '3.50'}},
#                             {'1xBet': {'col_1': '1.33', 'odds_1': '1.29', 'col_2': '3.40', 'odds_2': '3.50'}},
#                             {'Pinnacle': {'col_1': '1.33', 'odds_1': '1.30', 'col_2': '3.59', 'odds_2': '3.82'}}],
#     'C.Gauff - L.Siegemund': [{'veikkaus': {'odds_1': '1,45', 'odds_2': '2,60'}}, {'time': '09 Jan 2020, 00:00'},
#                               {'bet365': {'col_1': '1.44', 'odds_1': '1.44', 'col_2': '2.62', 'odds_2': '2.62'}},
#                               {'William Hill': {'col_1': '1.53', 'odds_1': '1.44', 'col_2': '2.50', 'odds_2': '2.75'}},
#                               {'1xBet': {'col_1': '1.50', 'odds_1': '1.48', 'col_2': '2.65', 'odds_2': '2.69'}},
#                               {'Pinnacle': {'col_1': '1.51', 'odds_1': '1.53', 'col_2': '2.74', 'odds_2': '2.65'}}],
#     'J.Teichmann - J.Goerges': [{'veikkaus': {'odds_1': '3,20', 'odds_2': '1,30'}}, {'time': '09 Jan 2020, 00:00'},
#                                 {'bet365': {'col_1': '3.00', 'odds_1': '2.37', 'col_2': '1.36', 'odds_2': '1.53'}}, {
#                                     'William Hill': {'col_1': '3.30', 'odds_1': '2.90', 'col_2': '1.33',
#                                                      'odds_2': '1.40'}},
#                                 {'1xBet': {'col_1': '3.62', 'odds_1': '2.78', 'col_2': '1.30', 'odds_2': '1.44'}},
#                                 {'Pinnacle': {'col_1': '3.56', 'odds_1': '2.64', 'col_2': '1.34', 'odds_2': '1.54'}}],
#     'S.Williams - C.McHale': [{'veikkaus': {'odds_1': '1,10', 'odds_2': '5,80'}}, {'time': '09 Jan 2020, 00:00'},
#                               {'bet365': {'col_1': '1.11', 'odds_1': '1.12', 'col_2': '6.50', 'odds_2': '6.00'}},
#                               {'William Hill': {'col_1': '1.12', 'odds_1': '1.14', 'col_2': '6.00', 'odds_2': '5.50'}},
#                               {'1xBet': {'col_1': '1.10', 'odds_1': '1.11', 'col_2': '7.70', 'odds_2': '6.80'}},
#                               {'Pinnacle': {'col_1': '1.11', 'odds_1': '1.15', 'col_2': '7.78', 'odds_2': '6.13'}}],
#     'E.Ruusuvuori - T.Daniel': [{'veikkaus': {'odds_1': '1,33', 'odds_2': '2,90'}}, {'time': '09 Jan 2020, 01:00'},
#                                 {'bet365': {}}, {'William Hill': {'col_1': '1.44', 'odds_1': '1.44', 'col_2': '2.62',
#                                                                   'odds_2': '2.62'}},
#                                 {'1xBet': {'col_1': '1.45', 'odds_1': '1.51', 'col_2': '2.63', 'odds_2': '2.59'}},
#                                 {'Pinnacle': {'col_1': '1.39', 'odds_1': '1.50', 'col_2': '3.01', 'odds_2': '2.59'}}],
#     'A.Barty - J.Brady': [{'veikkaus': {'odds_1': '1,19', 'odds_2': '4,20'}}, {'time': '09 Jan 2020, 02:00'},
#                           {'bet365': {'col_1': '1.18', 'odds_1': '1.18', 'col_2': '4.50', 'odds_2': '4.50'}},
#                           {'William Hill': {'col_1': '1.20', 'odds_1': '1.20', 'col_2': '4.50', 'odds_2': '4.50'}},
#                           {'1xBet': {'col_1': '1.23', 'odds_1': '1.24', 'col_2': '4.42', 'odds_2': '4.14'}},
#                           {'Pinnacle': {'col_1': '1.22', 'odds_1': '1.23', 'col_2': '4.70', 'odds_2': '4.67'}}],
#     'A.Tomljanovic - Ka.Pliskova': [{'veikkaus': {'odds_1': '3,90', 'odds_2': '1,21'}}],
#     'K.Bertens - A.Kontaveit': [{'veikkaus': {'odds_1': '1,73', 'odds_2': '1,98'}}, {'time': '09 Jan 2020, 02:00'},
#                                 {'bet365': {'col_1': '1.66', 'odds_1': '1.66', 'col_2': '2.10', 'odds_2': '2.10'}}, {
#                                     'William Hill': {'col_1': '1.80', 'odds_1': '1.67', 'col_2': '2.00',
#                                                      'odds_2': '2.20'}},
#                                 {'1xBet': {'col_1': '1.83', 'odds_1': '1.62', 'col_2': '2.03', 'odds_2': '2.30'}},
#                                 {'Pinnacle': {'col_1': '1.86', 'odds_1': '1.76', 'col_2': '2.04', 'odds_2': '2.16'}}],
#     'L.Samsonova - P.Kvitova': [{'veikkaus': {'odds_1': '4,40', 'odds_2': '1,17'}}, {'time': '09 Jan 2020, 02:00'},
#                                 {'bet365': {'col_1': '5.00', 'odds_1': '5.00', 'col_2': '1.16', 'odds_2': '1.16'}}, {
#                                     'William Hill': {'col_1': '4.50', 'odds_1': '4.50', 'col_2': '1.20',
#                                                      'odds_2': '1.20'}},
#                                 {'1xBet': {'col_1': '4.84', 'odds_1': '4.92', 'col_2': '1.20', 'odds_2': '1.18'}},
#                                 {'Pinnacle': {'col_1': '4.94', 'odds_1': '5.00', 'col_2': '1.21', 'odds_2': '1.21'}}],
#     'S.Kenin - N.Osaka': [{'veikkaus': {'odds_1': '2,30', 'odds_2': '1,55'}}, {'time': '09 Jan 2020, 02:00'},
#                           {'bet365': {'col_1': '2.37', 'odds_1': '2.62', 'col_2': '1.53', 'odds_2': '1.44'}},
#                           {'William Hill': {'col_1': '2.30', 'odds_1': '2.75', 'col_2': '1.62', 'odds_2': '1.44'}},
#                           {'1xBet': {'col_1': '2.35', 'odds_1': '2.38', 'col_2': '1.61', 'odds_2': '1.59'}},
#                           {'Pinnacle': {'col_1': '2.37', 'odds_1': '2.63', 'col_2': '1.65', 'odds_2': '1.54'}}],
#     'Bondarenko - Kr.Pliskova': [{'veikkaus': {'odds_1': '2,50', 'odds_2': '1,48'}}, {'time': '09 Jan 2020, 04:00'},
#                                  {'bet365': {'col_1': '2.62', 'odds_1': '2.75', 'col_2': '1.50', 'odds_2': '1.44'}}, {
#                                      'William Hill': {'col_1': '2.50', 'odds_1': '2.50', 'col_2': '1.53',
#                                                       'odds_2': '1.53'}},
#                                  {'1xBet': {'col_1': '2.56', 'odds_1': '2.31', 'col_2': '1.57', 'odds_2': '1.62'}},
#                                  {'Pinnacle': {'col_1': '2.65', 'odds_1': '2.60', 'col_2': '1.55', 'odds_2': '1.56'}}],
#     'E.Rybakina - E.Mertens': [{'veikkaus': {'odds_1': '2,70', 'odds_2': '1,40'}}, {'time': '09 Jan 2020, 04:00'},
#                                {'bet365': {'col_1': '2.75', 'odds_1': '3.20', 'col_2': '1.44', 'odds_2': '1.36'}},
#                                {'William Hill': {'col_1': '2.75', 'odds_1': '3.10', 'col_2': '1.44', 'odds_2': '1.36'}},
#                                {'1xBet': {'col_1': '2.83', 'odds_1': '3.17', 'col_2': '1.48', 'odds_2': '1.38'}},
#                                {'Pinnacle': {'col_1': '2.86', 'odds_1': '3.21', 'col_2': '1.48', 'odds_2': '1.40'}}],
#     'S.Wawrinka - A.Bedene': [{'veikkaus': {'odds_1': '1,29', 'odds_2': '3,30'}}, {'time': '09 Jan 2020, 09:00'},
#                               {'bet365': {'col_1': '1.30', 'odds_1': '1.28', 'col_2': '3.50', 'odds_2': '3.75'}},
#                               {'William Hill': {'col_1': '1.29', 'odds_1': '1.29', 'col_2': '3.60', 'odds_2': '3.60'}},
#                               {'1xBet': {'col_1': '1.29', 'odds_1': '1.30', 'col_2': '3.56', 'odds_2': '3.70'}},
#                               {'Pinnacle': {'col_1': '1.34', 'odds_1': '1.32', 'col_2': '3.63', 'odds_2': '3.78'}}],
#     'C.Wozniacki - L.Davis': [{'veikkaus': {'odds_1': '1,34', 'odds_2': '3,00'}}, {'time': '09 Jan 2020, 00:00'},
#                               {'bet365': {'col_1': '1.36', 'odds_1': '1.44', 'col_2': '3.00', 'odds_2': '2.62'}},
#                               {'William Hill': {'col_1': '1.36', 'odds_1': '1.44', 'col_2': '3.10', 'odds_2': '2.75'}},
#                               {'1xBet': {'col_1': '1.41', 'odds_1': '1.47', 'col_2': '3.03', 'odds_2': '2.69'}},
#                               {'Pinnacle': {'col_1': '1.41', 'odds_1': '1.42', 'col_2': '3.14', 'odds_2': '3.06'}}],
#     'ATP  Australian Open': [{'veikkaus': {'odds_1': ' - ', 'odds_2': ' - '}}],
#     'WTA  Australian Open': [{'veikkaus': {'odds_1': ' - ', 'odds_2': ' - '}}]}

