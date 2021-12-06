import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConvertWeightComponent } from './convert-weight.component';

describe('ConvertWeightComponent', () => {
  let component: ConvertWeightComponent;
  let fixture: ComponentFixture<ConvertWeightComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ConvertWeightComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ConvertWeightComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
