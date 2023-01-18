"""
создание списка
res = {
    '052XL7D4': {
        'name': 'БОЙКО ВОЛОДИМИР ІВАНОВИЧ'
        'visits': {
            '2020-01-01': [
                ['08:11:52', '12:17:53']
                ['13:35:46', '18:10:02']
            ],
            '2020-01-01': [
                ['08:11:52', '12:17:53']
                ['13:35:46', '18:10:02']
            ]
        }
    },
    '052XL7D4': {
        'name': 'БОЙКО ВОЛОДИМИР ІВАНОВИЧ'
        'visits': {
            '2020-01-01': [
                ['08:11:52', '12:17:53']
                ['13:35:46', '18:10:02']
            ],
            '2020-01-01': [
                ['08:11:52', '12:17:53']
                ['13:35:46', '18:10:02']
            ]
        }
    },
    ...
}
"""
import pathlib
from pprint import pprint

PATH = 'Users\alexa\PycharmProjects\pythonProject1'

CREW_FILENAME = 'crew.txt'
ENTRANCE_FILENAME = 'entrance.log'
EXIT_FILENAME = 'exit.log'


def read_files(path: str) -> tuple:
    path = pathlib.Path(path).resolve()
    try:
        with open('../45/crew.txt', encoding='utf-8') as cf, \
                open('../45/entrance.txt', encoding='utf-8') as enf, \
                open('../45/exit.txt', encoding='utf-8') as exf:
            crew = cf.readlines()
            enter = enf.readlines()
            exit_ = exf.readlines()
    except:
        raise FileNotFoundError(f'Got a wrong path "{path}"!')
    return crew, enter, exit_


def parsing_dict(data_parsing: list) -> dict:
    parsed_dict = {**dict(tuple(filter(None, map(str.strip, str(item).split('|')))
                                for item in data_parsing))}
    return parsed_dict


def parsing_list(data_parsing: list) -> list:
    parsed_list = list(filter(None, ((tuple(map(str.strip, item.replace('|', '').split()))
                                              for item in data_parsing))))
    return sorted(parsed_list)


def person_info(person_id: str, entranse: list, exit: list) -> dict:
    visit_dic = {}
    for (id_into_in, date_into_in, time_into_in), (id_into_out, date_into_out, time_into_out) in zip(entranse, exit):
        if id_into_in != person_id:
            continue
        _time_in_out = [time_into_in, time_into_out]
        if visit_dic.get(date_into_in) is None:
            visit_dic.update({date_into_in: [_time_in_out]})
        else:
            visit_dic[date_into_in].append(_time_in_out)
    return visit_dic


def my_main(path: str) -> dict:
    if not isinstance(path, str):
        raise TypeError(f'Got {type(path)}, expected string')
    res = {}
    crew, enter, exit = read_files(path)
    p_crew = parsing_dict(crew)
    p_enter = parsing_list(enter)
    p_exit = parsing_list(exit)

    for code, name in p_crew.items():
        res.update({
            code: {
                'name': name,
                'visits': person_info(code, p_enter, p_exit)
            }
        })
    return res


if __name__ == '__main__':
    pprint(my_main(PATH), width=100)