(function (){
	var arrows = document.querySelectorAll('.accordion-wrap .entry-title');
	for(var i=0; i < arrows.length; i++){
		arrows[i].onclick = function() {
			if(this.querySelector('.arrow').classList.contains('arrow-d')) {
				old_class = 'arrow-d';
				new_class = 'arrow-r';
				return
			}
			for(var i=0; i < arrows.length; i++){
				arrows[i].querySelector('.arrow').classList.remove('arrow-d');
				arrows[i].querySelector('.arrow').classList.add('arrow-r');
			}
			this.querySelector('.arrow').classList.toggle('arrow-d');
			this.querySelector('.arrow').classList.toggle('arrow-r');

			var answers = this.parentNode.querySelectorAll('.entry-content');
			for(var i=0; i < answers.length; i++) {
				answers[i].classList.remove('accordion-active');
			}
			this.nextElementSibling.classList.toggle('accordion-active');
		}
	}
})();
