"# Mi Plan de Aprendizaje: IA y Mantenimiento" 
"## Modulo 2: Monitoreo con Prometheus" 

### Arquitectura y Funcionamiento
* Modelo Pull: Prometheus va a buscar las metricas activamente a los sistemas (no espera a que se las envien).
* Exporters: Programas auxiliares que convierten las variables de un sistema (servidor, base de datos, motor) en metricas legibles para Prometheus.
* Scrape Interval: Frecuencia con la que Prometheus consulta y recolecta las metricas de los Exporters.

### Consultas con PromQL
* PromQL: Lenguaje de consultas para extraer y filtrar metricas en Prometheus.
* Consulta simple: Muestra el valor actual de una variable (ej. memoria disponible).
* Consulta con filtro: Permite buscar eventos especificos usando etiquetas (ej. solo errores tipo 500).
* Funciones de tiempo: Permiten calcular promedios o velocidades de cambio en intervalos de tiempo (ej. ultimos 5 minutos).
"
ejemplos
Cuanta memoria RAM libre hay ahora                                 PromQL: node_memory_MemFree_bytes

Cual es el porcentaje de CPU usado en los ultimos 5 minutos        PromQL: rate(node_cpu_seconds_total[5m])

Cuantos errores 500 ha tenido mi sistema                            PromQL: http_requests_total{status="500"}
"
de consola a vs code
### Laboratorio Practico Exporter en Python
* prometheus_client: Libreria de Python utilizada para exponer un endpoint de metricas en formato Prometheus.
* Endpoint /metrics: Punto de acceso HTTP en el puerto 8000 donde Prometheus realiza el raspado Pull de los datos....

de consola a vs code

### Simulación de Mantenimiento Predictivo
* Analisis de Tendencia: Evaluacion del historial de lecturas (Series Temporales) para detectar patrones de crecimiento anormall.
* Deteccion Preventiva: Emision de alertas dinamicas antes de que el recurso alcance un limite critico (100%), evitando caidas de servicio.