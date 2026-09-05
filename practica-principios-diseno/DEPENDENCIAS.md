# Dependencias externas

Una fila por dependencia externa que el proyecto usa hoy, incluidas las de
la práctica. Complete las cuatro columnas: sin ruta de salida, la
dependencia es un compromiso indefinido.


| Dependencia | Versión acotada | Licencia | Riesgo | Ruta de salida |
| :--- | :--- | :--- | :--- | :--- |
| **pytest** | `^9.1.1` | MIT | Bajo. Es una herramienta exclusiva de desarrollo y pruebas locales. | Mantener actualizada o migrar al módulo nativo `unittest` de Python. |
| **pydantic** | `^2.0.0` | MIT | Medio. Si cambia su API principal, obliga a reescribir validadores del borde. | Migrar a los componentes nativos `dataclasses` incorporados en Python. |
| **urllib3** | `^2.0.0` | MIT | Alto. El proveedor de red puede quedar obsoleto o presentar fallas de seguridad. | Migrar a la librería moderna `requests` o al cliente asíncrono `httpx`. |

