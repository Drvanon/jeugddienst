$(document).ready(function() {
    var $reacon = $('.reactioncontainer');
    var counter = 0;
        
    setInterval(function () {
        console.log('scrolling');
        var elem = $reacon[counter];
        var pos = $(elem).position()
        scrollTo(0, pos.top);
        if (counter >= $reacon.length - 1) {
            counter = 0;
        } else {
            counter++;
        }
    }, 1000
    );
});