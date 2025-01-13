# Proyecto_Python_HashReveal

# Hash Decryptor
# Este proyecto es una herramienta para desencriptar hashes utilizando distintos métodos, incluyendo diccionario y fuerza bruta. Soporta varios tipos de hash comunes, como MD5, SHA-1, SHA-256, y Argon2. El objetivo de este proyecto es ofrecer una manera sencilla de intentar desencriptar un hash, tanto con un archivo de diccionario como con la opción de usar un enfoque de fuerza bruta.

# Requisitos
# Antes de ejecutar la herramienta, asegúrate de tener instaladas las siguientes dependencias:
# - Python 3.x
# - Pip (gestor de paquetes de Python)

# Dependencias necesarias:
# - **argon2**: Para manejar y verificar hashes Argon2.
# - **hashlib**: Para los hashes MD5, SHA-1, SHA-256, SHA-512, etc.
# - **itertools**: Para generar combinaciones de caracteres para la fuerza bruta.

# Instala las dependencias ejecutando el siguiente comando:
# pip install argon2


# Descripción de la Herramienta
# Funcionamiento Principal
# 1. **Detectar Hash**: El sistema intenta identificar el tipo de hash automáticamente (MD5, SHA-1, SHA-256, o Argon2) al proporcionarle un hash.
# 2. **Desencriptado con Diccionario**: Si el tipo de hash es detectado, se intenta desencriptar el hash comparando las contraseñas en un archivo de diccionario.
# 3. **Fuerza Bruta**: Si el hash no se encuentra en el diccionario o si no es posible identificar el tipo de hash, la herramienta puede intentar desencriptar el hash mediante fuerza bruta, generando combinaciones de caracteres posibles.
# 4. **Tiempo de Ejecución**: Se muestra el tiempo que tardó el proceso de desencriptado, tanto si se usó el diccionario como si se usó la fuerza bruta.

# Archivos Involucrados
# - `decrypt_hash.sh`: Script principal para ejecutar la herramienta en tu terminal.
# - `dictionary.txt`: Un archivo de texto que contiene un listado de posibles contraseñas que se probarán para desencriptar el hash.

# Uso
# 1. Ejecutar el Script
# Una vez que hayas instalado todas las dependencias, puedes ejecutar el script de la siguiente manera:
# ./decrypt_hash.sh


# Este script realizará lo siguiente:
# 1. Solicitará un hash para desencriptar.
# 2. Intentará identificar el tipo de hash (MD5, SHA-1, SHA-256, o Argon2).
# 3. Si el tipo de hash es compatible, intentará desencriptarlo utilizando el archivo de diccionario (`dictionary.txt`) si está disponible.
# 4. Si no se encuentra el hash en el diccionario, el sistema procederá a usar fuerza bruta para intentar descifrar el hash.
# 5. Se mostrará el tiempo que ha tardado el proceso de desencriptado.

# 2. Probar el Hash
# Cuando el script te pida que ingreses un hash, puedes proporcionarle uno de los siguientes tipos:
# - MD5
# - SHA-1
# - SHA-256
# - Argon2 (Para hashes Argon2, la herramienta usará la opción de fuerza bruta debido a la naturaleza de este algoritmo)

# Ejemplo:
# d95b6e6b5317876c79e493c90a178f759a6ffd54

# El script intentará desencriptar el hash de acuerdo con el tipo detectado.

# 3. Archivo de Diccionario
# El archivo `dictionary.txt` contiene una lista de palabras que se utilizarán para intentar el desencriptado de hashes. Puedes modificar este archivo agregando tus propias palabras, o incluso usar un archivo de diccionario más grande para mejorar la efectividad del proceso.

# 4. Resultados
# Una vez que el script termine de intentar desencriptar el hash, te mostrará los resultados:
# - Si el hash fue desencriptado exitosamente, mostrará la contraseña original.
# - Si no pudo ser desencriptado utilizando el diccionario o la fuerza bruta, te informará que no se pudo encontrar la contraseña.
# - También se mostrará el tiempo que ha tardado en intentar cada proceso.

# Funcionalidad
# 1. **Fuerza Bruta para Hashes**: Si el hash no se encuentra en el diccionario, el sistema generará automáticamente combinaciones de caracteres posibles (letras y números) para tratar de coincidir con el hash.
# 2. **Soporte de Hashes Comunes**: Este sistema soporta los tipos de hash más comunes (MD5, SHA-1, SHA-256) y también el potente algoritmo Argon2, aunque en este último caso la fuerza bruta es más efectiva debido a la seguridad del algoritmo.
# 3. **Optimización de Tiempo**: Para cada tipo de hash, se mostrará cuánto tiempo ha tomado cada intento de desencriptado, ya sea con el diccionario o con fuerza bruta.

# Ejemplo de Ejecución
# Al ejecutar el script, puede que veas una salida similar a la siguiente:
# Detectando el tipo de hash para: d95b6e6b5317876c79e493c90a178f759a6ffd54
# Se detectó el tipo de hash: SHA-1
# Tiempo de ejecución: 16.47 segundos.
# No se pudo desencriptar el hash usando el tipo detectado (SHA-1).

# Si no se puede encontrar el hash en el diccionario, el script intentará usar fuerza bruta:
# No se pudo desencriptar el hash usando fuerza bruta.

# Contribuciones
# Si deseas mejorar esta herramienta o agregar soporte para otros tipos de hashes, siéntete libre de realizar un fork del repositorio y hacer las modificaciones que consideres necesarias. Asegúrate de seguir las buenas prácticas de codificación y de proporcionar documentación clara sobre las modificaciones que realizas.

# Licencia
# Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE.TXT para más detalles.
