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
Las 4 pruebas pasaron lo que quiere decir que mi tabla esta completa y redactada de buena manera

**Sello: 9782c5acba7eec48**

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
Cree las 3 carpetas, al principio fallo la prueba porque se me habia olvidado crear infraestructura y aplicacion, pero lo corregi rapidamente, dentro dominio cree los errores, las clases y un par de funciones rapidas que validan una cedula y otra que calcula recargo.

**Sello:3aa416a64f45ffda**

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
Nada mas tuve que crear la funcion de emitir dentro de servicio, solo la hice que retornara un diccionario ya que no me pidieron que le pusiera logica al cuerpo de la funcion asi que quedo como solo un return. Por otro lado me toco modificar dentro de reglas la funcion de calcular tarifa para que los parametros no fuera variables globales que pudieran ser cambiadas

**Sello: ac1da5c02588b26a**

## Etapa 3 — Abstracción y reuso

**Predicción:**
Me salieron 2 coincidencias, creo que vamos a poder bajarlo hasta 0 porque de eso se trata el ejercicio, vamos a ver como nos va
**Observación:**

```


.......                                                                                       [100%]
7 passed in 0.04s

```

**Explicación:**
Quitamos los JSON externos y las librerias para usar los puertos, los cuales no tienen el riesgo de infectar el codigo. Hicimos que la cedula se valide a si misma con un metodo interno ademas de ahora EmisionDeRecetas ahora devuelve un objeto de tipo despacho, modificando la version vieja que hice que solo devolvia un diccionario, asi los evitamos.

Despues de correr el sello me di cuenta que habia roto la etapa 1 por poner un datetime.now(), pero luego lo corregi y ahora ya estan bien las 2, se me habia olvidado ese detalle, ahora la fecha debe de venir por el puerto que acabamos de crear

**Sello: 6abac9074fcdd7ee**

## Etapa 4 — Flexibilidad, obsolescencia y portabilidad

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Etapa 5 — Testabilidad

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Etapa 6 — Diseño defensivo

**Predicción:**

**Observación:**

```
```

**Explicación:**

**Sello:**

## Cierre — Los principios en conflicto

Nombre dos principios que se estorbaron entre sí en SU rediseño, y con qué
criterio resolvió el conflicto. Cite el archivo donde se ve la decisión.

**Conflicto 1:**

**Conflicto 2:**
