# Nota de versión — Curso original vs Angular actual

Curso base: Píldoras Informáticas (Node 14.15 LTS / 15.6, ~Angular 10-12).
Desarrollo real: Angular 21, agosto 2026.

Diferencias estructurales que se traducen en cada capítulo, no se siguen
literales:
- NgModules → Standalone components (default desde Angular 17+)
- HttpClientModule → provideHttpClient() en app.config.ts
- Interceptores/guards de clase → funciones (HttpInterceptorFn, CanActivateFn)
- *ngIf/*ngFor → @if/@for (control de flujo nuevo, Angular 17+)
- Webpack → esbuild/Vite (builder por defecto desde Angular 17+)
- Sin Signals en el curso original → Signals como mecanismo de estado moderno
- Instalación global de @angular/cli → npx, sin instalar nada en el host
  (Docker + WSL2, contenedores efímeros, mismo patrón que curso-docker)

Referencia real de aplicación de estos conceptos: proyecto de prueba
técnica mh-prueba-tecnica (github.com/manuelhm1993/mh-prueba-tecnica).

### Comandos
- Instalación de proyecto:        dexecit node:22.22.0-slim npx @angular/cli@latest new curso-angular-demo --routing --style=scss
- Levantamiento de servidor:      dportit 4200 node:22.22.0-slim npx ng serve --host 0.0.0.0
- Creación de componentes:        dexec node:22.22.0-slim npx ng g c empleados
- Creación de componentes inline: dexec node:22.22.0-slim npx ng g c empleados -t -s

CONTEXTO — ARQUITECTURA SPA Y BOOTSTRAP (ANGULAR 11 VS 21)
Versión: 1.0 · Fecha: Septiembre 2026
Objetivo: Documentar las bases físicas del modelo Single Page Application y la mutación arquitectónica del motor de arranque de Angular.
═══════════════════════════════════════════════════════════════════

1. EL MODELO SPA (SINGLE PAGE APPLICATION) Y AJAX
───────────────────────────────────────────────────────────────────
La ley física inmutable de la web moderna. A diferencia de las webs tradicionales que recargan toda la página por cada clic, una SPA funciona así:

1. **Carga Inicial (El Lienzo):** El navegador del cliente hace una única petición HTTP al servidor y descarga el `index.html` (un cascarón vacío) junto con el bundle de JavaScript (Angular).
2. **Interactividad (El Tráfico):** A partir de ese momento, el navegador no vuelve a pedir HTML. Angular intercepta los clics y utiliza `HttpClient` (la evolución moderna de AJAX) para comunicarse con el servidor (APIs).
3. **Intercambio (JSON):** El servidor responde únicamente con datos puros en formato JSON.
4. **Renderizado (DOM):** Angular toma ese JSON y repinta dinámicamente solo las partes necesarias de la pantalla, logrando una velocidad instantánea sin parpadeos.

═══════════════════════════════════════════════════════════════════

2. LA MUTACIÓN DEL FLUJO DE ARRANQUE (BOOTSTRAP)
───────────────────────────────────────────────────────────────────
Angular eliminó al intermediario burocrático (NgModules) para lograr un arranque directo y estéril.

* **Angular 11 (La Burocracia):** 
  `main.ts` -> Compila el motor -> Invoca a `AppModule` (revisa dependencias, declaraciones, imports) -> Inyecta el `AppComponent` en el DOM.
* **Angular 21 (La Ejecución Directa):** 
  `main.ts` -> Ejecuta nativamente `bootstrapApplication(AppComponent, appConfig)` -> Inyecta el `AppComponent` en el DOM pasándole las configuraciones globales al vuelo. Es el equivalente exacto a la limpieza del `index.php` en Laravel.

═══════════════════════════════════════════════════════════════════

3. TABLA COMPARATIVA: EL CHOQUE DE VERSIONES
───────────────────────────────────────────────────────────────────
| Fase del Arranque | 🏛️ Angular 11 (Curso 2021) | 🚀 Angular 21 (Tu Realidad 2026) |
| :--- | :--- | :--- |
| **Punto de Entrada** | `main.ts` compila el motor e invoca a `AppModule`. | `main.ts` invoca nativamente a `bootstrapApplication()` apuntando directo al componente. |
| **El Intermediario** | `app.module.ts` (Módulo Raíz). Actuaba como una aduana, registrando cada componente, servicio y ruta de forma obligatoria. | **Destruido**. La aduana ya no existe; los componentes son *Standalone* (autónomos) por defecto. |
| **La Configuración** | Vivía incrustada dentro del decorador `@NgModule` en forma de arrays masivos (`declarations`, `imports`, `providers`). | Extraída a un archivo estéril e independiente: `app.config.ts`. |
| **Motor de Red** | Importación global de `HttpClientModule` acoplado al módulo raíz. | Inyección funcional y global mediante `provideHttpClient()` en la configuración. |