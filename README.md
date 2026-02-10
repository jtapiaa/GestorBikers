# Evaluación del Módulo 3
Proyecto: Sistema de gestión de Datos de Corredores Federación de Ciclisco V Región

Descripción
Sistema de gestión de ciclistas (bikers) que permite registrar, validar, guardar y leer información desde archivos de texto.

## 🚀 Características

- Registro de bikers con validación de RUT
- Almacenamiento en archivo `.txt`
- Lectura de bikers desde archivo
- Prevención de registros duplicados
- Uso de estructuras `list` y `dict`

## 🛠️ Tecnologías

- Python 3.12.1+
- Git / GitHub
- Archivos TXT (CSV-like)

## 📂 Estructura del proyecto
src
├── model/
│ └── biker.py
├── data/
│ └── bikers.txt
├── services/
│ └── controller.py
├── utils/
│ └── file_manager.py
|.└── module_11.py
├── main.py
└── README.md

### 6️⃣ Formato del archivo de datos
```md
## 📄 Formato del archivo bikers.txt
Cada línea representa un biker con el siguiente formato:

RUT,Nombre,Apellido,Edad,Categoría,Ciudad,Club

Ejemplo:
17208981-K,Juan Pablo,Tapia Arancibia,37,Master B,Nogales,EcoTeam

## ▶️ Cómo ejecutar

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/tu-repo.git
2. Entrar a proyecto
    cd tu-repo
3. Ejecutar 
    python main.py

### 8️⃣ Ejemplo de uso
```md
## 🧪 Ejemplo de uso

- El usuario ingresa los datos del biker
- El sistema valida el RUT
- El biker se guarda en `data/bikers.txt`
- Al iniciar, el sistema carga los bikers desde el archivo

---

### 8️⃣ Ejemplo de uso
```md
## 🧪 Ejemplo de uso

- El usuario ingresa los datos del biker
- El sistema valida el RUT
- El biker se guarda en `data/bikers.txt`
- Al iniciar, el sistema carga los bikers desde el archivo

## 👤 Autor

Juan Pablo Tapia Arancibia
