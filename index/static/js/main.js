
$(document).ready(function() {
	$('.loader_container').fadeOut("slow");
	$(".navbar-burger").click(function() {
		// Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
		$(".navbar-burger").toggleClass("is-active");
		$(".navbar-menu").toggleClass("is-active");
	});
	$("#comment-button").on('click', function(){
		$("i", this).toggleClass("fa-chevron-down fa-chevron-up");
		$("#comment-container").slideToggle("Slow");
	});
	$('#leave-comment').on('click',function(){
		$('comment-container').slideToggle('slow');
		$('thankyou-container').html("<div class=\'is-notification is-primary\'>Thank you for you feedback</div>");
	});
	$('.members-in').slick({
		infinite: true,
		slidesToShow: 6,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 2000,
		arrows: false
	});

	$('.journal-carousel').slick({
		infinite: true,
		slidesToShow: 3,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 4000,
		arrows: false,
		variableWidth: true
	});
	$('.top-editors-carousel').slick({
		infinite: true,
		slidesToShow: 3,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 4000,
		arrows: false,
		vertical: true
	});
	$('.global-indexing-container').slick({
		infinite: true,
		slidesToShow: 4,
		slidesToScroll: 1,
		autoplay: true,
		autoplaySpeed: 3000,
		arrows: false
	});
	$(".abstract-button").click(function(){
		var id = $(this).data('id');
		$("#abstract-panel-"+id).slideToggle("slow");
	});
	$('.count').each(function () {
		$(this).prop('Counter',0).animate({
			Counter: $(this).text()
		}, {
			duration: 3000,
			easing: 'swing',
			step: function (now) {
				$(this).text(Math.ceil(now));
			}
		});
	});
});


