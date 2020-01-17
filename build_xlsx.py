def check_and_handle_key(dictinary, key):
    if key in dictinary:
        return dictinary[key]
    else:
        return ' - '


def prpre_for_insrt_new_match(match):
    ready_list = list()
    for pos in range(48):
        ready_list.append(' - ')
    for item in match:
        for key in item:
            if key == 'veikkaus':
                ready_list[1] = check_and_handle_key(item[key], 'event_description')
                ready_list[2] = check_and_handle_key(item[key], 'odds_1')
                ready_list[3] = check_and_handle_key(item[key], 'odds_2')
                # dummy for new matches
                ready_list[4] = check_and_handle_key(item[key], 'odds_1_new')
                ready_list[5] = check_and_handle_key(item[key], 'odds_2_new')
            elif key == 'time':
                ready_list[6] = check_and_handle_key(item, 'time')
            elif key == 'bet365':
                ready_list[7] = check_and_handle_key(item[key], 'odds_1')
                ready_list[8] = check_and_handle_key(item[key], 'odds_2')
                ready_list[9] = check_and_handle_key(item[key], 'col_1')
                ready_list[10] = check_and_handle_key(item[key], 'col_2')
                # ready_list[11] = ' - '
                # ready_list[12] = ' - '
                # ready_list[13] = ' - '
                # ready_list[14] = ' - '
                # ready_list[15] = ' - '
                # ready_list[16] = ' - '
            elif key == 'William Hill':
                ready_list[17] = check_and_handle_key(item[key], 'odds_1')
                ready_list[18] = check_and_handle_key(item[key], 'odds_2')
                ready_list[19] = check_and_handle_key(item[key], 'col_1')
                ready_list[20] = check_and_handle_key(item[key], 'col_2')
                # ready_list[21] = ' - '
                # ready_lis[22] = ' - '
                # ready_list[23] = ' - '
                # ready_list[24] = ' - '
                # ready_list[25] = ' - '
                # ready_list[26] = ' - '
            elif key == '1xBet':
                ready_list[27] = check_and_handle_key(item[key], 'odds_1')
                ready_list[28] = check_and_handle_key(item[key], 'odds_2')
                ready_list[29] = check_and_handle_key(item[key], 'col_1')
                ready_list[30] = check_and_handle_key(item[key], 'col_2')
                # ready_list[31] = ' - '
                # ready_list[32] = ' - '
                # ready_list[33] = ' - '
                # ready_list[34] = ' - '
                # ready_list[35] = ' - '
                # ready_list[36] = ' - '
            elif key == 'Pinnacle':
                ready_list[37] = check_and_handle_key(item[key], 'odds_1')
                ready_list[38] = check_and_handle_key(item[key], 'odds_2')
                ready_list[39] = check_and_handle_key(item[key], 'col_1')
                ready_list[40] = check_and_handle_key(item[key], 'col_2')
                # ready_list[41] = ' - '
                # ready_list[42] = ' - '
                # ready_list[43] = ' - '
                # ready_list[44] = ' - '
                # ready_list[45] = ' - '
                # ready_list[46] = ' - '
            # ready_list[47] = ' - '
    return ready_list


def prpr_for_insrt_exst_mtch(match):
    ready_list = list()
    for pos in range(48):
        ready_list.append(' - ')
    for item in match:
        for key in item:
            if key == 'veikkaus':
                # dummy for existing matches
                ready_list[1] = check_and_handle_key(item[key], 'event_description')
                ready_list[2] = check_and_handle_key(item[key], 'odds_1_exist')
                ready_list[3] = check_and_handle_key(item[key], 'odds_2_exist')
                # end dummy for existing matches
                ready_list[4] = check_and_handle_key(item[key], 'odds_1')
                ready_list[5] = check_and_handle_key(item[key], 'odds_2')
            elif key == 'time':
                ready_list[6] = check_and_handle_key(item, 'time')
            elif key == 'bet365':
                ready_list[7] = check_and_handle_key(item[key], 'odds_1')
                ready_list[8] = check_and_handle_key(item[key], 'odds_2')
                ready_list[9] = check_and_handle_key(item[key], 'col_1')
                ready_list[10] = check_and_handle_key(item[key], 'col_2')
                # ready_list[11] = ' - '
                # ready_list[12] = ' - '
                # ready_list[13] = ' - '
                # ready_list[14] = ' - '
                # ready_list[15] = ' - '
                # ready_list[16] = ' - '
            elif key == 'William Hill':
                ready_list[17] = check_and_handle_key(item[key], 'odds_1')
                ready_list[18] = check_and_handle_key(item[key], 'odds_2')
                ready_list[19] = check_and_handle_key(item[key], 'col_1')
                ready_list[20] = check_and_handle_key(item[key], 'col_2')
                # ready_list[21] = ' - '
                # ready_lis[22] = ' - '
                # ready_list[23] = ' - '
                # ready_list[24] = ' - '
                # ready_list[25] = ' - '
                # ready_list[26] = ' - '
            elif key == '1xBet':
                ready_list[27] = check_and_handle_key(item[key], 'odds_1')
                ready_list[28] = check_and_handle_key(item[key], 'odds_2')
                ready_list[29] = check_and_handle_key(item[key], 'col_1')
                ready_list[30] = check_and_handle_key(item[key], 'col_2')
                # ready_list[31] = ' - '
                # ready_list[32] = ' - '
                # ready_list[33] = ' - '
                # ready_list[34] = ' - '
                # ready_list[35] = ' - '
                # ready_list[36] = ' - '
            elif key == 'Pinnacle':
                ready_list[37] = check_and_handle_key(item[key], 'odds_1')
                ready_list[38] = check_and_handle_key(item[key], 'odds_2')
                ready_list[39] = check_and_handle_key(item[key], 'col_1')
                ready_list[40] = check_and_handle_key(item[key], 'col_2')
                # ready_list[41] = ' - '
                # ready_list[42] = ' - '
                # ready_list[43] = ' - '
                # ready_list[44] = ' - '
                # ready_list[45] = ' - '
                # ready_list[46] = ' - '
            # ready_list[47] = ' - '
    return ready_list
