function showSlide(carousel_id, index) {
	var carousel = document.getElementById(carousel_id);
	var slides = carousel.getElementsByClassName('swiper-slide');;
	var bullets = carousel.getElementsByClassName('swiper-pagination-bullet')

	carousel.setAttribute('style', 'height: ' + carousel.clientHeight + 'px');

	for(var i=0; i < slides.length; i++){
		slides[i].className = slides[i].className.replace(/swiper-slide-active/, '');
	}

	window.setTimeout(
		function(slides, index){
			slides[index].className += ' swiper-slide-active';
			for(var i=0; i < slides.length; i++){
				if(i != index){
					slides[i].className += ' swiper-slide-hide';
				}
			}
		},
		300, slides, index
	);


	for(var i=0; i < bullets.length; i++){
		if(i == index){
			bullets[i].className += ' swiper-pagination-bullet-active';
		} else {
			bullets[i].className = bullets[i].className.replace(/swiper-pagination-bullet-active/, '');
		}
	}
}
