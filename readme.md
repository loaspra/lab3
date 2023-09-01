# Gateway de autenticacion con JWT


---

Authentication.py

Este script es el encargado de manejar la autenticacion de los usuarios, para ello se ha definido un endpoint /login el cual recibe como parametros
un username y un password, si el usuario y la contraseña son validos se genera un token con el nombre de usuario y una fecha de expiracion, este token
es enviado en la respuesta del endpoint, si las credenciales son invalidas se envia un mensaje de error en formato JSON con un codigo de error 401.

Se ha definido otro endpoint /verify el cual recibe como parametro el token, este endpoint se encarga de verificar el token con la clave secreta y el
algoritmo usado, si el token es valido se devuelve el nombre de usuario en formato JSON, si el token es invalido o ha expirado se envia un mensaje de
error con un codigo de error 401.

para poder ejecutar este script en un contenedor se debe ejecutar el siguiente comando:

```bash
docker build -t authentication .
docker run -d -p 5003:5003 --name authentication_microservice authentication
```

---

Gateway.py

Este script es el encargado de manejar las peticiones a los microservicios, para ello se ha definido un endpoint /login el cual recibe como parametros
un username y un password, si el usuario y la contraseña son validos se genera un token con el nombre de usuario y una fecha de expiracion, este token
es enviado en la respuesta del endpoint, si las credenciales son invalidas se envia un mensaje de error en formato JSON con un codigo de error 401.

Se ha definido otro endpoint /verify el cual recibe como parametro el token, este endpoint se encarga de verificar el token con la clave secreta y el
algoritmo usado, si el token es valido (en este caso, solo se valida que sea un solo usuario hardcodeado) se devuelve el nombre de usuario en formato JSON, si el token es invalido o ha expirado se envia un mensaje de
error con un codigo de error 401.

para poder ejecutar este script en un contenedor se debe ejecutar el siguiente comando:

La actividad 1 por si sola se encuentra en la carpeta **actividad1**, en **NodeJS**. Correr el archvio **app.js**. 
```bash
docker build -t gateway .
docker run -d -p 5000:5000 --name gateway_microservice gateway
```