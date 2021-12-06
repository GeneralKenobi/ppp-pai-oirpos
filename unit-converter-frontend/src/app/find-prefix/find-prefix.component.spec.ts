import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FindPrefixComponent } from './find-prefix.component';

describe('FindPrefixComponent', () => {
  let component: FindPrefixComponent;
  let fixture: ComponentFixture<FindPrefixComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FindPrefixComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(FindPrefixComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
