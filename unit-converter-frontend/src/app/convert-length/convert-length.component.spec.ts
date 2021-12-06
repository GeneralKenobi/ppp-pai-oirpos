import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConvertLengthComponent } from './convert-length.component';

describe('ConvertLengthComponent', () => {
  let component: ConvertLengthComponent;
  let fixture: ComponentFixture<ConvertLengthComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConvertLengthComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConvertLengthComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
