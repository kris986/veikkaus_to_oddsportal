#!/usr/bin/env python3
import logging
import urllib
from time import sleep
# from xvfbwrapper import Xvfb

from selenium import webdriver
from external.veikkaus_base import VeikkausBase
from internal.oddsportal_base import OddsportalBase
from selenium.webdriver.chrome.options import Options

from post_to_xlsx import update_xlsl_file, analyze_existing_matches

log = logging.getLogger(__name__)

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
    # options = webdriver.ChromeOptions()
    # options.add_argument('--disable-features=RendererCodeIntegrity')
    # driver = webdriver.Chrome(options=options)

    driver = webdriver.Chrome()
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
    driver = run_driver()
    try:
        go_to_url(driver, veikkaus_url)
        print('Started collect data on veikkaus...')
        data_dict = veikkaus_base.collect_tennis_data(driver)
        print('Ended collect data on veikkaus')
        go_to_url(driver, oddsportal_url)
        print('Started collect data on oddsportal...')
        data_dict = oddssportal_base.collect_data_by_dict(driver, data_dict)
        print('Ended collect data on oddsportal')
        print('Creating excel file')
        update_xlsl_file(data_dict)
        analyze_existing_matches(driver)
        print('Parsing is finished')
    except Exception as inst:
        log.exception('Это сообщение об ошибке:')
    finally:
        driver.close()
        # vdisplay.stop()
        quit()

# data_dict = {'D.Shapovalov - M.Fucsovics': [{'veikkaus': {'event_description': 'New: D.Shapovalov!!!!!!!!!!', 'odds_1': '1,16', 'odds_2': '4,60'}},
#             {'time': '21 Jan 2020, 01:00'},
#             {'bet365': {'col_1': '1.16', 'odds_1': '1.30', 'col_2': '5.00', 'odds_2': '3.50'}},
#             {'William Hill': {'col_1': '1.14', 'odds_1': '1.22', 'col_2': '5.50', 'odds_2': '4.00'}},
#             {'1xBet': {'col_1': '1.15', 'odds_1': '1.31', 'col_2': '5.45', 'odds_2': '3.46'}},
#             {'Pinnacle': {'col_1': '1.20', 'odds_1': '1.26', 'col_2': '5.30', 'odds_2': '4.23'}}],
#             'N.Osaka - M.Bouzkova': [{'veikkaus': {'event_description': 'new event_description',
#                                                    'odds_1': '1,15', 'odds_2': '4,80'}},
#                                      {'time': '22 Jan 2020, 01:00'}, {
#                                          'bet365': {'col_1': '10.12', 'odds_1': '1.14', 'col_2': '60.00',
#                                                     'odds_2': '5.50'}}, {
#                                          'William Hill': {'col_1': '1.12', 'odds_1': '1.11', 'col_2': '6.00',
#                                                           'odds_2': '6.00'}}, {
#                                          '1xBet': {'col_1': '1.13', 'odds_1': '1.14', 'col_2': '6.30',
#                                                    'odds_2': '5.45'}}, {
#                                          'Pinnacle': {'col_1': '1.16', 'odds_1': '1.15', 'col_2': '5.91',
#                                                       'odds_2': '6.13'}}], 'A.Barty - L.Tsurenko': [
#                 {'veikkaus': {'event_description': '101501', 'odds_1': '10,07', 'odds_2': '60,60'}},
#                 # {'time': '20 Jan 2020, 06:00'},
#                 {'bet365': {'col_1': '600', 'odds_1': '1.12', 'col_2': '69', 'odds_2': '6.00'}},
#                 {'William Hill': {'col_1': '1.08', 'odds_1': '1.11', 'col_2': '7.50', 'odds_2': '6.00'}},
#                 {'1xBet': {'col_1': '1.07', 'odds_1': '1.14', 'col_2': '9.10', 'odds_2': '5.35'}},
#                 {'Pinnacle': {'col_1': '1.09', 'odds_1': '1.14', 'col_2': '8.43', 'odds_2': '6.47'}}],
#             'ATP  Australian Open': [{'veikkaus': {'event_description': 'ATP Australian Avoimet',
#                                                    'odds_1': ' - ', 'odds_2': ' - '}}],
#             'Berrettini - A.Harris': [{'veikkaus': {'event_description': 'ATP Australian Avoimet',
#                                                     'odds_1': '1,11', 'odds_2': '5,60'}},
#                                       {'time': '20 Jan 2020, 01:00'}, {
#                                           'bet365': {'col_1': '1.10', 'odds_1': '1.08', 'col_2': '7.00',
#                                                      'odds_2': '8.00'}}, {
#                                           'William Hill': {'col_1': '1.08', 'odds_1': '1.07', 'col_2': '8.00',
#                                                            'odds_2': '7.50'}}, {
#                                           '1xBet': {'col_1': '1.11', 'odds_1': '1.08', 'col_2': '6.65',
#                                                     'odds_2': '8.40'}}, {
#                                           'Pinnacle': {'col_1': '1.14', 'odds_1': '1.08', 'col_2': '6.72',
#                                                        'odds_2': '9.82'}}]}


