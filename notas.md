"# Mi Plan de Aprendizaje: IA y Mantenimiento" 
"## Modulo 2: Monitoreo con Prometheus" 

### Arquitectura y Funcionamiento
* Modelo Pull: Prometheus va a buscar las metricas activamente a los sistemas (no espera a que se las envien).
* Exporters: Programas auxiliares que convierten las variables de un sistema (servidor, base de datos, motor) en metricas legibles para Prometheus.
* Scrape Interval: Frecuencia con la que Prometheus consulta y recolecta las metricas de los Exporters.
