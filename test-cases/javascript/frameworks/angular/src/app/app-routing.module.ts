import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';

import {EventHandlerComponent} from './event-handler/event-handler.component';
import {RouterOutletComponent} from './router-outlet/router-outlet.component';


const routes: Routes = [
  {path: 'event-handler.found', component: EventHandlerComponent},
  {path: 'router-outlet.found', component: RouterOutletComponent},
];

@NgModule({
  declarations: [EventHandlerComponent, RouterOutletComponent],
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
