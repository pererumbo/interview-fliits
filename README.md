# Fliits - Technical Interview Setup

¡Bienvenido/a! 🎉

Este repositorio contiene el entorno de configuración para la entrevista técnica en **FLiiTS**. Por favor, sigue los pasos a continuación **antes de la entrevista** para asegurarte de que todo funciona correctamente.

---

## Requisitos previos

### 1. IDE de SQL

Necesitarás un IDE o cliente de SQL para conectarte a la base de datos PostgreSQL durante la entrevista.

Algunas opciones recomendadas:
- **DBeaver** (gratuito, multiplataforma): [https://dbeaver.io/](https://dbeaver.io/)
- **DataGrip** (de pago, con prueba gratuita): [https://www.jetbrains.com/datagrip/](https://www.jetbrains.com/datagrip/)
- **pgAdmin** (gratuito, específico para PostgreSQL): [https://www.pgadmin.org/](https://www.pgadmin.org/)

### 2. Docker

Asegúrate de tener Docker instalado y en funcionamiento.

- **macOS/Windows**: [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- **Linux**: [Docker Engine](https://docs.docker.com/engine/install/)

Verifica la instalación:

```bash
docker --version
```

### 3. Python 3.12

Necesitarás Python 3.12 instalado en tu sistema.

- **macOS** (con Homebrew):
  ```bash
  brew install python@3.12
  ```
- **Linux** (Ubuntu/Debian):
  ```bash
  sudo apt update
  sudo apt install python3.12
  ```
- **Windows**: [Descarga desde python.org](https://www.python.org/downloads/)

Verifica la instalación:

```bash
python3.12 --version
```

### 4. Poetry

Poetry es el gestor de dependencias que utilizamos.

Instalación:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Si tienes algun problema puedes ver la documentación oficial: https://python-poetry.org/docs/#installing-with-the-official-installer


Verifica la instalación:

```bash
poetry --version
```

> **Nota**: Puede que necesites reiniciar tu terminal o añadir Poetry al PATH después de la instalación.

---

## Configuración del entorno

### Paso 1: Levantar PostgreSQL con Docker

Ejecuta el siguiente comando para iniciar una instancia de PostgreSQL:

```bash
docker run --name postgres_fliits \
  -e POSTGRES_PASSWORD=password \
  -p 5432:5432 \
  -d postgres:16.8
```

Verifica que el contenedor está corriendo:

```bash
docker ps
```

Deberías ver `postgres_fliits` en la lista de contenedores activos.

### Paso 2: Instalar dependencias con Poetry

Desde la raíz del proyecto, ejecuta:

```bash
poetry install
```

### Paso 3: Verificar la configuración

Ejecuta el script de verificación para comprobar que todo está funcionando correctamente:

```bash
poetry run python check.py
```

Si todo está bien configurado, deberías ver un mensaje como este:

```
🔍 Comprobando conexión a la base de datos...
✅ CREATE TABLE OK
✅ INSERT OK

✅ SELECT con pandas OK
   id   name  value
0   1  alpha     10
1   2   beta     20
2   3  gamma     30

🎉 Todo está listo para la entrevista técnica 🚀
```

Eso es todo, asegúrate de tener todo funcionando correctamente antes de la entrevista. 

---

## Troubleshooting

### El contenedor de PostgreSQL no arranca

Si ya existe un contenedor con el mismo nombre, elimínalo primero:

```bash
docker rm -f postgres_fliits
```

Y vuelve a ejecutar el comando de `docker run`.

### Error de conexión a la base de datos

Asegúrate de que:
1. El contenedor de Docker está corriendo (`docker ps`)
2. El puerto 5432 no está siendo usado por otra aplicación
3. Las credenciales son correctas (usuario: `postgres` y password: `password`)

### Poetry no encuentra Python 3.12

Especifica la versión de Python al instalar:

```bash
poetry env use python3.12
poetry install
```

---

## ¿Problemas?

Si encuentras algún problema durante la configuración, no dudes en contactarnos. ¡Nos vemos en la entrevista! 💪

