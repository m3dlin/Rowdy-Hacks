function order_by_occurrence(arr) {
    var counts = {};
    arr.forEach(function (value) {
      if (!counts[value]) {
        counts[value] = 0;
      }
      counts[value]++;
    });
  
    return Object.keys(counts).sort(function (curKey, nextKey) {
      return counts[curKey] < counts[nextKey];
    });
  }
  const loadQuagga = () => {
    if ("mediaDevices" in navigator && navigator.mediaDevices.getUserMedia) {
      var last_result = []; //create array of detected images to improve scanning functionality
  
      if (Quagga.initialized == undefined) {
        //makes sure Quagga.onDetected only ran once
        //detect barcodes
        Quagga.onDetected(function (result) {
          //once a barcode is detected, save it to last_code and stop video
          var last_code = result.codeResult.code;
          last_result.push(last_code);
          if (last_result.length > 20) {
            //capture 20 images
            code = order_by_occurrence(last_result)[0]; //get the image that appears the most often **most accurate**
            last_result = [];
            Quagga.stop();
            sendCodeToFlask(code);
            /*****SEND DATA TO PYTHON BACKEND */
          }
        });
      }
  
      Quagga.init(
        {
          inputStream: {
            name: "Live",
            type: "LiveStream",
            numOfWorkers: navigator.hardwareConcurrency,
            target: document.querySelector("#barcode-scanner"),
            //   constraints: {
            //     width: 400, //{
            //     //   min: 640,
            //     //   ideal: 1280,
            //     //   max: 2560,
            //     //},
            //     height: 400, //{
            //     //   min: 360,
            //     //   ideal: 720,
            //     //   max: 1440,
            //     //},
            //     facingMode: "environment",
            //   },
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
          Quagga.initialized = true; //user defined variable so that onDetected only runs once
          console.log("Initialization finished. Ready to start");
          Quagga.start();
        }
      );
    }
  };
  
  document.addEventListener("DOMContentLoaded", loadQuagga);
  


  function sendCodeToFlask(code) {
    // Send a POST request to the Flask backend with the image data
    fetch("/upload_code", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ code: code }),
    })
      .then((response) => {
        if (response.ok) {
          console.log("code uploaded successfully");
          //redirect to capture page
          window.location.href = "/capture";
        } else {
          console.error("Error uploading code1:", response.statusText);
        }
      })
      .catch((error) => {
        console.error("Error uploading code2:", error);
      });
  }