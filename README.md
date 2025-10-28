# Proyecto de Automatización - Pre Entrega

Este proyecto contiene pruebas automatizadas utilizando **Selenium**, **Pytest** y **pytest-html**.

## Estructura
```
Automatizacion-PreEntrega/
├── run.py
├── utils.py
├── conftest.py
├── requirements.txt
├── README.md
└── tests/
    ├── test_login.py
    ├── test_inventario.py
    ├── test_carrito.py
```

## Ejecución
1. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

2. Ejecutar todos los tests y generar el reporte HTML:
   ```bash
   python run.py
   ```

El archivo **report.html** se generará en la raíz del proyecto.
