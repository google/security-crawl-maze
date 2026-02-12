import {Component, ChangeDetectionStrategy} from '@angular/core';

@Component({
  changeDetection: ChangeDetectionStrategy.Eager,standalone: false,
  selector: 'event-handler-navigation',
  template: `
    <h1>Event Handler Navigation</h1>
  `,
})
export class EventHandlerComponent {
}
