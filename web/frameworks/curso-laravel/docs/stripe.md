# INTEGRACIÓN STRIPE SANDBOX: FASE 1 A 3

El SDK oficial no aparece en el panel principal porque Stripe prioriza la documentación de su API REST pura. Los comandos de instalación residen en la sección "Libraries" de su documentación o directamente en su repositorio oficial.

## Fase 1: Infraestructura Backend (Laravel)
Ejecuta la instalación en tu terminal de WSL2 utilizando tu contenedor efímero de Composer para mantener la regla de cero contaminación.

```bash
dexec composer:2.9.4 composer require stripe/stripe-php
```

Abre tu archivo `.env` en la raíz del proyecto e inyecta las llaves que generaste en el panel de Sandbox (https://dashboard.stripe.com/test/apikeys):

```env
STRIPE_KEY=pk_test_tu_clave_publica_aqui
STRIPE_SECRET=sk_test_tu_clave_secreta_aqui
```

## Fase 2: Infraestructura Frontend (Vue 3)
*(Ajuste de arquitectura: El texto que citaste mencionaba Angular por un proyecto anterior. Tu stack activo actual es Vue 3).*
Utiliza tu contenedor efímero de Node para inyectar el SDK nativo de Stripe en tu Single Page Application:

```bash
dexec node:22.22.0-slim npm install @stripe/stripe-js
```

## Fase 3: El Túnel de Webhooks (Stripe CLI)
Tu servidor aislado en `localhost` no puede recibir notificaciones asíncronas de Stripe sin un túnel inverso. Instala el binario CLI directamente en el kernel de tu Ubuntu (WSL2):

```bash
curl -s [https://packages.stripe.dev/api/security/keypair/stripe-cli-gpg/public](https://packages.stripe.dev/api/security/keypair/stripe-cli-gpg/public) | gpg --dearmor | sudo tee /usr/share/keyrings/stripe-cli-archive-keyring.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/stripe-cli-archive-keyring.gpg] [https://packages.stripe.dev/stripe-cli-debian-local](https://packages.stripe.dev/stripe-cli-debian-local) stable main" | sudo tee -a /etc/apt/sources.list.d/stripe-cli.list
sudo apt update && sudo apt install stripe
```

Vincula tu consola local con tu cuenta de Stripe Sandbox ejecutando:

```bash
stripe login
```