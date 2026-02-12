import {Component, ChangeDetectionStrategy} from '@angular/core';
import {Router} from '@angular/router';

@Component({changeDetection: ChangeDetectionStrategy.Eager,standalone: false,
            selector: 'app-root', templateUrl: './app.component.html'})
export class AppComponent {
  constructor(private readonly router: Router) {}

  navigate() {
    this.router.navigate(['/event-handler.found']);
  }
}
