import re
import pandas as pd
import matplotlib.pyplot as plt
import datetime
from wordcloud import WordCloud

filename = "chat.txt"
messages =[]

#Examples: 31/12/22 23:59 - username: msj



with open(filename, "r") as file:
    for line in file:
        # Buscar el patrón de fecha y hora
        pattern = r"^(.\d{1,2}.\d{1,2}.\d{2,4},?\s\d{1,2}.*\d{2}) - (.+?): (.*)$"
        match = re.match(pattern, line)
        if match:
            # Extraer los elementos de la línea
            timestamp = match.group(1)
            username = match.group(2)
            message = match.group(3)
            try:
                fecha_datetime = datetime.datetime.strptime(timestamp, "%d/%m/%y %H:%M")
            except ValueError:
                fecha_datetime = datetime.datetime.strptime(timestamp, "%d.%m.%y, %H:%M")
            messages.append({
                "FECHA": timestamp,
                "USUARIO": username,
                "MENSAJE": message,
                "FECHA_DATETIME": fecha_datetime
            })


df = pd.DataFrame(messages)


#01
###################################################################################################
 # group messages by user and count the number of messages
user_message_count = df.groupby(['USUARIO'])['MENSAJE'].count()
# plot the data
fig, ax = plt.subplots(figsize=(8, 6))
user_message_count.plot(kind='bar', ax=ax, color=['orchid','deepskyblue'], alpha=0.5)

# set plot title and axis labels
ax.set_title('Mensajes enviados por usuario')
#ax.set_xlabel('Usuario')
ax.set_ylabel('Número de mensajes')

# rotate x-axis labels horizontally
ax.tick_params(axis='x', rotation=0)
# display a horizontal grid
ax.yaxis.grid(True)
fig.savefig('01_msj_enviados_usuario.png', dpi=300, bbox_inches='tight')
###################################################################################################

#02
###################################################################################################

omit_words = ['<Multimedia omitido>', '<multimedia', 'omitido>','null']
all_words = []
for message in df['MENSAJE']:
    words = message.split()
    for word in words:
        if word.lower() not in omit_words:
            all_words.append(word.lower())

# Crear un DataFrame con las frecuencias de cada palabra
word_counts = pd.Series(all_words).value_counts().sort_values(ascending=False)

word_counts = word_counts[word_counts.index.str.len() > 3]

# Crear un mapa de palabras
wordcloud = WordCloud(width=800, height=400, background_color='white',colormap='winter').generate_from_frequencies(word_counts)

# Mostrar el mapa de palabras
fig, ax = plt.subplots(figsize=(12, 6))
ax.imshow(wordcloud, interpolation='bilinear') 
ax.axis('off')
fig.savefig('02_mapa_palabra.png', dpi=300, bbox_inches='tight')
###################################################################################################

#03
###################################################################################################
# Agrupar los mensajes por semana y contar el número de mensajes por semana
weekly_counts = df.groupby(pd.Grouper(key='FECHA_DATETIME', freq='W'))['MENSAJE'].count()

colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

# Crear un gráfico de barras de los mensajes por semana
fig, ax = plt.subplots(figsize=(12, 6))
weekly_counts.plot(kind='bar', ax=ax, color=colors, alpha=0.5)

# set plot title and axis labels
ax.set_title('Mensajes por semana')
ax.set_xlabel('Semana')
ax.set_ylabel('Número de mensajes')
labels = [label.strftime('%Y-%m-%d') for label in weekly_counts.index]
ax.set_xticklabels(labels)
# display a horizontal grid
ax.yaxis.grid(True)
plt.xticks(fontsize=8)

ax.tick_params(axis='x', rotation=45)

fig.savefig('03_msj_enviados_por_semana.png', dpi=300, bbox_inches='tight')


###################################################################################################

#04
###################################################################################################
hourly_counts = df.groupby(['USUARIO', df['FECHA_DATETIME'].dt.hour])['MENSAJE'].count().unstack()
# Trasponer el DataFrame para que los usuarios se conviertan en columnas
hourly_counts = hourly_counts.T
colors = ['#FFA07A', '#87CEFA', '#90EE90', '#FFC0CB']

# Crear una gráfica apilada por usuario con colores personalizados
fig1, ax1 = plt.subplots(figsize=(12, 6))
hourly_counts.plot(kind='bar', stacked=True, color=colors, ax=ax1, alpha=0.7)

# Personalizar los ejes y agregar un título
ax1.set_xlabel('Hora del día')
ax1.set_ylabel('Número de mensajes')
ax1.set_title('Número de mensajes por hora del día y usuario')

# Mostrar la gráfica
fig1.savefig('04_hora_de_los_msj.png', dpi=300, bbox_inches='tight')

###################################################################################################



#05
###################################################################################################
multimedia_count=0
multimedia_count = df[df['MENSAJE'].str.contains('<Multimedia omitido>')]['MENSAJE'].count()

# Crear una imagen que muestre el número de veces que aparece la cadena
fig2, ax2 = plt.subplots()
plt.text(0.5, 0.5, str(multimedia_count), fontsize=100, ha='center', va='center', color='navy')
ax2.set_title('Imágenes o videos enviados')

# Ocultar ejes y mostrar la imagen
ax2.axis('off')
fig2.savefig('05_multimedia.png', dpi=300, bbox_inches='tight')

###################################################################################################


#06
###################################################################################################


# Agregar una columna con la fecha sin la hora
df['FECHA_DIA'] = df['FECHA_DATETIME'].dt.date

# Contar los mensajes por usuario y por día
daily_counts = df.groupby(['USUARIO', 'FECHA_DIA']).count()['MENSAJE']

# Calcular el promedio de mensajes diarios por usuario
avg_daily_counts = daily_counts.groupby('USUARIO').mean()

# Crear una gráfica de barras para mostrar los promedios
fig, ax = plt.subplots()
ax.bar(avg_daily_counts.index, avg_daily_counts.values, color=['pink','navy'], alpha=0.7)

# Personalizar los ejes y agregar un título
ax.set_xlabel('Usuario')
ax.set_ylabel('Promedio de mensajes diarios')
ax.set_title('Promedio de mensajes diarios por usuario')

# Mostrar la gráfica

fig.savefig('06_promedio_msj_diarios.png', dpi=300, bbox_inches='tight')  