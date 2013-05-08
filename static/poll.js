$(document).on( "pageinit", ".pollpage", function() {
    $(".pollForm").on('submit', function (e) {
        e.preventDefault();
        var form_content;
        form_content = $('.pollForm').serialize();
        $.post(window.location.pathname,
            form_content, 
            function () {
                window.location ='/';
            }
        );
        return false;
    });
});