# NoLimits
## _Visualización en tiempo real / Visualization in real time_

[ESP]
NoLimits es una aplicación de escritorio que permite al usuario ver en tiempo real los cambios en la concurrencia de las 100 principales monedas criptográficas.

- Visualiza el cambio de la moneda en tiempo real
- Selecciona la moneda de interés para evaluar su cambio
- Guarda la data analizada en una BASE DE DATOS

[ENG]
NoLimits is a desktop application that allows users to see real-time changes in the concurrency of the top 100 cryptocurrencies.

- Visualizes currency changes in real-time
- Selects the currency of interest to evaluate its change
- Saves analyzed data into a DATABASE

## Features

[ESP]
- Consume una API para recuperar información en tiempo real
- Guarda los datos en archivos en crudo y en formato de base de datos
- Ofrece funcionalidad para limpiar los registros de datos
- Muestra un gráfico evolutivo con los cambios en los datos

[ENG]
- Consumes API to retrieve real-time information
- Saves data in raw files and database format
- Offers data cleanup functionality
- Displays an evolutionary graph with data changes

## Tech

[ESP]
Se utilizan las siguientes tecnologías para el desarrollo de la aplicación:

- [Python] - Lenguaje de alto nivel orientado a objetos
- [PostgreSQL] - Base de datos para la captura y almacenamiento de datos
- [Flask] - Framework para el desarrollo de aplicaciones web
- [HTML & CSS] - Diseño de la interfaz de usuario
- [Matplotlib] - Desarrollo de gráficos

[ENG]
The following technologies are used for the development of the application:

- [Python] - High-level object-oriented programming language
- [PostgreSQL] - Database for capturing and saving data
- [Flask] - Framework for web application development
- [HTML & CSS] - User interface design
- [Matplotlib] - Graph development

## Configuración del Entorno / Env Config

### [ESP]

1. Clona el repositorio y navega al directorio del proyecto:

    ```bash
    git clone https://github.com/chdencor/NoLimits-Webapp.git
    cd direccion-al-repositorio
    ```

2. Crea y activa un entorno virtual:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # En Windows: .venv\Scripts\activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Configura las variables de entorno necesarias (ver `.env.example`).

5. Ejecuta la aplicación:

    ```bash
    flask run
    ```

### [ENG]

1. Clone the repository and navigate to the project directory:

    ```bash
    git clone https://github.com/chdencor/NoLimits-Webapp.git
    cd project-directory
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure the necessary environment variables (see `.env.example`).

5. Run the application:

    ```bash
    flask run
    ```
