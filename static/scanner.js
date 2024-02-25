feather.replace();

const controls = document.querySelector(".controls");
const cameraOptions = document.querySelector(".video-options>select");
const video = document.querySelector("video");
const canvas = document.querySelector("canvas");
const screenshotImage = document.querySelector("img");
const buttons = [...controls.querySelectorAll("button")];
let streamStarted = false;

// navigator.mediaDevices.getUserMedia({ video: true });
const [play, pause, screenshot] = buttons;

const constraints = {
  video: {
    width: {
      min: 1280,
      ideal: 1920,
      max: 2560,
    },
    height: {
      min: 720,
      ideal: 1080,
      max: 1440,
    },
    facingMode: {
      exact: "environment",
    },

    // facingMode: {
    //   exact: "environment",
    // },
  },
};

const getCameraSelection = async () => {
  const devices = await navigator.mediaDevices.enumerateDevices();
  const videoDevices = devices.filter((device) => device.kind === "videoinput");
  const options = videoDevices.map((videoDevice) => {
    return `<option value="${videoDevice.deviceId}">${videoDevice.label}</option>`;
  });
  cameraOptions.innerHTML = options.join("");
};

play.onclick = () => {
  if (streamStarted) {
    video.play();
    play.classList.add("d-none");
    pause.classList.remove("d-none");
    return;
  }
  if ("mediaDevices" in navigator && navigator.mediaDevices.getUserMedia) {
    const updatedConstraints = {
      ...constraints,
      deviceId: {
        exact: cameraOptions.value,
      },
    };
    startStream(updatedConstraints);
  }
};

const startStream = async (constraints) => {
  const stream = await navigator.mediaDevices.getUserMedia(constraints);
  handleStream(stream);
};

const handleStream = (stream) => {
  video.srcObject = stream;
  play.classList.add("d-none");
  pause.classList.remove("d-none");
  screenshot.classList.remove("d-none");
  streamStarted = true;
};

getCameraSelection();

cameraOptions.onchange = () => {
  const updatedConstraints = {
    ...constraints,
    deviceId: {
      exact: cameraOptions.value,
    },
  };
  startStream(updatedConstraints);
};

const pauseStream = () => {
  video.pause();
  play.classList.remove("d-none");
  pause.classList.add("d-none");
};

const doScreenshot = () => {
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  canvas.getContext("2d").drawImage(video, 0, 0);
  screenshotImage.src = canvas.toDataURL("image/webp");
  const imageDataURL = canvas.toDataURL("image/webp");
  screenshotImage.classList.remove("d-none");
  sendImageToFlask(imageDataURL);
};

function sendImageToFlask(imageDataURL) {
  // Send a POST request to the Flask backend with the image data
  fetch("/upload", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ imageDataURL: imageDataURL }),
  })
    .then((response) => {
      if (response.ok) {
        console.log("Image uploaded successfully");
      } else {
        console.error("Error uploading image:", response.statusText);
      }
    })
    .catch((error) => {
      console.error("Error uploading image:", error);
    });
}

pause.onclick = pauseStream;
screenshot.onclick = doScreenshot;
