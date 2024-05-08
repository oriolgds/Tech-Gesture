// Reference to the video element in HTML
const videoElement = document.getElementById('videoElement');
const predictionsImage = document.getElementById('predictions-show');
navigator.mediaDevices.getUserMedia({ video: true })
  .then(function(stream) {
    // Assign the camera stream to the video element
    videoElement.srcObject = stream;

    // List all available camera devices
    navigator.mediaDevices.enumerateDevices()
      .then(function(devices) {
        // Filter out only the video input devices (cameras)
        const cameras = devices.filter(device => device.kind === 'videoinput');
        
        // Log the list of camera devices
        console.log('Available cameras:', cameras);
      })
      .catch(function(error) {
        console.error('Error listing camera devices:', error);
      });
  })
  .catch(function(error) {
    console.error('Error accessing camera:', error);
  });



// Function to capture and send the webcam signal
function captureAndSend() {
  var canvas = document.createElement('canvas');
  var video = document.getElementById('videoElement');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  var context = canvas.getContext('2d');
  context.drawImage(video, 0, 0, canvas.width, canvas.height);

  // Convert canvas to base64 image
  var imageDataURL = canvas.toDataURL('image/jpeg');

  // Send the data to the server
  fetch('../predict', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ image: imageDataURL })
  })
  .then(response => {
      if (!response.ok) {
          throw new Error('Network response was not ok');
      }
      
      return response.json()
  })
  .then(data => {
      console.log('Server response:', data);
      const dataURL = "data:image/jpeg;base64," + data.predictions_image;
      predictionsImage.src = dataURL
  })
  .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
  });
}

// Capture and send the webcam signal every 5 seconds (adjust as needed)
setInterval(captureAndSend, 5);