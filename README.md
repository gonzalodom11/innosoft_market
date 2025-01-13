# InnoSoft Days Online Store

Los **InnoSoft Days** son jornadas organizadas por estudiantes de la ETSII, enfocadas en promover el desarrollo sostenible a través de la informática y las nuevas tecnologías. Bajo el lema *"Compilemos un futuro sostenible"*, esta edición se ha destacado por actividades como charlas, talleres, torneos y más.

Este proyecto propone una tienda en línea para los **InnoSoft Days**, permitiendo a los usuarios adquirir productos oficiales, generar ingresos para futuras ediciones y fortalecer la visibilidad del evento.

---

## Tabla de Contenidos

1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Para comenzar](#para-comenzar)
3. [Whoosh](#whoosh)
4. [Beautiful Soup](#beautiful-soup)
5. [Extension points](#extension-points)

---

## Descripción del Proyecto

Este proyecto es una tienda online funcional basada en Django, con las funcionalidades esenciales de una plataforma de comercio electrónico:

- **Catálogo de productos**: Visualización de productos disponibles.
- **Carrito de compras**: Gestión de compras utilizando Django sessions.
- **Procesamiento de pedidos**: Realización de compras y envío de confirmaciones por correo electrónico.
- Uso de **Celery** como procesador de tareas y **RabbitMQ** como principal organizador.
- Enviar **correos electrónicos** a los usuarios tras completar una compra.
- **Scraping**: Extracción de productos de otras tiendas con Beautiful Soup.
- Índice de búsqueda utilizando **Whoosh**.

---
## Para comenzar 

Para comenzar, abre una terminal y utiliza el siguiente comando para crear un nuevo entorno virtual para este proyecto dentro del directorio env/:
```
PS C:\innosoft_market> python -m venv venv
```
Activar el entorno virtual:
Windows
```
venv\Scripts\activate
```
Linux
```
source venv/bin/activate
```
Instalar Django junto a las demás herramientas necesarias para el proyecto:
```
pip install -r requirements.txt
```
Para que funcionen las notificaciones por correo electrónico deberás crear un archivo de configuración como el siguiente en el directorio principal, .env:
```
EMAIL_HOST_USER=tucorreo@gmail.com
EMAIL_HOST_PASSWORD=xxxx xxxx xxxx xxxx
DEFAULT_FROM_EMAIL=Innosoft Market<tucorreo@gmail.com>
```

En este deberás introducir el correo principal de la tienda, desde donde se enviarán las notificaciones de compra. Si utilizar una dirección correo de google, tendrás que activar en Seguridad, la verificación en 2 pasos. Además, es necesario un llave de acceso para que la aplicación pueda utilizar tu cuenta gmail.

---

## Whoosh
Whoosh es una biblioteca de Python diseñada para implementar motores de búsqueda full-text. Es utilizada para crear, mantener y consultar índices de búsqueda, siendo una solución ligera y eficaz para proyectos que requieren capacidades de búsqueda en texto. Whoosh se destaca por ser independiente de la base de datos, lo que significa que no necesita un backend específico y puede usarse con cualquier aplicación. Configuración en settings.py:
```
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': BASE_DIR / 'whoosh_index',
    },
}
```

--- 

## Beautiful Soup
Beautiful Soup es una biblioteca de Python utilizada para extraer datos de documentos HTML y XML. Es especialmente útil para el web scraping, ya que permite navegar y manipular fácilmente la estructura de un documento web. Esta herramienta se integra bien con bibliotecas como requests para descargar páginas web y lxml o el analizador HTML interno de Python para procesar el contenido.

Se define una función que se encarga de la mayor parte del trabajo, tanto recogiendo la información como guardándola en la base de datos. Lo primero que hacemos es limpiar los productos que pertenecen a la categoría “Ratones inalámbricos” y la misma propia:
```
def populateDatabase():
    Category.objects.filter(name__in=["Ratones inalámbricos"]).delete()
```
Importante: definimos la url y los encabezados HTTP, incluyendo un User-Agent para simular una solicitud desde un navegador web.
```

    url = 'https://www.mediamarkt.es/es/category/ratones-inal%C3%A1mbricos-91.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    req = urllib.request.Request(url, headers=headers)
    f = urllib.request.urlopen(req)
    s = BeautifulSoup(f, "lxml")
```
---
## Extension points
- **Pasarela de pago**: implemetar un pasarela de pago con Stripe, para que el cliente puede hacer todo el proceso de compra en la web.
- **Modificar papeleta**: modificar el modelo de product de manera que el usuario pueda elegir el número de papeleta.
- **Gestión de cuentas**: aunque la cuenta de administrador está en funcionamiento, se puede implementar una nueva aplicación django para permitir al usuario entrar en su cuenta y modificar su perfil
