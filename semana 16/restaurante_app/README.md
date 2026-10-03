## Manejo de eventos aplicado a la gestion de usuarios

### Descripcion del proyecto

En esta Semana 16 se continuo con el desarrollo de la aplicacion 'restaurante_app', manteniendo la estructura trabajada en las semanas anteriores.

En esta actividad se aplico el manejo de eventos en Tkinter para realizar la gestion de usuarios de un restaurante.

La aplicacion permite registrar, consultar, actualizar y eliminar usuarios mediante una interfaz grafica.Ademas, la informacion se guarda en archivos JSON para mantener los datos almacenados.

### Objetivo

El objeto de esta semana es aplicar el manejo de eventos en Tkinter mediante el uso de 'bind()', funciones callback y componentes como 'Treeview' y 'Combobox',

La idea es que las acciones realizadas por el usuario generen eventos que sean procesados por la aplicacion y produzcan una respuesta en la interfaz.

### Funcionalidades

La aplicacion permite realizar las siguientes operaciones:

- Registrar usuarios.
- Consultar usuarios.
- Seleccionar usuarios desde una tabla.
- Actualizar los datos de los usuarios.
- Eliminar usuarios.
-Limpiar el formulario.
- Seleccionar el rol del usuario. 
- Seleccionar el estado del usuario.
- Guardar la informacion en archivos JSON.
- Cargar nuevamente la informacion almacenada.

### Eventos utilizados

En esta Semana 16 se implementaron los siguientes eventos de Tkinter:

-'<<TreeviewSelect>>'
-'<Return>'
-'<Escape>'
-'<<ComboboxSelected>>'

El evento '<<TreeviewSelect>>' permite utiliza para detectar cuando se selecciona un usuario en la tabla y cargar sus datos en el formulario.

El evento '<Return>' permite utilizar la tecla Enter para ejecutar el registro de un usuario.

El evento '<Escape>' permite limpiar el formulario y cancelar la seleccion actual.

El evento '<<ComboboxSelected>>' permite detectar cuando se cambia el rol seleccionado en el 'Combobox'.

### Flujo del manejo de eventos

El funcionamiento de la aplicacion sigue el siguiente flujo:

'''text
Interaccion del usuario
        
Evento de Tkinter

brind()

Callback

Servicio
        
Persistencia en JSON 

Actualizacion de la interfaz
