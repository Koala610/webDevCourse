import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { ProductItemComponent } from './product-item/product-item.component';
import { CategoryComponent } from './category/category.component';
import { ProductListComponent } from './product-list/product-list.component';
<<<<<<< HEAD
import { AppMainComponent } from './app-main/app-main.component';
=======
>>>>>>> b5428bc97bd688502e6591d4d8746011e919e9c4

@NgModule({
  declarations: [
    AppComponent,
    ProductItemComponent,
    CategoryComponent,
<<<<<<< HEAD
    ProductListComponent,
    AppMainComponent
=======
    ProductListComponent
>>>>>>> b5428bc97bd688502e6591d4d8746011e919e9c4
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
