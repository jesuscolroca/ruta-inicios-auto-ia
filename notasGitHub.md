GUIA PRACTICA: GIT Y GITHUB
Enfoque en las 3 fases clave: ADD, COMMIT y PUSH

CONCEPTOS BASICOS

Git: Programa en tu computadora. Funciona como una máquina del tiempo para registrar los cambios en tu disco duro sin necesidad de internet.

GitHub: Página web en la nube. Es donde guardas el respaldo de tus proyectos en internet para consultarlos o compartirlos.

CONFIGURACION Y PRIMER USO (Solo se hace una vez)

Paso 1 (En la web): Entras a GitHub, haces clic en el botón mas, eliges Crear Nuevo Repositorio, le pones nombre y marcas la casilla Crear README.

Paso 2 (En tu PC): Copias la dirección HTTPS de GitHub. Abres la terminal CMD y ejecutas:
git clone URL_DE_TU_REPOSITORIO
cd NOMBRE_DE_TU_CARPETA

Paso 3 (Identificación):
git config --global user.name "TuNombre"
git config --global user.email "tu-correo@ejemplo.com"

EL FLUJO DE TRABAJO DIARIO (Las 3 frases clave)
Cada vez que crees, edites o elimines un archivo en tu computadora, ejecuta esta secuencia en la terminal:

FASE 1: PREPARAR (git add)
Coloca los archivos modificados en la caja de envío.
Para un archivo especifico: git add notas.md
Para todos los archivos a la vez: git add .

FASE 2: SELLAR Y REGISTRAR (git commit)
Cierra la caja y toma la foto local. Guarda un punto de control en tu computadora.
Comando: git commit -m "Escribe aqui una breve nota de lo que cambiaste"

FASE 3: ENVIAR A LA NUBE (git push)
Envía la caja sellada desde tu computadora hacia GitHub por internet.
Comando: git push

COMANDO DE APOYO

git status: Te muestra en pantalla si hay archivos modificados pendientes por guardar o enviar.


