# Diagnóstico del código de partida

Lea `clinicasegura/legado.py` entero antes de escribir una sola línea de
código nuevo. Llene una fila por principio. En la columna de evidencia
cite **archivo y línea** (por ejemplo `legado.py:38`); una fila sin
evidencia no cuenta.

Si cree que un principio **no** está violado, escriba la fila igual y
explique por qué en la columna de hallazgo.

| # | Principio | Hallazgo concreto | Evidencia (archivo:línea) | Qué cuesta si no se corrige |
|---|-----------|-------------------|---------------------------|------------------------------|
| 1 | Dividir y conquistar | La clase ServicioRecetas hace todo el trabajo sola: valida, cobra, usa la red, escribe la BD y exporta. | legado.py:34-152 | Cualquier cambio obliga a tocar y poner en riesgo la única clase central. |
| 2 | Aumentar la cohesión | Los métodos mezclan tareas que deberian estar desconectadas. emitir procesa dinero, maneja SQL y ejecuta llamadas HTTP. | legado.py:42-96 | El código se vuelve un enredo difícil de entender, mantener y de separar ante fallas especificas. |
| 3 | Reducir el acoplamiento | El módulo entero depende de variables globales en memoria CONFIG y CACHE_PACIENTES. | legado.py:23-31 | Cualquier función puede alterar el estado y arruinar otras partes del sistema. |
| 4 | Mantener alta la abstracción | El método emitir mezcla lógica de alto nivel como las tarifas con código de bajo nivel como el SQL. | legado.py:59-62, legado.py:84-88 | Quien lea las reglas de negocio tiene que pelearse obligatoriamente con la parte técnica. |
| 5 | Aumentar la reusabilidad | Los datos viajan como diccionarios y JSONs a como salgan sin nigun tipo de forma ni orden. | legado.py:42, legado.py:114, legado.py:122 | No podemos reutilizar el comportamiento de un paciente o receta en otra pantalla sin tenr que copiar todo el bendito JSON. |
| 6 | Reusar lo existente | El método validar_cedula revisa guiones y números uno por uno a mano. | legado.py:129-142 | Desperdiciamos tiempo manteniendo algoritmos caseros que Python ya resuelve con funciones del lenguaje. |
| 7 | Diseñar para la flexibilidad | Usar un if/elif tieso con texto quemado para decidir a qué farmacia enviar la receta. | legado.py:65-80 | Para agregar una farmacia nueva en el futuro estamos obligados a modificar el codigo |
| 8 | Anticipar la obsolescencia | Depende de librerías nativas directas de red urllib, request dentro de los metodos. | legado.py:102, legado.py:118 | Si queremos migrar a otra libreria mejor, hay que reescribir todo el dominio de nuevo. |
| 9 | Diseñar para la portabilidad | El método exportar usa una ruta física que solo sirve en windows a lo que leí | legado.py:144 | El sistema va a crashear de inmediato si intentamos correrlo en servidores Linux o derivados. |
| 10 | Diseñar para la testabilidad | El código tiene el reloj del sistema datetime.now y el azar random.randint incrustados directamente. | legado.py:49, legado.py:52 | No podemos predecir los resultados en un test unitario porque el folio y las fechas cambian siempre o son aleatorios. |
| 11 | Diseñar defensivamente | Usa sentencias assert para validar datos del cliente y se traga a la fuerza errores críticos de BD con un pass. | legado.py:46-47, legado.py:88 | Si los asserts se apagan, entra basura y los fallos se ocultan en silencio. |