# data_dict = {'A.Barty - L.Tsurenko': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,07', 'odds_2': '6,60'}}], 'M.Cilic - C.Moutet': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,63', 'odds_2': '2,15'}}], 'H.Hurkacz - D.Novak': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,39', 'odds_2': '2,75'}}], 'K.Kanepi - B.Krejcikova': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,75', 'odds_2': '1,95'}}], 'M.Gasparyan - M.Sakkari': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '2,65', 'odds_2': '1,43'}}], 'S.Cirstea - Strycova': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '2,10', 'odds_2': '1,65'}}], 'F.Lopez - Bautista-Agut': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '4,80', 'odds_2': '1,14'}}], 'A.Potapova - S.Williams': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '8,80', 'odds_2': '1,03'}}], 'Li Ann - L.Cabrera': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,65', 'odds_2': '2,10'}}], 'J.Sinner - Purcell': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,30', 'odds_2': '3,20'}}], 'C.Garin - S.Travaglia': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,73', 'odds_2': '2,00'}}], 'K.Edmund - D.Lajovic': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,45', 'odds_2': '2,55'}}], 'R.Opelka - F.Fognini': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,73', 'odds_2': '2,00'}}], 'T.Sandgren - M.Trungelliti': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,48', 'odds_2': '2,50'}}], 'A.Riske - Yafan Wang': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,58', 'odds_2': '2,25'}}], 'K.Ahn - C.Wozniacki': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '3,85', 'odds_2': '1,22'}}], 'K.Siniakova - P.Kvitova': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '4,90', 'odds_2': '1,14'}}], 'M.Linette - A.Rus': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,45', 'odds_2': '2,55'}}], 'T.Zidansek - Han Na-Lae': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,53', 'odds_2': '2,35'}}], 'Q.Halys - F.Krajinovic': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '3,60', 'odds_2': '1,24'}}], 'J.Thompson - A.Bublik': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,98', 'odds_2': '1,75'}}], 'S.Johnson - Federer': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '9,60', 'odds_2': '1,02'}}], 'A.Davidovich - N.Gombos': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,68', 'odds_2': '2,08'}}], 'J.I.Londero - G.Dimitrov': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '4,10', 'odds_2': '1,19'}}], 'M.Polmans - M.Kukushkin': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '2,60', 'odds_2': '1,43'}}], 'M.Brengle - C.Garcia': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,98', 'odds_2': '1,73'}}], 'V.Williams - C.Gauff': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '2,35', 'odds_2': '1,53'}}], 'P.Andujar - M.Mmoh': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '2,30', 'odds_2': '1,55'}}], 'L.Mayer - T.Paul': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '3,30', 'odds_2': '1,29'}}], 'F.Ferro - A.Van Uytvanck': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '2,65', 'odds_2': '1,43'}}], 'M.Keys - D.Kasatkina': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,15', 'odds_2': '4,70'}}], 'Wang Qiang - P.Parmentier': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,13', 'odds_2': '5,10'}}], 'Kohlschreiber - M.Giron': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,32', 'odds_2': '3,10'}}], 'T.Ito - P.Gunneswaran': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '2,35', 'odds_2': '1,53'}}], 'B.Paire - C.Stebe': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,27', 'odds_2': '3,40'}}], 'D.Schwartzman - L.Harris': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,23', 'odds_2': '3,70'}}], 'J.Millman - U.Humbert': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,88', 'odds_2': '1,83'}}], 'A.Sasnovich - G.Minnen': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,63', 'odds_2': '2,15'}}], 'K.Juvan - D.Yastremska': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '4,00', 'odds_2': '1,20'}}], 'Konta - O.Jabeur': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,58', 'odds_2': '2,25'}}], 'N.Hibino - S.Peng': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '2,40', 'odds_2': '1,50'}}], 'S.Stosur - C.McNally': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '2,80', 'odds_2': '1,39'}}], 'P.Hercog - R.Peterson': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '2,25', 'odds_2': '1,58'}}], 'B.Pera - E.Rybakina': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '2,30', 'odds_2': '1,55'}}], 'S.Tsitsipas - S.Caruso': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,01', 'odds_2': '11,00'}}], 'J-L.Struff - Djokovic': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': ' - ', 'odds_2': ' - '}}], 'S.Stephens - Shuai Zhang': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '2,25', 'odds_2': '1,58'}}], 'P.Niklas-Salm. - L.Vanni': [{'veikkaus': {'event_description': 'Rennes, Ranska, Miehet', 'odds_1': '3,05', 'odds_2': '1,31'}}], 'A.Bolt - A.Ramos': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '2,40', 'odds_2': '1,50'}}], 'A.Mannarino - D.Thiem': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '6,00', 'odds_2': '1,09'}}], 'A.Popyrin - J-W.Tsonga': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '2,50', 'odds_2': '1,48'}}], 'A.Tabilo - D.Galan': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '2,45', 'odds_2': '1,48'}}], 'C.Eubanks - P.Gojowczyk': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '2,45', 'odds_2': '1,48'}}], "C.O'Connell - A.Rublev": [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '7,80', 'odds_2': '1,05'}}], 'Ca.Ruud - E.Gerasimov': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,32', 'odds_2': '3,10'}}], 'D.Dzumhur - S.Wawrinka': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '5,20', 'odds_2': '1,12'}}], 'D.Goffin - J.Chardy': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,20', 'odds_2': '4,00'}}], 'D.Koepfer - Martinez Porte': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,37', 'odds_2': '2,85'}}], 'D.Medvedev - F.Tiafoe': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,05', 'odds_2': '8,00'}}], 'E.Gulbis - F.Auger-Aliass': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '4,10', 'odds_2': '1,20'}}], 'F.Delbonis - J.Sousa': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,80', 'odds_2': '1,90'}}], 'F.Verdasco - E.Donskoy': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,22', 'odds_2': '3,80'}}], 'G.Monfils - Y-H.Lu': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,01', 'odds_2': '11,50'}}], 'H.Gaston - J.A.Munar': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '3,30', 'odds_2': '1,28'}}], 'I.Ivashka - K.Anderson': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '4,60', 'odds_2': '1,16'}}], 'I.Karlovic - V.Pospisil': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '4,00', 'odds_2': '1,20'}}], 'J.Duckworth - A.Bedene': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '2,35', 'odds_2': '1,53'}}], 'J.Isner - T.Monteiro': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,29', 'odds_2': '3,25'}}], 'J.Kovalik - Carreno Busta': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '5,30', 'odds_2': '1,12'}}], 'M.Cecchinato - A.Zverev': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '6,20', 'odds_2': '1,08'}}], 'M.Kecmanovic - A.Seppi': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,38', 'odds_2': '2,80'}}], 'N.Basilashvili - Kwon S-W': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,50', 'odds_2': '2,45'}}], 'N.Kyrgios - L.Sonego': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,12', 'odds_2': '5,20'}}], 'P.Cuevas - G.Simon': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '2,85', 'odds_2': '1,37'}}], 'PH.Herbert - C.Norrie': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,60', 'odds_2': '2,18'}}], 'R.Nadal - H.Dellien': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': ' - ', 'odds_2': ' - '}}], 'T.Fritz - T.Griekspoor': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,19', 'odds_2': '4,10'}}], 'Vilella - K.Khachanov': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '8,00', 'odds_2': '1,04'}}], 'Y.Sugita - E.Benchetrit': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '1,35', 'odds_2': '2,95'}}], 'Y.Uchiyama - M.Ymer': [{'veikkaus': {'event_description': 'ATP Australian Avoimet', 'odds_1': '3,60', 'odds_2': '1,24'}}], 'A.Anisimova - Z.Diyas': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,33', 'odds_2': '3,05'}}], 'A.Cornet - M.Niculescu': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,68', 'odds_2': '2,08'}}], 'A.Lottner - C.Giorgi': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '2,90', 'odds_2': '1,35'}}], 'A.Sharma - A.Kontaveit': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '4,30', 'odds_2': '1,18'}}], 'A.Tomljanovic - A.Sevastova': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '2,00', 'odds_2': '1,73'}}], 'B.Bencic - A.Schmiedlova': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,10', 'odds_2': '5,80'}}], 'Bondarenko - A.Rodionova': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,68', 'odds_2': '2,08'}}], 'C.Bellis - T.Maria': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,25', 'odds_2': '3,55'}}], 'D.Collins - V.Diatchenko': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,14', 'odds_2': '4,90'}}], 'D.Vekic - M.Sharapova': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,63', 'odds_2': '2,13'}}], 'E.Cocciaretto - A.Kerber': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '3,45', 'odds_2': '1,26'}}], 'E.Mertens - D.Kovinic': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,10', 'odds_2': '5,80'}}], 'E.Svitolina - K.Boulter': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,03', 'odds_2': '9,20'}}], 'G.Muguruza - S.Rogers': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,36', 'odds_2': '2,90'}}], 'H.Dart - M.Doi': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,63', 'odds_2': '2,15'}}], 'I-C.Begu - K.Bertens': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '4,90', 'odds_2': '1,14'}}], 'I.Swiatek - T.Babos': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '1,75', 'odds_2': '1,95'}}], 'J.Brady - S.Halep': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '2,80', 'odds_2': '1,38'}}], 'J.Paolini - A.Blinkova': [{'veikkaus': {'event_description': 'WTA Australian Avoimet', 'odds_1': '3,50', 'odds_2': '1,26'}}]}
