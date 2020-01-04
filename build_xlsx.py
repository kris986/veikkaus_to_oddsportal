from datetime import datetime

from openpyxl import Workbook, load_workbook


def creating_xlsl():
    wb = Workbook()
    ws = wb.active

    ws['B1'] = 'veikkaus'  # creating header for 'veikkaus data'
    ws.merge_cells('B1:C1')
    ws['B2'] = 'odds_1'
    ws['C2'] = 'odds_2'

    ws['D1'] = 'time'  # creating header for 'Time'
    ws.merge_cells('D1:D2')

    ws['E1'] = 'bet365'  # creating header for bet365 data'
    ws.merge_cells('E1:H1')
    ws['E2'] = 'odds_1'
    ws['F2'] = 'odds_2'
    ws['G2'] = 'col_1'
    ws['H2'] = 'col_2'

    ws['I1'] = 'William Hill'  # creating header for William Hill data
    ws.merge_cells('I1:L1')
    ws['I2'] = 'odds_1'
    ws['J2'] = 'odds_2'
    ws['K2'] = 'col_1'
    ws['L2'] = 'col_2'

    ws['M1'] = '1xBet'  # creating header for 1xBet data
    ws.merge_cells('M1:P1')
    ws['M2'] = 'odds_1'
    ws['N2'] = 'odds_2'
    ws['O2'] = 'col_1'
    ws['P2'] = 'col_2'

    ws['Q1'] = 'Pinnacle'  # creating header for Pinnacle data
    ws.merge_cells('Q1:T1')
    ws['Q2'] = 'odds_1'
    ws['R2'] = 'odds_2'
    ws['S2'] = 'col_1'
    ws['T2'] = 'col_2'

    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    file_name = 'result-' + timestamp + '.xlsx'
    wb.save(file_name)
    return file_name


# param match is a list type
def prepare_for_inserting(match):
    ready_list = list(range(0, 20))
    for item in match:
        for key, val in item.items():
            if key == 'veikkaus':
                ready_list[1] = item[key]['odds_1']
                ready_list[2] = item[key]['odds_2']
            elif key == 'time':
                ready_list[3] = item['time']
            elif key == 'bet365':
                ready_list[4] = item[key]['odds_1']
                ready_list[5] = item[key]['odds_2']
                ready_list[6] = item[key]['col_1']
                ready_list[7] = item[key]['col_2']
            elif key == 'William Hill':
                ready_list[8] = item[key]['odds_1']
                ready_list[9] = item[key]['odds_2']
                ready_list[10] = item[key]['col_1']
                ready_list[11] = item[key]['col_2']
            elif key == '1xBet':
                ready_list[12] = item[key]['odds_1']
                ready_list[13] = item[key]['odds_2']
                ready_list[14] = item[key]['col_1']
                ready_list[15] = item[key]['col_2']
            elif key == 'Pinnacle':
                ready_list[16] = item[key]['odds_1']
                ready_list[17] = item[key]['odds_2']
                ready_list[18] = item[key]['col_1']
                ready_list[19] = item[key]['col_2']
    print(ready_list)
    return ready_list


def write_to_excel(matches_data):
    file_name = creating_xlsl()
    wb = load_workbook(file_name)
    ws = wb.get_active_sheet()
    checker = 3  # insert rows from 3 row. 2 first rows take header
    for match in matches_data:
        inserting_row = prepare_for_inserting(matches_data[match])
        inserting_row[0] = match
        ws.insert_rows(checker)
        ws.append(inserting_row)
        checker += 1
        wb.save(file_name)
    wb.save(file_name)

