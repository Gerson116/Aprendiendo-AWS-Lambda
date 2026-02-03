# Laboratorio Lambda

## 🎯 **Objetivo del Laboratorio**

- Crear una **APY GATEWAY** que integre 3 lambdas.
- Cada lambda debe simular el comportamiento REST, donde

---

## 📚 **Paso 1: Crear el bucket S3**

- Crea un archivo controlador (handler) en tu lenguaje de programación que desees que contenga el código para:
  - Definir un **contador** fuera del `lambda_handler`(o la función que definas que va a gestionar cada invocación lambda) para mantener su valor en _invocaciones calientes_.
  - El contador aumentará en 1 por cada invocación mientras que la lambda esté caliente.
  - Retornar el valor del contador con el mensaje "Está haciendo frío, ¿no?" si la lambda está en estado "cold start".

---

## 📚 **Paso 2: Crear los archivos ZIP para los lambdas**

- Comprimir las carpetas que contienen los lambdas y subirlos al S3

---

## 📚 **Paso 3: Desplegar los lambdas**

- Desplegar los lambdas usando AWS CLI

---

## 📚 **Paso 4: Crear un API GATEWAY con Cloud formation y integrar los lambdas que desplegue**

- Crear API GATEWAY y integrarlo con los lambdas que desplegue.

---

## 📚 **Paso 5: Crear un API GATEWAY con Cloud formation y integrar los lambdas que desplegue**

- Agregar Open API al apigateway, para manejar los datos que serán enviados.

---
## 📚 **Paso 6: Probar la Lambda URL**
- Realiza varias invocaciones a la Lambda URL creada.
- Observa y anota el comportamiento del contador en cada invocación.