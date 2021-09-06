window.onload = () => {
    var myVar = setInterval(function() {
        myTimer();
      }, 1000);
      
      function myTimer() {
        var date = new Date();
        var minutes = date.getMinutes()
        if (parseInt(minutes) < 10) {
            minutes = '0' + minutes
        }
        document.getElementsByClassName("editional-info_time-info")[0].innerHTML = date.getHours() + ':' + minutes;
      }
    
    var slider = document.getElementById('slider');
    var amount = document.getElementsByClassName('section_image-add').length;
    var left_sroller = document.getElementById('left_scroller');
    var right_scroller = document.getElementById('right_scroller');
    var position = 0;

    left_scroller.addEventListener("click", function() {
        if(position == 0) {
            position = -(amount*500);
        }
        position += 500;
        slider.style.left = position + 'px';
    });

    right_scroller.addEventListener("click", function() {
        if(position == -((amount-1)*500)) {
            position = 500;
        }
        position -= 500;
        slider.style.left = position + 'px';
    });
}