$(document).on( "pageinit", ".forumpage", function() {
    alert('shits happening');
    $(".reactionForm").on('submit', function (e) {
        e.preventDefault();
        var form_content;
        form_content = $('.reactionForm').serialize();
        $.post(window.location.pathname,
            form_content, 
            function () {
                window.location ='/';
            }
        );
        return false;
    });
});