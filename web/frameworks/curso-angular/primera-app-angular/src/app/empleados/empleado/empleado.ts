import { Component } from '@angular/core';

@Component({
  selector: 'app-empleado',
  imports: [],
  // Permite la simplificación de componentes incluyendo lógica y vista en un archivo
  // templateUrl: './empleado.html', // Convertir el componente en inline
  // styleUrl: './empleado.scss', //Convertir el componente en inline
  template: `<p>Aquí iría un empleado</p>`,
  styles: `
  p {
      background-color: #48e;
      color: #fff;
  }
`
})
export class Empleado {}
