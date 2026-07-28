import time
import random
from prometheus_client import start_http_server, Counter, Gauge

# 1. Definimos las métricas
PETICIONES_TOTALES = Counter('peticiones_servidor_total', 'Numero total de peticiones recibidas')
USO_MEMORIA = Gauge('memoria_uso_porcentaje', 'Porcentaje actual de memoria usada')

if __name__ == '__main__':
    # 2. Iniciamos el servidor de métricas en el puerto 8000
    start_http_server(8000)
    print("Servidor de metricas corriendo en http://localhost:8000/metrics")
    
    # 3. Simulamos el funcionamiento del sistema en un bucle infinito
    while True:
        # Simula que llega una petición
        PETICIONES_TOTALES.inc()
        
        # Simula que la memoria fluctúa entre 40% y 95%
        USO_MEMORIA.set(random.uniform(40.0, 95.0))
        
        # Espera 2 segundos antes de volver a actualizar
        time.sleep(2)