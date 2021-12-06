import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { StatusComponent } from './status/status.component';
import { FindPrefixComponent } from './find-prefix/find-prefix.component';
import { ConvertLengthComponent } from './convert-length/convert-length.component';
import { ConvertWeightComponent } from './convert-weight/convert-weight.component';
import { ConvertTimeComponent } from './convert-time/convert-time.component';

const routes: Routes = [
  { path: 'status', component: StatusComponent },
  { path: 'find-prefix', component: FindPrefixComponent },
  { path: 'convert-length', component: ConvertLengthComponent },
  { path: 'convert-weight', component: ConvertWeightComponent },
  { path: 'convert-time', component: ConvertTimeComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
