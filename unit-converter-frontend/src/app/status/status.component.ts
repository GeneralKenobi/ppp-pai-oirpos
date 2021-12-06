import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-status',
  templateUrl: './status.component.html',
  styleUrls: ['./status.component.scss']
})
export class StatusComponent implements OnInit {
  public status: string = 'Not responding'

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
    this.http.get<Status>('/v1/status')
      .subscribe((data: Status) => {
        this.status = data.message;
      })
  }

}

export interface Status {
  message: string;
}
