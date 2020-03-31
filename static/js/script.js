$('#myModal').modal(show)

(function($){
    var a = null;
    $(window).resize(function(){
        if(a != null) {
            clearTimeout(a);
        }

        a = setTimeout(function(){
            FB.XFBML.parse();
        },1000)
    })
})(jQuery)