from datetime import datetime

from openpyxl import Workbook, load_workbook

from build_xlsx import prpre_for_insrt_new_match
from build_xlsx import prpr_for_insrt_exst_mtch


def creat_xlsl_file():
    wb = Workbook()
    ws = wb.active

    ws['B1'] = 'veikkaus'  # creating header for 'veikkaus data'
    ws.merge_cells('B1:E1')
    ws['B2'] = 'odds_1'
    ws['C2'] = 'odds_2'
    ws['D2'] = 'odds_1_new'
    ws['E2'] = 'odds_2_new'

    ws['F1'] = 'time'  # creating header for 'Time'
    ws.merge_cells('F1:F2')

    ws['G1'] = 'bet365'  # creating header for bet365 data'
    ws.merge_cells('G1:J1')
    ws['G2'] = 'odds_1'
    ws['H2'] = 'odds_2'
    ws['I2'] = 'col_1'
    ws['J2'] = 'col_2'

    ws['K1'] = 'William Hill'  # creating header for William Hill data
    ws.merge_cells('K1:N1')
    ws['K2'] = 'odds_1'
    ws['L2'] = 'odds_2'
    ws['M2'] = 'col_1'
    ws['N2'] = 'col_2'

    ws['O1'] = '1xBet'  # creating header for 1xBet data
    ws.merge_cells('O1:R1')
    ws['O2'] = 'odds_1'
    ws['P2'] = 'odds_2'
    ws['Q2'] = 'col_1'
    ws['R2'] = 'col_2'

    ws['S1'] = 'Pinnacle'  # creating header for Pinnacle data
    ws.merge_cells('S1:V1')
    ws['S2'] = 'odds_1'
    ws['T2'] = 'odds_2'
    ws['U2'] = 'col_1'
    ws['V2'] = 'col_2'

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
    # timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    # work_book = False
    file_name = 'result-' + datetime.now().strftime("%Y%m%d") + '.xlsx'
    work_book = xlsl_file_exists()
    if work_book:
        write_to_xlsl(work_book, matches_data)
    else:
        creat_xlsl_file()
        work_book = xlsl_file_exists()
        write_to_xlsl(work_book, matches_data)
    work_book.save(file_name)


def match_exist_in_sheet(ws, match):
    print(f'Match: {match}')
    iter_rows = ws.iter_rows()
    for row in iter_rows:
        for cell in row:
            cell_val = cell.value
            if cell_val == match:
                num_row = cell.row
                return num_row
            else:
                num_row = False
    return num_row


def update_row(ws, num_of_row, inserting_row):
    # for creating coordinates of cell
    # cols_for_changing = ['D', 'E', 'F' ,'G']
    cols_for_changing = list()
    cols = range(68, 87)
    for col in cols:
        cols_for_changing.append(chr(col))
    # print(cols_for_changing)
    # print(ord('D'), ord('V'))
    # inserting_row = ['odds_1_new', 'odds_2_new', 'Time new']
    ind = 3
    for col in cols_for_changing:
        # print(f'{col}{num_of_row}')
        if ind < 6:
            ws[f'{col}{num_of_row}'].value = inserting_row[ind]
        elif ws[f'{col}{num_of_row}'].value == ' - ' and ind > 5:
            ws[f'{col}{num_of_row}'].value = inserting_row[ind]
        ind += 1


def write_to_xlsl(work_book, matches_data):
    # timestamp = list([datetime.now().strftime("Last update: %d/%m/%Y %H:%M:%S")])
    timestamp = str(datetime.now().strftime("Last update: %d/%m/%Y %H:%M:%S"))

    file_name = 'result-' + datetime.now().strftime("%Y%m%d") + '.xlsx'
    ws = work_book.get_active_sheet()
    # ws.append(timestamp)
    ws['A3'].value = timestamp  # inserting date of the last update
    for match in matches_data:
        match_exists = match_exist_in_sheet(ws, match)  # (int) return number of row where match is written
        if match_exists:
            inserting_row = prpr_for_insrt_exst_mtch(matches_data[match])
            inserting_row[0] = match

            update_row(ws, match_exists, inserting_row)
            # print(f'A{match_exists}')
            # ws[f'A{match_exists}'].value = f'hello New {match}'

            # ws.insert_rows(match_exists)
            # ws.append(inserting_row)
        else:
            inserting_row = prpre_for_insrt_new_match(matches_data[match])
            inserting_row[0] = match
            ws.append(inserting_row)
    work_book.save(file_name)
