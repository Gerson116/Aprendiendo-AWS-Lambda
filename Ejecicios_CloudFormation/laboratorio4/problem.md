# Laboratorio Lambda

## 🎯 **Objetivo del Laboratorio**

- Crear una **APY GATEWAY** que integre 3 lambdas.
- Cada lambda debe simular el comportamiento REST, donde

---

## 📚 **Paso 1: Crear el bucket S3**

- Crear un S3 que contendrá todos los zips de los lambdas y las plantillas de Open API
- Dentro del bucket deben existir dos carpetas:
-   **Deploy** -> contendra los zips de los lambdas
-   **OpenAPITemplate** -> contendra los Open API template de los lambdas.

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

## 📚 **Paso 6: Subir el Open API al bucket**

- Al crear la plantilla Open API, debo enviar la misma al S3 par areferenciarla en mi plantilla API Gateway

---

## 📚 **Paso 7: Probar la Lambda URL**
- Realiza varias invocaciones a la Lambda URL creada.
- Observa y anota el comportamiento del contador en cada invocación.


---

## 📚 **Paso 8: Hacer que el servicio se alcance desde cualquier pais usando el servicio: AWS API Gateway Deployment**
- Investigar sobre este servicio y implementarlo

---

## 📚 **Paso 9: Probar la Lambda URL**
- Realiza varias invocaciones a la Lambda URL creada.
- Observa y anota el comportamiento del contador en cada invocación.


---

## 📚 **Paso 10: Integrar AWS Proxy**
- Investigar sobre este servicio y implementarlo

---

## 📚 **Paso 11: Probar la Lambda URL**
- Realiza varias invocaciones a la Lambda URL creada.
- Observa y anota el comportamiento del contador en cada invocación.


---