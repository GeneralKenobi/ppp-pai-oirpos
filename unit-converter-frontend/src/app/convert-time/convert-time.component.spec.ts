import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConvertTimeComponent } from './convert-time.component';

describe('ConvertTimeComponent', () => {
  let component: ConvertTimeComponent;
  let fixture: ComponentFixture<ConvertTimeComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConvertTimeComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConvertTimeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
