# 🏠 Proyecto Inmuebles Chile - Sistema de Arriendos con Django

**Inmuebles Chile** es una plataforma web completa para la gestión de arriendos de propiedades en Chile, desarrollada con Django y PostgreSQL. El proyecto abarca desde la configuración inicial del entorno hasta funcionalidades avanzadas como migraciones de datos, autenticación de usuarios y operaciones CRUD complejas. Este sistema fue desarrollado como parte de un programa formativo en desarrollo web.

---

## ⚙️ Stack Tecnológico

* **Lenguaje:** Python 3.10+
* **Framework backend:** Django 5.0.7
* **Base de datos:** PostgreSQL 12+ (con psycopg2 2.9.9)
* **Frontend:** HTML5 + CSS3 + JavaScript
* **ORM:** Django ORM para operaciones de base de datos
* **Autenticación:** Sistema de usuarios integrado de Django
* **Gestión de dependencias:** PIP (requirements.txt incluido)
* **Control de versiones:** Git

### 📦 Dependencias principales
```text
asgiref==3.8.1
Django==5.0.7
psycopg2==2.9.9
sqlparse==0.5.1
tzdata==2024.1
```

---

## ✨ Funcionalidades principales

### 🏗️ Hito 1: Configuración Inicial y Modelos

* **Entorno de desarrollo completo**:
  - Configuración de PostgreSQL para producción
  - Creación de ambiente virtual con Python
  - Instalación de paquetes esenciales para Django

* **Modelado de datos avanzado**:
  - Modelo `Region` con todas las regiones de Chile
  - Modelo `Comuna` relacionado con las regiones
  - Modelo `TipoInmueble` para clasificar propiedades
  - Modelo `Inmueble` con campos detallados:
    - `nombre`, `descripcion`, `m2_construidos`, `m2_totales`
    - `cantidad_estacionamientos`, `cantidad_habitaciones`, `cantidad_banos`
    - `direccion`, `precio_mensual`, `tipo_inmueble` (FK)
    - `comuna` (FK), `arrendador` (FK a User)
  - Modelos de usuario personalizados para `Arrendador` y `Arrendatario`

* **Operaciones CRUD básicas**:
  - Creación, lectura, actualización y eliminación de inmuebles
  - Gestión de usuarios con permisos diferenciados

---

### 📊 Hito 2: Migraciones y Datos

#### 🗃️ Población de la base de datos
* Carga inicial con `loaddata` de:
  - Todas las **16 regiones** y **346 comunas** de Chile
  - Tipos de inmuebles básicos (Casa, Departamento, Oficina, etc.)
  - Datos de prueba para usuarios e inmuebles

#### 📝 Scripts de reportes
* **Reporte por comunas**:
  - Listado filtrado por comuna
  - Campos: nombre y descripción del inmueble
  - Salida en archivo TXT estructurado

* **Reporte por regiones**:
  - Agrupación de inmuebles por región
  - Conteo de propiedades disponibles
  - Exportación a formato TXT

---

### 🔐 Hito 3: Autenticación y Perfiles

#### 👥 Sistema de usuarios
* **Vista de login** personalizada:
  - Validación de credenciales
  - Redirección según tipo de usuario
* **Vista de registro**:
  - Formulario para arrendadores/arrendatarios
  - Validación de datos personales
* **Perfiles de usuario**:
  - Página personal para arrendadores:
    - Listado de sus propiedades
  - Página personal para arrendatarios:
* **Edición de perfiles**:
  - Actualización de datos personales

---

### 🛠️ Hito 4: Operaciones Avanzadas con ORM

#### 🏡 Gestión de inmuebles
* **Publicación de nuevas propiedades**:
  - Formulario multipaso con validación
* **Edición de propiedades**:
  - Formulario pre-cargado con datos actuales
  - Modificación de fotos existentes
* **Búsqueda avanzada**:
  - Filtros por: región y comuna 


#### 📱 Vistas responsivas
* Adaptación para móviles de:
  - Listados de propiedades
  - Formularios de contacto
  - Páginas de perfil

---

## 🛡️ Seguridad y Buenas Prácticas

* **Protección de rutas**:
  - `@login_required` para vistas críticas
  - `@user_passes_test` para permisos específicos
* **Validación de formularios**:
  - Sanitización de inputs
  - Validación de tipos de archivo en uploads
* **Protección de datos**:
  - Los arrendadores solo ven/editan sus propiedades

---

## 💡 Lecciones aprendidas

* **Configuración avanzada de Django con PostgreSQL**:
  - Optimización de conexiones
  - Manejo de transacciones complejas

* **Migraciones de datos masivos**:
  - Carga eficiente de datos geográficos
  - Manejo de relaciones complejas

* **Patrones de diseño MVC en Django**:
  - Separación clara de responsabilidades
  - Reutilización de componentes

* **Seguridad en aplicaciones web**:
  - Protección contra inyecciones SQL
  - Manejo seguro de uploads

---