# dict_d = {
#     'R.Nadal - N.Basilashvili': [
#         {
#             'veikkaus': {
#                 'odds_1': '1,04',
#                 'odds_2': '8,40'
#             }
#         },
#         {
#             'time': '04 Jan 2020, 12:00'
#         },
#         {
#             'bet365': {
#                 'col_1': '1.04',
#                 'odds_1': '1.05',
#                 'col_2': '9.00',
#                 'odds_2': '8.50'
#             }
#         },
#         {
#             'William Hill': {
#                 'col_1': '1.05',
#                 'odds_1': '1.04',
#                 'col_2': '10.00',
#                 'odds_2': '9.00'
#             }
#         },
#         {
#             '1xBet': {
#                 'col_1': '1.03',
#                 'odds_1': '1.09',
#                 'col_2': '16.00',
#                 'odds_2': '11.00'
#             }
#         },
#         {
#             'Pinnacle': {
#                 'col_1': '1.07',
#                 'odds_1': '1.05',
#                 'col_2': '10.01',
#                 'odds_2': '11.94'
#             }
#         }
#     ],
#     'D.Kuzmanov - A.Cozbinov': [
#         {
#             'veikkaus': {
#                 'odds_1': '1,07',
#                 'odds_2': '7,00'
#             }
#         },
#         {
#             'time': '05 Jan 2020, 00:00'
#         },
#         {
#             'bet365': {
#                 'col_1': '1.08',
#                 'col_2': '7.00'
#             }
#         },
#         {
#             'William Hill': {
#                 'col_1': '1.07',
#                 'col_2': '8.00'
#             }
#         },
#         {
#             '1xBet': {
#                 'col_1': '1.11',
#                 'odds_1': '1.06',
#                 'col_2': '7.10',
#                 'odds_2': '14.50'
#             }
#         },
#         {
#             'Pinnacle': {
#                 'col_1': '1.11',
#                 'odds_1': '1.06',
#                 'col_2': '7.60',
#                 'odds_2': '12.97'
#             }
#         }
#     ],
#     'F.Fognini - Ca.Ruud': [
#         {
#             'veikkaus': {
#                 'odds_1': '1,38',
#                 'odds_2': '2,80'
#             }
#         }
#     ],
#     'S.Darcis - C.Norrie': [
#         {
#             'veikkaus': {
#                 'odds_1': '2,95',
#                 'odds_2': '1,35'
#             }
#         },
#         {
#             'time': '05 Jan 2020, 07:30'
#         },
#         {
#             'bet365': {
#                 'col_1': '2.75',
#                 'odds_1': '2.75',
#                 'col_2': '1.40',
#                 'odds_2': '1.40'
#             }
#         },
#         {
#             'William Hill': {
#                 'col_1': '2.90',
#                 'odds_1': '2.50',
#                 'col_2': '1.40',
#                 'odds_2': '1.40'
#             }
#         },
#         {
#             '1xBet': {
#                 'col_1': '2.90',
#                 'odds_1': '2.44',
#                 'col_2': '1.44',
#                 'odds_2': '1.59'
#             }
#         },
#         {
#             'Pinnacle': {
#                 'col_1': '2.96',
#                 'odds_1': '2.04',
#                 'col_2': '1.44',
#                 'odds_2': '1.84'
#             }
#         }
#     ],
#     'D.Medvedev - J.Isner': [
#         {
#             'veikkaus': {
#                 'odds_1': '1,27',
#                 'odds_2': '3,45'
#             }
#         },
#         {
#             'time': '05 Jan 2020, 12:00'
#         },
#         {
#             'bet365': {
#                 'col_1': '1.28',
#                 'odds_1': '1.28',
#                 'col_2': '3.50',
#                 'odds_2': '3.50'
#             }
#         },
#         {
#             'William Hill': {
#                 'col_1': '1.33',
#                 'odds_1': '1.33',
#                 'col_2': '3.30',
#                 'odds_2': '3.30'
#             }
#         },
#         {
#             '1xBet': {
#                 'col_1': '1.32',
#                 'odds_1': '1.35',
#                 'col_2': '3.54',
#                 'odds_2': '3.36'
#             }
#         },
#         {
#             'Pinnacle': {
#                 'col_1': '1.29',
#                 'odds_1': '1.33',
#                 'col_2': '3.86',
#                 'odds_2': '3.51'
#             }
#         }
#     ]
# }
# write_to_excel(dict_d)
