 // Get the canvas element
 var canvas = document.getElementById('canvas');
 var ctx = canvas.getContext('2d');

 // Set canvas dimensions
 canvas.width = 500;
 canvas.height = 300;

 // Add event listeners to input fields
 var caption1 = document.getElementById('caption1');
 var caption2 = document.getElementById('caption2');
 var caption3 = document.getElementById('caption3');

 caption1.addEventListener('input', function () {
   // Update the canvas with caption 1 text
   ctx.clearRect(0, 0, canvas.width, canvas.height);
   ctx.fillText(caption1.value, 10, 50);
 });

 caption2.addEventListener('input', function () {
   // Update the canvas with caption 2 text
   ctx.clearRect(0, 0, canvas.width, canvas.height);
   ctx.fillText(caption2.value, 10, 100);
 });

 caption3.addEventListener('input', function () {
   // Update the canvas with caption 3 text
   ctx.clearRect(0, 0, canvas.width, canvas.height);
   ctx.fillText(caption3.value, 10, 150);
 });