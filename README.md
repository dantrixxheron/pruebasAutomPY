# 🧪 Pruebas Automatizadas en Python.

Este repositorio contiene dos ejercicios sencillos para practicar pruebas automatizadas en Python:

1. **Operaciones matemáticas básicas** (`suma`, `resta`, `multiplicación`, `división`)
2. **Validación de renta de auto** en función de la edad del usuario.
3. **Descuento de una tienda** bajo ciertas condiciones.
4. **Validación de contraseña segura** según el contenido de esta.
5. **Otorgar préstamos** según el sueldo y otras condicionantes.
6. **Validación y corroboración del tipo de triángulo** según las medidas de sus lados.

## 🧠 ¿Qué se prueba?
### operaciones.py
En el módulo `operaciones.py`, se comprueba que los resultados de las funciones básicas sean correctos para una amplia gama de valores, incluyendo bordes y casos negativos.

### rentaAuto.py
En `rentaAuto.py`, se verifica si un usuario puede rentar un auto y si se le aplica una tarifa extra, según su edad.

### descuento.py
En `descuento.py`, se verifica la cantidad de descuento a aplicar (si este fuera acumulable) dependiendo del nivel de membresía del cliente y cantidad a comprar.

### passwords.py
El código de `passwords.py` se comprueba si la contraseña es segura bajo ciertos parámetros: si contiene números, letras mayúsculas y minúsculas, algún caracter especial y la longitud entre 8 a 16 caracteres.

### prestamos.py
En este código se hace la solución a si a una persona se le cederá un crédito bajo ciertos indicadores: su salario, historial de crédito y de pagos.

### triangulos.py
En este código en base a tres medidas ingresadas se reconoce si es un triángulo y qué clase de triángulo es (escaleno, equilátero e isóseles).

## 🔧 Requisitos de instalación

Asegúrate de tener instalado **Python 3.8 o superior**. Comprueba su versión ejecutando en el CLI:
```bash
python --version
```

Luego, instala las dependencias necesarias con:
```bash
pip install pytest hypothesis
```

## ▶️ ¿Cómo ejecutar las pruebas?
Para correr todas las pruebas, usa:

````bash
pytest
````
Para correr un archivo específico:
````bash
pytest [nombre_del_archivo_a_ejecutar].py
````

Se puede añadir la opción `-v` para ver más detalles:
````bash
pytest -v
````
## 📁 Estructura del repositorio.
```
.
├── practica1/
│   └── operaciones/
│   │   └── operaciones.py       # Funciones de operaciones matemáticas
│   │   └── test_operaciones.py  # Pruebas con Pytest para las operaciones
│   │   └── test_operaciones_hypo.py # Pruebas con Hypothesis para operaciones
│   └── rentaAuto/
│   │   └── rentaAuto.py             # Lógica de validación de renta de auto
│   │   └── test_rentaAuto_hypo.py # Pruebas con Hypothesis de renta de auto
│   │   └── test_rentaAuto.py   # Pruebas con Pytest para renta
└── practica2/
│   └── descuento/
│   │   └── descuentos.py       # Aplicar de descuento en base al tipo de cliente y monto de compra
│   │   └── test_operaciones_para.py # Pruebas con Parametrize para probar descuentos
│   └── passwd/
│   │   └── passwords.py             # Lógica de validación de contraseña segura
│   │   └── test_passwords_hypo.py   # Pruebas con Hypothesis para validar contraseñas
│   └── prestamo/
│   │   └── prestamos.py             # Lógica de validación de préstamo
│   │   └── test_prestamos_hypo.py   # Pruebas con Hypothesis para validar préstamos
│   └── triangulo/
│   │   └── triangulos.py             # Lógica de validación de triángulos ingresando sus lados
│   │   └── test_triangulos_hypo.py   # Pruebas con Hypothesis para validar triángulos
│   │   └── test_triangulos.py        # Pruebas con Pytest para validar triángulos
│   |   └── test_triangulos_parametrize.py # Pruebas con Parametrize para validar triángulos
└── README.md
```
## 🧪 Tipos de pruebas implementadas
El proyecto utiliza dos enfoques de pruebas automatizadas:
- ✅ Pruebas basadas en ejemplos (`pytest.mark.parametrize`):
      Prueban casos concretos y límites específicos, como edades exactas que activan o no una tarifa extra.

- 🔁 Pruebas basadas en propiedades (`hypothesis`)
      Generan múltiples entradas aleatorias para verificar que las funciones siempre cumplen ciertas propiedades lógicas.

