// Initialize and add the map
function initMap() {
  // The location of spejchar
  var spejchar = {lat: 50.063100, lng: 14.597043};
  // The map, centered at spejchar
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 12, center: spejchar});
  // The marker, positioned at spejchar
  var marker = new google.maps.Marker({position: spejchar, map: map});
}

$(document).ready(function(){
	"use strict";

	var window_width 	 = $(window).width(),
	window_height 		 = window.innerHeight,
	header_height 		 = $(".default-header").height(),
	header_height_static = $(".site-header.static").outerHeight(),
	fitscreen 			 = window_height - header_height;


	$(".fullscreen").css("height", window_height)
	$(".fitscreen").css("height", fitscreen);

     
  //------- Active Nice Select --------//   
  $('select').niceSelect();

    $('.img-pop-up').magnificPopup({
        type: 'image',
        gallery:{
        enabled:true
        }
    });

     
   // -------   Active Mobile Menu-----//
    $('.active-about-carousel').owlCarousel({
        items:1,
        loop:true,
        autoplay:true
    })
    $('.next-trigger').click(function() {
        $(".active-about-carousel").trigger('next.owl.carousel');
    })
        // Go to the previous item
    $('.prev-trigger').click(function() {
        $(".active-about-carousel").trigger('prev.owl.carousel');
    });

    $('.active-gallery-carusel').owlCarousel({
        items:6,
        loop:true,
        autoplay:true
    })
    $('.next-trigger').click(function() {
        $(".active-gallery-carousel").trigger('next.owl.carousel');
    })
        // Go to the previous item
    $('.prev-trigger').click(function() {
        $(".active-gallery-carousel").trigger('prev.owl.carousel');
    });    




  // Select all links with hashes
  $('a[href*="#"]')
    // Remove links that don't actually link to anything
    .not('[href="#"]')
    .not('[href="#0"]')
    .click(function(event) {
      // On-page links
      if (
        location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
        && 
        location.hostname == this.hostname
      ) {
        // Figure out element to scroll to
        var target = $(this.hash);
        target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
        // Does a scroll target exist?
        if (target.length) {
          // Only prevent default if animation is actually gonna happen
          event.preventDefault();
          $('html, body').animate({
            scrollTop: target.offset().top-60
          }, 1000, function() {
            // Callback after animation
            // Must change focus!
            var $target = $(target);
            $target.focus();
            if ($target.is(":focus")) { // Checking if the target was focused
              return false;
            } else {
              $target.attr('tabindex','-1'); // Adding tabindex for elements not focusable
              $target.focus(); // Set focus again
            };
          });
        }
      }
    });

    // -------   Mail Send
    //update this with your $form selector
    var form_id = "myForm";
    var $form = $("#" + form_id);
    var sendButton = $('.submit-btn'); // submit button
    var data = {
        "access_token": "le9z6m3aagiqqwz17yqpi0vt"
    };

    function onSuccess(data) {
      $form .trigger('reset'); // reset form
      sendButton.text('Posláno');
    }

    function onError(error) {
      console.log(error)
      sendButton.text('Nastala chyba');
    }


    function send() {

      if ($form.get(0).reportValidity()){
        sendButton.text('Posílám...');
        sendButton.prop('disabled',true);
  
        var subject = "[web] Potvrzeni svatby";
        var message = $form .serialize(); // serialize form data;
  
        data['subject'] = subject;
        data['text'] = message;
  
        $.post('https://postmail.invotes.com/send',
            data,
            onSuccess
        ).fail(onError);
      }

      return false;
    }

    sendButton.on('click', send);
    $form.submit(function( event ) {
        event.preventDefault();
    });

    // include and load lightgallery
    const lightgallery = $('#js-lightgallery');
    lightgallery.load(lightgallery.attr("src"), () => {
      lightgallery.lightGallery({
        thumbnail:true,
        animateThumb: false,
        showThumbByDefault: false,
        // selector: '.lg-img',
      });
    });
 });
