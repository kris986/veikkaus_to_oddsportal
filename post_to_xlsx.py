from datetime import datetime

from openpyxl import Workbook, load_workbook

from build_xlsx import prepare_for_inserting


def creat_xlsl_file():
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

    timestamp = datetime.now().strftime("%Y%m%d")
    file_name = 'result-' + timestamp + '.xlsx'
    wb.save(file_name)
    return file_name


def xlsl_file_exists():
    file_name = 'result-' + datetime.now().strftime("%Y%m%d") + '.xlsx'
    try:
        work_book = load_workbook(file_name)
        return work_book
    except FileNotFoundError:
        work_book = False
        return work_book


def update_xlsl_file(matches_data):
    file_name = 'result-' + datetime.now().strftime("%Y%m%d") + '.xlsx'
    work_book = xlsl_file_exists()
    if work_book:
        write_to_xlsl(work_book, matches_data)
    else:
        creat_xlsl_file()
        work_book = xlsl_file_exists()
        write_to_xlsl(work_book, matches_data)
    work_book.save(file_name)


def write_to_xlsl(work_book, matches_data):
    timestamp = list([datetime.now().strftime("%d/%m/%Y Time: %H:%M:%S")])
    file_name = 'result-' + datetime.now().strftime("%Y%m%d") + '.xlsx'
    ws = work_book.get_active_sheet()
    ws.append(timestamp)
    for match in matches_data:
        inserting_row = prepare_for_inserting(matches_data[match])
        inserting_row[0] = match
        ws.append(inserting_row)
    work_book.save(file_name)
