odoo.define('your_module.custom_widget', function (require) {
    "use strict";

    var core = require('web.core');
    var FieldChar = require('web.basic_fields').FieldChar;

    var CustomWidget = FieldChar.extend({
        template: 'CustomWidgetTemplate',
        
        events: _.extend({}, FieldChar.prototype.events, {
            'click .btn': '_onButtonClick',
        }),

        _onButtonClick: function () {
            this.do_notify('Notification', 'Button clicked!');
        },
    });

    core.field_registry.add('custom_widget', CustomWidget);
});
