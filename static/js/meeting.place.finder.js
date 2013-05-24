(function($) {
    var defaults = {
       : 'Jack',
       number: '555-jack'
    }

    $.myPlugin = function(options) {
        var settings = $.extend({}, defaults, options);

        this.someFunction = function() {
            // you can use settings here
        }
    }
}(jQuery));