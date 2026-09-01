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
- Instalación de proyecto:   dexecit node:22.22.0-slim npx @angular/cli@latest new curso-angular-demo --routing --style=scss
- Levantamiento de servidor: dportit 4200 node:22.22.0-slim npx ng serve --host 0.0.0.0