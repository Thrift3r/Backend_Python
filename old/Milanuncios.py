import csv
from idlelib import browser

for i in range(1, 2338):
    url_base = 'https://www.milanuncios.com/telefonia/?pagina='+str(i)
    print('Estamos en la pagina:'+url_base)
    browser_url = browser.get(url_base)
    output = 'data.csv'
    data_file = open(output, 'w')
    writer = csv.writer(data_file)
    writer.writerow(['url','titulo','descripcion','ubicacion','vendedor','precio','particular', 'stats_visto', 'stats_contactado', 'stats_compartido', 'stats_favorito', 'stats_renovados'])
    scroll = 400