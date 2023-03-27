import pyshark

# Capturar paquetes de red
capture = pyshark.LiveCapture(interface="wlxc4e98407a185")

# Filtrar paquetes de tipo HTTP
capture.filter('http')

# Recorrer los paquetes capturados
for packet in capture:
    # Extraer la información del paquete HTTP
    print(packet.http.request_full_uri)
