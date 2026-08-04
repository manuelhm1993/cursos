# Lista de principios, paradigmas, patrones y síndromes

Este documento establece el marco teórico y mental sobre el cual se construyen y operan los proyectos de la organización. 

---

## 1. Principios de Diseño

### SOLID
Un acrónimo de cinco principios fundamentales de diseño orientado a objetos que hacen el software más comprensible, flexible y mantenible.

* **S - Single Responsibility Principle (SRP):** Una clase o módulo debe tener una, y solo una, razón para cambiar.
    * *Ejemplo:* En mi bot de Python, una clase `Usuario` solo debe manejar los datos del usuario. Si necesito enviar un correo de bienvenida, creo una clase separada `EmailService`.
* **O - Open/Closed Principle (OCP):** El software debe estar abierto a extensión, pero cerrado a modificación.
    * *Ejemplo:* Mi clase `ProcesadorPagos` que acepta PayPal, para agregar Stripe no modifico la clase original llena de *If-Else*, sino que creo una interfaz `IPago` y extiendo con una nueva clase `StripePago`.
* **L - Liskov Substitution Principle (LSP):** Las clases derivadas deben poder sustituir a sus clases base sin romper la ejecución del programa.
    * *Ejemplo:* Mi clase base `Ave` con el método `volar()`, crear una clase `Pinguino` que herede de `Ave` violará este principio (porque los pingüinos no vuelan).
* **I - Interface Segregation Principle (ISP):** Es mejor tener muchas interfaces pequeñas y específicas que una interfaz general y enorme. (Sin prefijo "I" explícito en lenguajes como Python).
    * *Ejemplo:* En lugar de una interfaz `ITrabajador` con `trabajar()` y `comer()` (que obligaría a un robot a implementar `comer()`), separas en `ITrabajable` y `IComible`.
* **D - Dependency Inversion Principle (DIP):** Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones.
    * *Ejemplo:* La clase `Controlador` no instancia directamente `BaseDeDatosMySQL`, sino que recibe por inyección de dependencias una interfaz genérica `IConexionDB`. Esto facilita los *Mocks* en Testing.

### KISS (Keep It Simple, Stupid)
Establece que la mayoría de los sistemas funcionan mejor si se mantienen simples en lugar de hacerlos complejos. La simplicidad debe ser un objetivo clave del diseño y se debe evitar la complejidad innecesaria.
* *Ejemplo real:* Cuando quise descargar los SVGs de los logos, subirlos por FTP y referenciarlos manualmente solo para tener íconos en tus Badges del README. La solución KISS fue usar el generador de *Shields.io* sin logo para mantener el código mantenible.

### YAGNI (You Aren't Gonna Need It)
Principio de la programación extrema que dicta que no debes agregar funcionalidad al software hasta que no sea estrictamente necesario.
* *Ejemplo real:* Intentar configurar Traefik, PostgreSQL y Redis para arrancar n8n en local por primera vez. No se necesita una arquitectura masiva para aprender flujos de trabajo; con SQLite y Docker es suficiente. Se construye para hoy, no para escenarios hipotéticos del futuro.

### The Zen of Python (Tim Peters)
Filosofía de diseño fundamental que guía el desarrollo idiomático en Python (extraída directamente con `import this`):

```bash
mhenriquez@MHenriquez:~$ python
Python 3.12.3 (main, Jun 19 2026, 12:46:00) [GCC 13.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
>>>
```

---

## 2. Paradigmas de Programación

### OOP (Object Oriented Programming)
Paradigma que organiza el diseño de software en torno a datos u objetos, en lugar de funciones y lógica. Modela entidades del mundo real usando cuatro pilares:
1.  **Abstracción:** Ocultar la complejidad y mostrar solo lo esencial.
2.  **Encapsulamiento:** Proteger los datos de un objeto (usando `__atributos` privados o *protected* en Python/Java) modificándolos solo a través de métodos (Getters/Setters).
3.  **Herencia:** Crear nuevas clases a partir de clases existentes, promoviendo la reutilización de código.
4.  **Polimorfismo:** Diferentes objetos respondiendo al mismo método de manera específica.

* *Ejemplo:* En mi sistema de Tkinter, se modela una clase base `VentanaBase`, y a partir de ahí se crean `VentanaLogin` y `VentanaDashboard` que heredan sus propiedades pero aplican polimorfismo en sus métodos de pintado.

---

## 3. Patrones de Diseño Arquitectónico

### MVC (Model-View-Controller)
Patrón de arquitectura de software que separa los datos de una aplicación, la interfaz de usuario, y la lógica de control en tres componentes distintos.
1.  **Model (Modelo):** La fuente de verdad. Accede y gestiona la base de datos (Ej. Eloquent en Laravel).
2.  **View (Vista):** La interfaz visual. Es "tonta", no procesa lógica, solo pinta datos (Ej. Blade/Tailwind o los *Widgets* en Tkinter).
3.  **Controller (Controlador):** El cerebro intermediario. Recibe la petición de la vista, busca la data en el modelo, y se la devuelve a la vista para renderizar.

* *Ejemplo:* Un usuario hace clic en "Ver Perfil" (Vista) -> Llega la ruta al `UserController` (Controlador) -> Éste pide `User::find(1)` (Modelo) -> El Controlador envía la data de vuelta a la `perfil.blade.php` (Vista).

---

## 4. Síndromes del Desarrollador

### Síndrome del Objeto Brillante
Es la tendencia constante de un desarrollador a distraerse y abandonar tecnologías, frameworks o proyectos a la mitad en favor de la "nueva y brillante" herramienta del mercado (Ej. Querer abandonar PHP/Laravel por Rust o Go sin haber dominado primero las bases de la ingeniería de software). El antídoto es el rigor, la hoja de ruta y cerrar hitos.

### Síndrome del Impostor
Experiencia psicológica mediante la cual un profesional siente que no está a la altura de las circunstancias y teme ser expuesto como un "fraude", a pesar de tener evidencia objetiva empírica (repositorios, despliegues, años de experiencia) de su competencia. 
* *Mi Antídoto del Arquitecto:* Entender que buscar en la documentación oficial, revisar StackOverflow o consultar a una IA para armar una estructura no me hace menos programador; te hace un ingeniero que sabe utilizar las herramientas de su época.