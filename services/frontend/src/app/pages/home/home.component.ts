import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-home',
  imports: [CommonModule],
  template: `
    <h1>Datos desde el backend</h1>
    <ul>
      <li *ngFor="let item of data">{{ item }}</li>
    </ul>
  `,
  styles: [``]
})
export class HomeComponent {
  data: any[] = [];

  constructor() {}

  }
