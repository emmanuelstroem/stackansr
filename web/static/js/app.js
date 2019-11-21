$(document).ready(function() {

    $('.search-box').keydown(function(event) {
        // enter has keyCode = 13, change it if you want to use another button
        if (event.keyCode == 13) {
            console.log('enetered')
            this.form.submit();
        return false;
        }
});

});