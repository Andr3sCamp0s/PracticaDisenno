# Bitácora de la práctica

Estudiante:
Carné:

> Cómo se llena cada entrada, en este orden y sin saltarse pasos:
>
> 1. **Predicción** — escríbala ANTES de correr nada. Qué cree que va a
>    pasar y por qué. Equivocarse aquí y entender después vale más que
>    acertar; no vuelva a corregirla.
> 2. **Observación** — corra el experimento de la etapa y pegue la salida.
> 3. **Explicación** — por qué pasó lo que pasó, en sus palabras, citando
>    **su** archivo y **su** línea (`servicio.py:24`).
> 4. **Sello** — corra `python herramientas/marcador.py` al cerrar la
>    etapa y pegue el sello que imprime.

## Etapa 0 — Diagnóstico

**Predicción:**
Pienso que se van a incumplir los 11 principios por la naturaleza de la practica, por lo que hare un buen analisis para tratar de encontrar al menos una violacion a cada uno de los 11

**Observación:**
```
....                                                                                                           [100%]
4 passed in 0.04s

```

**Explicación:**
Las 4 pruebas pasaron lo que quiere decir que mi tabla esta completa y redactada de buena manera en `tablas.py:1`.

**Sello:**
9782c5acba7eec48

## Etapa 1 — Dividir y conquistar, cohesión

**Predicción:**
La clase ServicioRecetas actualmente tiene 6 responsabilidades:
Valida el formato de las cedulas
Calculos financieros de las recetas
Manejo de bitacora dentro de la base de datos
Counicacion con la red HTTP
Control de la cache mutable
Exportacion de texto a los archivos del sistema 

Pienso que voy a necesitar unos 7 archivos, uno por cada funcionalidad y otro que llame a los metodos de los otros archivos

**Observación:**

```
.......                                                                                                        [100%]
7 passed in 0.06s

```

**Explicación:**
Cree las 3 carpetas, al principio fallo la prueba porque se me habia olvidado crear infraestructura y aplicacion, pero lo corregi rapidamente, dentro dominio cree los errores, las clases en `modelos.py:5` y un par de funciones rapidas que validan una cedula y otra que calcula recargo en `reglas.py:15`.

**Sello:**
3aa416a64f45ffda

## Etapa 2 — Reducir el acoplamiento

**Predicción:**
Al alterar vigencia_dias en CONFIG cambiándolo a 1, predigo que se afectará directamente el cálculo de las fechas de vencimiento de las recetas emitidas. Ya que la informacion entre las funciones va a ser erronea rompiendo la logica del codigo.
Yo digo que el archivo va a cambiar en 2 lugares, en la expiracion de la receta y calcular la tarifa.

5min despues*

Luego de contarlos me di cuanta que no aprecie un elemento, el calculo de la tarifa duplicada por riesgo, por lo que en realidad cambio en 3 lugares

**Observación:**

```

.....                                                                                         [100%]
5 passed in 0.03s

```

**Explicación:**
Nada mas tuve que crear la funcion de emitir dentro de servicio en `servicio.py:9`, solo la hice que retornara un diccionario ya que no me pidieron que le pusiera logica al cuerpo de la funcion asi que quedo como solo un return. Por otro lado me toco modificar dentro de reglas la funcion de calcular tarifa en `reglas.py:15` para que los parametros no fuera variables globales que pudieran ser cambiadas.

**Sello:**
ac1da5c02588b26a

## Etapa 3 — Abstracción y reuso

**Predicción:**
Me salieron 2 coincidencias, creo que vamos a poder bajarlo hasta 0 porque de eso se trata el ejercicio, vamos a ver como nos va
**Observación:**

```


.......                                                                                       [100%]
7 passed in 0.04s

```

**Explicación:**
Quitamos los JSON externos y las librerias para usar los puertos en `puertos.py:4`, los cuales no tienen el riesgo de infectar el codigo. Hicimos que la cedula se valide a si misma con un metodo interno en `modelos.py:8` ademas de ahora EmisionDeRecetas ahora devuelve un objeto de tipo despacho en `servicio.py:6`, modificando la version vieja que hice que solo devolvia un diccionario, asi los evitamos.

Despues de correr el sello me di cuenta que habia roto la etapa 1 por poner un datetime.now(), pero luego lo corregi y ahora ya estan bien las 2, se me habia olvidado ese detalle, ahora la fecha debe de venir por el puerto que acabamos de crear en `puertos.py:6`.

**Sello:**
6abac9074fcdd7ee

## Etapa 4 — Flexibilidad, obsolescencia y portabilidad

