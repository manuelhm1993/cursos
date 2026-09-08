# Uso de docker, wsl2 y laravel sail

---

### Docker
Docker es un gestor de contenedores que permite ejecutar nuestra aplicación en una 
máquina virtual dentro de nuestra computadora. Permite configurar distintos servicios, 
dependencias que require nuestra app para correr.

Esto permite evitar el problema: "En mi computadora funciona". Docker permite descargar
la imagen de las distintas dependencias y sus versiones como php, mysql, composer, node,
etc... al distribuirse, se levanta el contenedor y el entorno es el mismo en cualquier
lugar, incluso al hacer deploy

---

### Laravel sail
Laravel sail permite usar docker por detrás a partir de la versión 8 de laravel, hace
una abstracción de toda la configuración de docker y permite usar comandos sencillos.
Requisitos:
- Wsl2 en caso de windows
- Ubuntu
- Docker desktop

---

### Crear un alias para sail
```bash
- echo "alias sail='sh \$( [ -f sail ] && echo sail || echo vendor/bin/sail )'" >> ~/.bashrc
- source ~/.bashrc
- sail up -d
```

### Comandos
```bash
1. Instalar laravel sail
- dexec composer:2.9.4 composer require laravel/sail --dev
- dexecit mh_php:8.3-dev php artisan sail:install

Si se está trabajando con los puertos 3306 se debe agregar esto a .env
APP_PORT=8000
FORWARD_DB_PORT=33060

- ./vendor/bin/sail up || sail up -d
- sail artisan migrate --seed
- sail npm install
- sail npm run dev
- sail stop
```

