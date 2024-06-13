# Animal Habitat Management - Odoo Module

## Descripción

El módulo **Animal Habitat Management** está diseñado para gestionar la información relacionada con los animales, sus cuidadores y los hábitats en los que residen. Es una herramienta útil para zoológicos, reservas naturales, y cualquier organización que necesite un sistema para organizar y controlar datos de animales y sus entornos.

Este módulo permite registrar y administrar la información de animales, sus fechas de nacimiento, especies, estado de conservación, y sus hábitats. Además, se incluye la gestión de cuidadores responsables de los animales.

## Estructura del Módulo

### Modelos Principales

1. **Animal (`animalhabitat.animal`)**
    - `name`: Nombre del animal.
    - `age`: Edad del animal (calculada automáticamente).
    - `birthday`: Fecha de nacimiento del animal.
    - `species`: Especie del animal.
    - `onExtinction`: Booleano que indica si el animal está en peligro de extinción.
    - `description`: Descripción del animal.
    - `habitat`: Relación Many2one con el modelo `habitat`.

2. **Caretaker (`animalhabitat.caretaker`)**
    - `name`: Nombre del cuidador.
    - `surname`: Apellido del cuidador.
    - `birthday`: Fecha de nacimiento del cuidador.
    - `description`: Descripción del cuidador.

3. **Habitat (`animalhabitat.habitat`)**
    - `name`: Nombre del hábitat.
    - `climate`: Clima del hábitat.
    - `humidity`: Humedad del hábitat (en porcentaje).
    - `ubication`: Ubicación del hábitat.
    - `animal`: Relación One2many con el modelo `animal`.

## Instalación

1. **Clonar el repositorio:**

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    ```

2. **Copiar el módulo a la carpeta de addons de Odoo:**

    ```bash
    cp -r <CARPETA_DEL_MODULO> /path/to/odoo/addons/
    ```

3. **Actualizar la lista de módulos en Odoo:**

    Inicia sesión en Odoo y navega a **Apps**. Luego, haz clic en **Actualizar lista de aplicaciones**.

4. **Instalar el módulo:**

    Busca el módulo "Animal Habitat Management" en la lista de aplicaciones y haz clic en **Instalar**.

## Uso

### Gestión de Animales

1. Navega a la sección de **Animales**.
2. Añade un nuevo animal proporcionando su nombre, fecha de nacimiento, especie y seleccionando su hábitat correspondiente.

### Gestión de Cuidadores

1. Ve a la sección de **Cuidadores**.
2. Añade un nuevo cuidador proporcionando su nombre, apellido y fecha de nacimiento.

### Gestión de Hábitats

1. Dirígete a la sección de **Hábitats**.
2. Crea un nuevo hábitat especificando su nombre, clima, humedad y ubicación.

### Cálculo de Edad de los Animales

La edad de los animales se calcula automáticamente en base a la fecha de nacimiento proporcionada. Esta funcionalidad es gestionada por el método `@api.depends('birthday')` que se encuentra en el modelo `animal`.

## Dependencias

- **Odoo**: Esta es una aplicación para Odoo y depende de la instalación previa de Odoo en tu sistema.
- **Python**: El código está escrito en Python 3.

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. **Fork el repositorio.**
2. **Crea una rama para tu característica (`git checkout -b feature/nueva-caracteristica`).**
3. **Confirma tus cambios (`git commit -am 'Añadir nueva característica'`).**
4. **Envía tu rama al repositorio principal (`git push origin feature/nueva-caracteristica`).**
5. **Abre una solicitud de extracción.**


## Contacto

Puedes encontrar más sobre mi [aquí](https://github.com/AncorGG).
