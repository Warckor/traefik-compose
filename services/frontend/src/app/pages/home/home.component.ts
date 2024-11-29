import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ApiService } from '../../services/api.service';

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
export class HomeComponent implements OnInit {
  data: any[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    this.apiService.getData().subscribe((response) => {
      this.data = response;
    });
  }
}
