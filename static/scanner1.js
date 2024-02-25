// import Quagga from "../dist/quagga.min.js"; // Adjust the path as needed

const loadQuagga = () => {
  if ("mediaDevices" in navigator && navigator.mediaDevices.getUserMedia) {
    Quagga.init(
      {
        inputStream: {
          name: "Live",
          type: "LiveStream",
          numOfWorkers: navigator.hardwareConcurrency,
          target: document.querySelector("#barcode-scanner"),
          constraints: {
            width: 400,
            height: 400,
            facingMode: "environment",
          },
        },
        decoder: {
          readers: [
            "ean_reader",
            "ean_8_reader",
            "code_39_reader",
            "code_39_vin_reader",
            "codabar_reader",
            "upc_reader",
            "upc_e_reader",
          ],
        },
      },
      function (err) {
        if (err) {
          console.error(err);
          return;
        }
        console.log("Initialization finished. Ready to start");
        Quagga.start();
      }
    );
  }
};

document.addEventListener("DOMContentLoaded", loadQuagga);
