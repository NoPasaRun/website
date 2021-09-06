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
      
    var btn = document.getElementById('upload-btn');
    var upload = document.getElementById('profile_photo');
    var fit = document.getElementById('change_image');
    var oFReader = new FileReader();
    btn.addEventListener('click', function() {
        upload.click()
    });

    upload.addEventListener('change', function() {
        if (upload.value) {
            oFReader.readAsDataURL((upload).files[0])
            oFReader.onload = function (oFREvent) {
                fit.src = oFREvent.target.result;
            };
            fit.style.display = 'block';
        };
    })
}