import streamlit as st
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.size'] = 30.0

from tools import *

st.title('Рейтинг поступающих')
path = {'тк': 'vtk.csv',
        'пром': 'prom.csv'}

college = st.text_area('Введите колледж', "Названи", height=25).lower()

if st.button('Обновить'):
    update_rate(college, path)
    st.write('Запускаю')

data_load_state = st.text('Loading data...')
data = load_data(path.get(college))
data_load_state.text('Loading data...done!')
st.write("""
* Рейтинг
""")

data

name = st.text_area('Ваш рейтинг', 'Фамилия и инициалы', height=25)
lgl_rate = data.query(f'Name == "{name}"')
lgl_rate

hist_name = st.text_area('Hist', 'Math', height=25)
fig, ax = plt.subplots(figsize=(25, 25))

ax.hist(data[hist_name].apply(float))

fig

seq_inpt = st.text_area('Pie', 'Math', height=25)

fig, ax = plt.subplots(figsize=(25, 25))
ax.pie(list(data[seq_inpt].value_counts().values), labels=list(data[seq_inpt].value_counts().keys()), autopct='%1.1f%%',
       shadow=True, wedgeprops={'lw': 1, 'ls': '--', 'edgecolor': "k"}, rotatelabels=True)

fig