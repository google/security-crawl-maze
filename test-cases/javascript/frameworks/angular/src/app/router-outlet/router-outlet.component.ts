import {Component, ChangeDetectionStrategy} from '@angular/core';

@Component({
  changeDetection: ChangeDetectionStrategy.Eager,standalone: false,
  selector: 'router-outlet-navigation',
  template: `
    <h1>Router Outlet Navigation</h1>
  `,
})
export class RouterOutletComponent {
}
