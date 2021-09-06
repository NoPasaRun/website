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
}