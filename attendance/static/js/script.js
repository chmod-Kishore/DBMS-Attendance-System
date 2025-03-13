document.addEventListener("DOMContentLoaded", function () {
    const video = document.getElementById("qr-video");
    const result = document.getElementById("scan-result");

    navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } })
        .then(stream => {
            video.srcObject = stream;
            video.play();
        });

    // Simulate scanning (replace with real QR scanner library)
    setTimeout(() => {
        result.innerText = "Scanned QR Code: CLASS123";
    }, 3000);
});