**Predicción:**
Pienso que no tiene porque fallar, como se habian eliminado los condicionales el sistema no tiene porque buscar exactamente la nueva cadena, si no mas bien este al venir de afuera lo que hace es que agrega el nuevo proveedor, me refiero al caso de uso central que se habia hecho en servicio.py

**Observación:**

```

.......                                                                                       [100%]
7 passed in 0.05s

```

**Explicación:**
En esta etapa logramos que el sistema sea completamente flexible eliminando los condicionales rígidos que estaban amarrados a los nombres de las farmacias. Ahora, EmisionDeRecetas recibe un mapa dinámico desde afuera y busca la pasarela correspondiente en `servicio.py:14`. Esto se probó con éxito con la cadena fantasma FarmaViva, la cual funcionó a la primera sin tener que escribir su nombre en el código del servicio médico. Toda la configuración de infraestructura como rutas y URL ahora entran de forma limpia mediante variables de entorno a través del archivo `arranque.py:5`.

**Sello:**
06b2e59868a2fec6

## Etapa 5 — Testabilidad

**Predicción:**
El código de fijo va a crashear de inmediato o se va a quedar colgado en un ciclo infinito al intentar conectar con un servidor externo del cual no tengo control.

Pensaria que para ejecutar esa única línea de negocio, necesita tocar 4 cosas:
Conexión a Internet
 Servidores externos de las farmacias (HTTP).
Archivos con los permisos para escribir en la base de datos.
El reloj físico de la CPU de la compu.

**Observación:**

```

.......                                                                                       [100%]
7 passed in 0.03s


```

**Explicación:**
En esta etapa logramos que el sistema sea completamente testable desde un programa externo. Al inyectar obligatoriamente por constructor las pasarelas, el reloj, el generador de folios y la bitácora en `servicio.py:6`, ganamos el control total. Además, creamos nuestras propias pruebas unitarias dentro de la carpeta mis_pruebas en `test_testabilidad.py:20` para ver tres escenarios críticos que antes eran imposibles de testear en el legado viejo: el cálculo exacto de la vigencia a 30 días fijando el tiempo, la simulación de una pasarela externa caída y el bloqueo inmediato de recetas inválidas desde el modelo.

**Sello:**
3760bd44f0564739

## Etapa 6 — Diseño defensivo

**Predicción:**
Pienso que en la corrida con python normal el programa detecta el error mediante el condicional e interrumpe la ejecución lanzando un AssertionError.
En cambio en la corrida optimizada python elimina por completo todas las líneas que contengan assert, por lo que la validación se apaga por completo, el sistema ignora que los días están en cero y procesa una receta corrupta con info basura en la base de datos.

Como dije en el diagnostico usar assert para validar datos de entrada externos no es lo mas recommended ya que en produccion se pueden hacer pruebas optimizados y pues eso puede traer problemas.

**Observación:**

```

...........                                                                                   [100%]
11 passed in 2.04s

```

**Explicación:**
En esta etapa logramos que el sistema sea completamente seguro dividiendo el código en dos zonas. Usamos Pydantic en la entrada mediante `SolicitudReceta` en `borde.py:5` para frenar la basura antes de que toque el cerebro del hospital. Gracias a esto, blindamos el sistema contra informacion erronea y datos basura en `servicio.py:20` que puedan afectar el programa.

**Sello:**
682b6b13064f791d

## Cierre — Los principios en conflicto

Nombre dos principios que se estorbaron entre sí en SU rediseño, y con qué
criterio resolvió el conflicto. Cite el archivo donde se ve la decisión.

**Conflicto 1:**
El Principio 4 (Nivel de abstracción) y el Principio 6 (Reusar lo que existe) chocaron en `borde.py:7`. Pydantic nos pide reglas fijas para la web, y eso iba a ensuciar nuestro código limpio del hospital. Lo resolví usando el criterio de separar las zonas: Pydantic frena la basura en la entrada de la aplicación en `borde.py:7` y luego convertimos todo a objetos limpios del dominio mediante la función en `borde.py:15`.

**Conflicto 2:**
El Principio 7 (Flexibilidad) y el Principio 11 (Diseño defensivo) chocaron en `servicio.py:13`. Al hacer el sistema flexible con un mapa dinámico para meter cualquier farmacia sin tocar el código, nos arriesgábamos a que alguien pidiera una farmacia que no existe y el programa fallara en silencio devolviendo un nulo. Lo resolví con el criterio de fallar rápido: el servicio busca la clave en el mapa en `servicio.py:13` y si no está, tira de una vez el error `CadenaNoSoportada` en `servicio.py:14`.

