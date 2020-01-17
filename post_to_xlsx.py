from datetime import datetime

from openpyxl import Workbook, load_workbook

from build_xlsx import prpre_for_insrt_new_match
from build_xlsx import prpr_for_insrt_exst_mtch

file_name = 'result.xlsx'
index_of_time = 6


def creat_xlsl_file():
    wb = Workbook()
    ws = wb.active

    ws['B1'] = 'veikkaus'  # creating header for 'veikkaus data'
    ws.merge_cells('B1:F1')
    ws['B2'] = 'tournament'
    ws['C2'] = 'odds_1'
    ws['D2'] = 'odds_2'
    ws['E2'] = 'odds_1_new'
    ws['F2'] = 'odds_2_new'

    ws['G1'] = 'time'  # creating header for 'Time'
    ws.merge_cells('G1:G2')

    ws['H1'] = 'bet365'  # creating header for bet365 data'
    ws.merge_cells('H1:Q1')
    ws['H2'] = 'odds_1'
    ws['I2'] = 'odds_2'
    ws['J2'] = 'col_1'
    ws['K2'] = 'col_2'
    ws['L2'] = 'col_1_12h'
    ws['M2'] = 'col_2_12h'
    ws['N2'] = 'col_1_6h'
    ws['O2'] = 'col_2_6h'
    ws['P2'] = 'col_1_started'
    ws['Q2'] = 'col_2_started'

    ws['R1'] = 'William Hill'  # creating header for William Hill data
    ws.merge_cells('R1:AA1')
    ws['R2'] = 'odds_1'
    ws['S2'] = 'odds_2'
    ws['T2'] = 'col_1'
    ws['U2'] = 'col_2'
    ws['V2'] = 'col_1_12h'
    ws['W2'] = 'col_2_12h'
    ws['X2'] = 'col_1_6h'
    ws['Y2'] = 'col_2_6h'
    ws['Z2'] = 'col_1_started'
    ws['AA2'] = 'col_2_started'

    ws['AB1'] = '1xBet'  # creating header for 1xBet data
    ws.merge_cells('AB1:AK1')
    ws['AB2'] = 'odds_1'
    ws['AC2'] = 'odds_2'
    ws['AD2'] = 'col_1'
    ws['AE2'] = 'col_2'
    ws['AF2'] = 'col_1_12h'
    ws['AG2'] = 'col_2_12h'
    ws['AH2'] = 'col_1_6h'
    ws['AI2'] = 'col_2_6h'
    ws['AJ2'] = 'col_1_started'
    ws['AK2'] = 'col_2_started'

    ws['AL1'] = 'Pinnacle'  # creating header for Pinnacle data
    ws.merge_cells('AL1:AU1')
    ws['AL2'] = 'odds_1'
    ws['AM2'] = 'odds_2'
    ws['AN2'] = 'col_1'
    ws['AO2'] = 'col_2'
    ws['AP2'] = 'col_1_12h'
    ws['AQ2'] = 'col_2_12h'
    ws['AR2'] = 'col_1_6h'
    ws['AS2'] = 'col_2_6h'
    ws['AT2'] = 'col_1_started'
    ws['AU2'] = 'col_2_started'

    ws['AV1'] = 'result'  # creating header for 'Result of match'
    ws.merge_cells('AV1:AV2')

    wb.save(file_name)
    return file_name


def xlsl_file_exists():
    try:
        work_book = load_workbook(file_name)
        return work_book
    except FileNotFoundError:
        work_book = False
        return work_book


def update_xlsl_file(matches_data):
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


def calc_delta_time(time):
    try:
        time = time.replace(',', '').replace(':', ' ')
        tm = datetime.strptime(time, '%d %b %Y %H %M')
        now = datetime.now()
        delta = tm - now
        delta = round((delta.seconds / 3600), 2)
        return delta
    except ValueError:
        return 0


def update_row(ws, num_of_row, inserting_row):
    # for creating coordinates of cell
    cols_for_changing = list()
    cols = range(69, 92)
    for col in cols:
        if col == 91:
            a_cols = range(65, 87)
            for a_col in a_cols:
                a_cols_for_changing = [65, a_col]
                cols_for_changing.append(a_cols_for_changing)
        else:
            cols_for_changing.append(col)
    ind = 4
    for col in cols_for_changing:
        # ir = inserting_row[ind]
        if ind < 7:
            y = f'{chr(col)}{num_of_row}'
            ws[f'{chr(col)}{num_of_row}'].value = inserting_row[ind]
        elif ind in [9, 10, 19, 20, 29, 30, 39, 40]:
           # calculate time. return delta time
            delta = calc_delta_time(inserting_row[index_of_time])
            # delta = 12
            if 5.3 < delta < 6.8:
                col_index = cols_for_changing.index(col) + 4
                col = cols_for_changing[col_index]
                if isinstance(col, list):
                    z = f'{chr(col[0])}{chr(col[1])}{num_of_row}'
                    ws[f'{chr(col[0])}{chr(col[1])}{num_of_row}'].value = inserting_row[ind]
                else:
                    p = f'{chr(col)}{num_of_row}'
                    ws[f'{chr(col)}{num_of_row}'].value = inserting_row[ind]
            elif 11.3 < delta < 12.8:
                col_index = cols_for_changing.index(col) + 2
                col = cols_for_changing[col_index]
                if isinstance(col, list):
                    x = f'{chr(col[0])}{chr(col[1])}{num_of_row}'
                    ws[f'{chr(col[0])}{chr(col[1])}{num_of_row}'].value = inserting_row[ind]
                else:
                    o = f'{chr(col)}{num_of_row}'
                    ws[f'{chr(col)}{num_of_row}'].value = inserting_row[ind]

        if isinstance(col, list):
            if ws[f'{chr(col[0])}{chr(col[1])}{num_of_row}'].value == ' - ' and ind > 6:
                m = f'{chr(col[0])}{chr(col[1])}{num_of_row}'
                ws[f'{chr(col[0])}{chr(col[1])}{num_of_row}'].value = inserting_row[ind]
        else:
            if ws[f'{chr(col)}{num_of_row}'].value == ' - ' and ind > 6:
                ws[f'{chr(col)}{num_of_row}'].value = inserting_row[ind]
        ind += 1


def write_to_xlsl(work_book, matches_data):
    timestamp = str(datetime.now().strftime("Last update: %d/%m/%Y %H:%M:%S"))
    ws = work_book.get_active_sheet()
    ws['A3'].value = timestamp  # inserting date of the last update
    for match in matches_data:
        match_exists = match_exist_in_sheet(ws, match)  # (int) return number of row where match is written
        if match_exists:
            inserting_row = prpr_for_insrt_exst_mtch(matches_data[match])
            inserting_row[0] = match
            update_row(ws, match_exists, inserting_row)
        else:
            inserting_row = prpre_for_insrt_new_match(matches_data[match])
            inserting_row[0] = match
            ws.append(inserting_row)
    work_book.save(file_name)
