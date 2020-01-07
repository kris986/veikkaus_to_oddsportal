from datetime import datetime

from openpyxl import Workbook, load_workbook


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


def update_xlsl_file():
    # timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    # work_book = False
    file_name = 'result-' + datetime.now().strftime("%Y%m%d") + '.xlsx'
    work_book = xlsl_file_exists()
    if work_book:
        write_to_xlsl(work_book)
    else:
        creat_xlsl_file()
        work_book = xlsl_file_exists()
        write_to_xlsl(work_book)
    work_book.save(file_name)


def write_to_xlsl(work_book):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    file_name = 'result-' + datetime.now().strftime("%Y%m%d") + '.xlsx'
    # wb = load_workbook(file_name)
    ws = work_book.get_active_sheet()
    checker = 0  # insert rows from 3 row. 2 first rows take header
    ws.insert_rows(checker)
    ws.append(timestamp)
    work_book.save(file_name)


update_xlsl_file()
