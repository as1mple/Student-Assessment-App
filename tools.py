import pandas as pd
import matplotlib as mpl

mpl.rcParams['font.size'] = 30.0

from pars import Parse_rate


def update_rate(col, pat):
    URL_dict = {'тк': "YOUR_PARAMS",
                'пром': "YOUR_PARAMS"}

    bot = Parse_rate(url=URL_dict.get(col), demo_mode=False, save_path=pat.get(col))
    bot.start()


def load_data(path: str):
    data = pd.read_csv(path)
    subs = ['Українська мова ', 'Історія України ', 'Математика ', 'Середній бал документа про освіту ',
            'Бал за успішне закінчення підготовчих курсів закладу освіти ']

    def get_sub_value(sub):
        def get_sub(person):
            if len(person := person.split(sub)) > 1:
                value = person[1].split(' ')[0]
            else:
                value = 0
            return value

        return get_sub

    def validetion_fill(dataseries):
        for sub in subs:
            if sub in dataseries:
                if not f' {sub}' in dataseries:
                    dataseries = dataseries.replace(sub, f' {sub}')
        return dataseries

    data.Деталізація = data.Деталізація.apply(validetion_fill)
    for key, value in zip(['Mova', 'History', 'Math', 'School', 'Course'], subs):
        data[key] = data.Деталізація.apply(get_sub_value(value))
    data = data.drop('Деталізація', axis=1)
    data = data.rename(columns={'ПІБ': 'Name',
                                'Бал': 'Score',
                                'Стан': 'Status',
                                'КО': 'Koef',
                                'Д': 'Document',
                                'Тип': 'Type',
                                'КВ': 'Kvota',
                                '№': 'Place'})
    columns = ['Place', 'Score', 'Name', 'Math', 'Mova', 'School', 'Course', 'History', 'Kvota', 'Koef', 'Document',
               'Status']
    return data[columns]
