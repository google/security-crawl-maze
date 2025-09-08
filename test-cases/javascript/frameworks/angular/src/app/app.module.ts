import {NgModule, provideZoneChangeDetection} from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';
import {RouterModule} from '@angular/router';

import {AppRoutingModule} from './app-routing.module';
import {AppComponent} from './app.component';

@NgModule({providers: [provideZoneChangeDetection()]})
export class ZoneChangeDetectionModule {}

@NgModule({
  declarations: [AppComponent],
  imports: [ZoneChangeDetectionModule, BrowserModule, AppRoutingModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
