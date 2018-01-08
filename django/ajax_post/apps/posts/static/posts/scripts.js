$(document).ready(function(){
    $('form').submit(function (e) {
        // preventDefault stops the default action of the event (e) from being triggered.
        e.preventDefault();
        console.log("Form submitted but no HTTP request sent to server!");
        $.ajax({
            url: $(this).attr('action'),
            method: 'post',
            data: $(this).serialize(),
            success: function(serverResponse){
                $('.posts').html(serverResponse)
            }
        });
        $(this).trigger('reset')
    });
});
