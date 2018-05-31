import { NgModule }        from '@angular/core';
import { CommonModule }    from '@angular/common';

import { TooltipModule }       from 'ngx-bootstrap/tooltip';

import { ClipboardComponent }  from './clipboard/clipboard.component';


@NgModule({
    imports: [
    	CommonModule,
        TooltipModule
    ],
    declarations: [
        ClipboardComponent
    ],
    exports: [
    	ClipboardComponent
    ]
})
export class UtilitiesModule { }
