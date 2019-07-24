function showTestimonial(testimonial_id, index) {
	var testimonials = document.getElementById(testimonial_id);
	var slides = testimonials.getElementsByClassName('swiper-slide');;
	var bullets = testimonials.getElementsByClassName('swiper-pagination-bullet')

	testimonials.setAttribute('style', 'height: ' + testimonials.clientHeight + 'px');

	for(var i=0; i < slides.length; i++){
		slides[i].className = slides[i].className.replace(/swiper-slide-active/, '');
	}

	
	slides[index].className += ' swiper-slide-active';
	for(var i=0; i < slides.length; i++){
		if(i != index){
			slides[i].className += ' swiper-slide-hide';
		}
	}


	for(var i=0; i < bullets.length; i++){
		if(i == index){
			bullets[i].className += ' swiper-pagination-bullet-active';
		} else {
			bullets[i].className = bullets[i].className.replace(/swiper-pagination-bullet-active/, '');
		}
	}
}
