import difflib
import antigravity

genuine = [
    "«Братец-хлеб» из Китая носит плащ и корону из булочек, чтобы кормить чаек",
    "Мясо гигантских тараканов станет вкусной и недорогой альтернативой говядине",
    "Скандал в ботаническом саду: 10 миллионов рублей ушло на зарплату кактусам",
]

plagiary = [
    "Китайский хлебный братец кормит чаек плащом и короной из булочек",
    "Гигантское мясо тараканов станет говядине недорогой и вкусной альтернативой",
    "Зарплата кактусов в ботаническом саду составила 10 скандальных миллионов рублей",
]


def compare_phrase_and_results(search_phrase: str, result_phrase: str) -> bool:
    search_phrase = search_phrase.replace('.', '. ').replace('-', ' ')
    result_phrase = result_phrase.replace('-', ' ')
    search_list = sorted(list(search_phrase.split(' ')))
    result_list = sorted(list(result_phrase.split(' ')))
    sf = ' '.join(search_list)
    rf = ' '.join(result_list)
    print(similarity(sf, rf))
    if similarity(sf, rf) >= 0.8:
      return True
    else:
      return False


def similarity(s1, s2):
    normalized1 = s1.lower()
    normalized2 = s2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    return matcher.ratio()


# print(similarity(genuine[0], plagiary[0]))

compare_phrase_and_results('K.Kozlov - Hon', 'Kozlova Kat. - Hon P.')
compare_phrase_and_results('H.Dart - S.Halep', 'Dart H. - Halep S.')
compare_phrase_and_results('P.Gojowczyk - Carreno Busta', 'Gojowczyk P. - Carreno-Busta P.')
