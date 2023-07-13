$(document).ready(function() {
    var canvas = document.getElementById('memeCanvas');
    var ctx = canvas.getContext('2d');
    
    // Draw the initial image on the canvas
    var img = new Image();
    img.src = "{% static 'images/default_image.png' %}";  // Replace with your default image URL
    img.onload = function() {
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
    };
    
    // Handle text input and canvas interactions
    $('#memeForm').on('input', 'input[type="text"]', function() {
      drawMeme();
    });
    
    function drawMeme() {
      // Clear the canvas
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      // Draw the image
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      
      // Set caption styles
      ctx.font = '36px Arial';
      ctx.fillStyle = '#ffffff';
      ctx.strokeStyle = '#000000';
      ctx.textAlign = 'center';
      
      // Draw the captions
      var caption1 = $('#caption1').val();
      var caption2 = $('#caption2').val();
      var caption3 = $('#caption3').val();
      
      ctx.fillText(caption1, canvas.width / 2, 100);
      ctx.fillText(caption2, canvas.width / 2, canvas.height - 100);
      ctx.fillText(caption3, canvas.width / 2, canvas.height / 2);
      ctx.strokeText(caption1, canvas.width / 2, 100);
      ctx.strokeText(caption2, canvas.width / 2, canvas.height - 100);
      ctx.strokeText(caption3, canvas.width / 2, canvas.height / 2);
    }
  });
  