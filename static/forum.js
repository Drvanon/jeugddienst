$(document).ready(function () {
    $("#reactionForm").submit(function (e) {
        e.preventDefault();
        var form_content;
        form_content = $('#reactionForm').serialize();
        $.post(window.location.pathname,
            form_content, 
            function () {
                window.location ='/';
            }
        );
        return false;
    });
});