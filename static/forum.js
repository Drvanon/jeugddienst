function words_in_sentence(sentence) {
    var spaces = 1;

    for(var i=0; i<sentence.length; i++) {
        if(sentence[i] == ' ') {
            spaces = spaces + 1;
        }
    }
    
    return spaces;
}

$(document).on( "pageinit", ".forumpage", function() {
    $('#reactionField').on('keydown', function() {
        var left = 30 - words_in_sentence($('#reactionField').val());
        
        if (left > 0) {
            $('#reactionSpan').text('Je hebt nog '+ left + ' woorden over');
            $('#reactionSpan').css('color',  'green');
        } else {
            $('#reactionSpan').text('Je hebt geen woorden over, haal er een paar weg.');
            $('#reactionSpan').css('color', 'red');
        }
    });

    $(".reactionForm").on('submit', function (e) {
        e.preventDefault();
        var left = 30 - words_in_sentence($('#reactionField').val());
        var form_content;
        
        if(left > 0) {
            form_content = $('.reactionForm').serialize();
            $.post(window.location.pathname,
                form_content, 
                function () {
                    window.location ='/';
                }
            );
        }
        return false;
    });
});