import time
from prometheus_client import start_http_server, Counter, Gauge

PETICIONES_TOTALES = Counter('peticiones_servidor_total', 'Numero total de peticiones recibidas')
USO_MEMORIA = Gauge('memoria_uso_porcentaje', 'Porcentaje actual de memoria usada')

if __name__ == '__main__':
    start_http_server(8000)
    print("Servidor corriendo en http://localhost:8000/metrics")
    
    memoria_actual = 40.0  # Inicia normal en 40%
    
    while True:
        PETICIONES_TOTALES.inc()
        memoria_actual += 3.0  # Sube 3% constantemente
        
        if memoria_actual > 100.0:
            print("--- ¡COLAPSO DEL SERVIDOR! Reiniciando memoria... ---")
            memoria_actual = 40.0
            
        USO_MEMORIA.set(memoria_actual)
        time.sleep(2)