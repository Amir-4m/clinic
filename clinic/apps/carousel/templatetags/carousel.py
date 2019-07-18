from django.template import Library
from django.conf import settings
from django.utils.safestring import mark_safe

register = Library()


@register.simple_tag
def carousel_js_tags():
    return mark_safe(
        f'''
            <script src="{settings.STATIC_URL}carousel/js/swiper.min.js"></script>
            <script>
              swiper = new Swiper('.swiper-container', {{
                direction: 'horizontal',
                loop: false,


                navigation: {{
                  nextEl: '.swiper-button-next',
                  prevEl: '.swiper-button-prev',
                }},

                scrollbar: {{
                  el: '.swiper-scrollbar',
                }},
              }});

              bullets = document.getElementsByClassName('swiper-pagination-bullet');
              for(var i=0; i < bullets.length; i++){{
                var bullet = bullets[i];
                bullet.addEventListener('click', function (e) {{
                  e.preventDefault();
                  for(var j=0; j < bullets.length; j++){{
                    bullets[j].classList.remove('swiper-pagination-bullet-active');
                  }}
                  this.classList.add('swiper-pagination-bullet-active');
                  swiper.slideTo(this.getAttribute('data-slide'), 200);
                }});
              }}
            </script>'''
    )


@register.simple_tag
def carousel_css_tags():
    return mark_safe(
        f'<link rel="stylesheet" href="{settings.STATIC_URL}carousel/css/swiper.min.css">'
    )


@register.inclusion_tag('carousel/carousel.html')
def carousel(carousel):
    return {
        'carousel': carousel
    }
