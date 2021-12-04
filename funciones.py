from datetime import datetime,timedelta

def mensaje(texto):
    fecha_hora = datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
    print(fecha_hora+" "+str(texto))

