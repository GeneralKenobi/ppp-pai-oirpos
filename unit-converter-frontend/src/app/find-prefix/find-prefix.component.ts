import { Component, OnInit } from '@angular/core';
import {FormGroup, FormControl, Validators} from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-find-prefix',
  templateUrl: './find-prefix.component.html',
  styleUrls: ['./find-prefix.component.scss']
})
export class FindPrefixComponent implements OnInit {
  valueFormControl = new FormControl('', [Validators.pattern('[0-9]*(\\.[0-9]+)?')]);
  unitFormControl = new FormControl('');
  result = ''

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }

  inputChanged(): void {
    if(!this.valueFormControl.valid) {
      this.result = '';
      return;
    }

    let uri = `/v1/si/prefix?value=${this.valueFormControl.value}`;
    const unit = this.unitFormControl.value;
    if (unit) {
      uri += `&unit=${unit}`
    }

    this.http.get<SiPrefix>(uri)
      .subscribe((data: SiPrefix) => {
        this.result = data.formatted ?? '';
      })
  }
}

export interface SiPrefix {
  value: number
  formatted?: string
  prefix: {
    power: number
    name?: string
    word?: string
    symbol?: string
  }
}
