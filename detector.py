import time
import requests
import re

URL_METRICAS = "http://localhost:8000/metrics"
historial_memoria = []

print("=== INICIANDO DETECTOR DE ANOMALÍAS E IA PREDICTIVA ===")

while True:
    try:
        # 1. Hacemos el Pull de las métricas
        respuesta = requests.get(URL_METRICAS)
        texto_metricas = respuesta.text
        
        # 2. Extraemos el valor de la memoria
        coincidencia = re.search(r'memoria_uso_porcentaje ([\d.]+)', texto_metricas)
        
        if coincidencia:
            memoria_actual = float(coincidencia.group(1))
            historial_memoria.append(memoria_actual)
            
            if len(historial_memoria) > 4:
                historial_memoria.pop(0)
            
            print(f"Lectura actual: {memoria_actual:.1f}% | Historial: {historial_memoria}")
            
            # 3. Detección de anomalía (Mantenimiento Predictivo)
            if len(historial_memoria) == 4:
                es_subida_constante = (
                    historial_memoria[0] < historial_memoria[1] < historial_memoria[2] < historial_memoria[3]
                )
                
                if es_subida_constante and memoria_actual > 60.0:
                    print("\n⚠️ [ALERTA PREDICTIVA IA] Detectada tendencia inusual de consumo de memoria.")
                    print(f"   La memoria sigue subiendo ({memoria_actual:.1f}%). Riesgo de colapso en breve.\n")
                    
    except Exception as e:
        print(f"Esperando conexión con el servidor de métricas... ({e})")
        
    time.sleep(2)