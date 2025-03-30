# CRUD de Tareas - Django  

![CRUD Tareas](https://github.com/user-attachments/assets/2d188d87-e63c-46d7-8100-f4032ff1857a)  

## 🛠 Tecnologías utilizadas  
- **Python**  
- **Django**  
- **PostgreSQL**  

## 📌 Sobre el Proyecto  
Este es un **CRUD** para la gestión de tareas desarrollado como parte de una **prueba técnica**, utilizando **vistas basadas en funciones (FBV)**.  

## 📥 Clonar el Repositorio  
```sh
git clone https://github.com/BarbadeProgramador/pruebaTecnica-CrudDjango
```

> ⚠ **Importante:**  
> El archivo `requirements.txt` **no está incluido** en el repositorio.  

## 🔧 Instalación de Dependencias  
Para usar PostgreSQL, instala la siguiente dependencia:  
```sh
pip install psycopg2
```

## 📌 Ejecutar Migraciones  
```sh
python manage.py migrate
```

## ⚡ Consejo para Configuración Rápida  
Si deseas probar el proyecto sin configurar PostgreSQL, puedes usar **SQLite**. Solo agrega la siguiente configuración en `settings.py` y luego ejecuta la migración:  

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```
