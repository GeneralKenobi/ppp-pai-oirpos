import { Component, OnInit } from '@angular/core';
import {FormGroup, FormControl, Validators} from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-convert-length',
  templateUrl: './convert-length.component.html',
  styleUrls: ['./convert-length.component.scss']
})
export class ConvertLengthComponent implements OnInit {
  valueFormControl = new FormControl('', [Validators.pattern('[0-9]*(\\.[0-9]+)?')]);
  fromFormControl = new FormControl('meter');
  toFormControl = new FormControl('meter');
  result = ''

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }

  inputChanged(): void {
    if(!this.valueFormControl.valid) {
      this.result = '';
      return;
    }

    if (this.fromFormControl.value === this.toFormControl.value) {
      this.result = this.valueFormControl.value;
      return
    }

    let uri = `/v1/convert/length?value=${this.valueFormControl.value}&fromUnit=${this.fromFormControl.value}&toUnit=${this.toFormControl.value}`;

    this.http.get<ConversionResult>(uri)
      .subscribe((data: ConversionResult) => {
        this.result = `${(Math.round(data.value * 1000) / 1000).toFixed(3)}`;
      })
  }
}

export interface ConversionResult {
  value: number
}
