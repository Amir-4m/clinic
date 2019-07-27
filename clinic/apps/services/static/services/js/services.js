(function (){
	var tabs = document.querySelectorAll('.tabs-nav li');
	for(var i=0; i < tabs.length; i++){
		tabs[i].onclick = function() {
			for(var i=0; i < tabs.length; i++){
				tabs[i].classList.remove('active');
			}
			this.classList.add('active');

			contents = document.querySelectorAll('.tabs-container div');
			for(var i=0; i < tabs.length; i++){
				contents[i].classList.remove('tab-content-active');
			}

			document.querySelector(
				'.tabs-container div' + this.getAttribute('data-target')
			).classList.add('tab-content-active');
		}
	}
})();
