/*=============================================================
    Authour URL: www.htmladmin.com
    
    http://www.htmladmin.com/

    License: MIT

    http://opensource.org/licenses/MIT

    100% Free To use For Personal And Commercial Use.

    IN EXCHANGE JUST TELL PEOPLE ABOUT THIS WEBSITE
   
========================================================  */           

$(document).ready(function () {

    /*====================================
           METIS MENU 
     ======================================*/

    $('#main-menu').metisMenu();

    /*======================================
    LOAD APPROPRIATE MENU BAR ON SIZE SCREEN
    ========================================*/

    $(window).bind("load resize", function () {
        if ($(this).width() < 768) {
            $('div.sidebar-collapse').addClass('collapse')
        } else {
            $('div.sidebar-collapse').removeClass('collapse')
        }
    });
     

});

/*======================================
  SIDE MENU SCRIPTS
  ========================================*/
$(document).ready(function () {
    $('#buttonMenu').on('click', function () {
        body.toggleClass('push-right');
        $('#side-menu-push').toggleClass('set-menu-open');
    });
});

body = $(document.body); // Passes the element when calling the $ function

/*======================================
  FOR TEXT EDITOE - summernote
  ========================================*/
$(document).ready(function () {
    $('#text-editor').summernote({
        height: 250,// set height for editor
    });
});

/*======================================
  WRITE YOUR SCRIPTS BELOW
  ========================================*/
      