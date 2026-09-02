import { Component, signal } from '@angular/core';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-raiz', // Es el que le da nombre a la etiqueta html del componente
  imports: [RouterOutlet],
  templateUrl: './app.html',
  styleUrl: './app.scss'
})

// Clase del componente, ídem laravel, la clase da la lógica y la plantilla la vista
export class App {
  protected readonly title = signal('primera-app-angular');
  protected readonly saludo = signal('Hola Sugey. Te amo.');
}
