document.getElementById('start-detect').addEventListener('click', function() {
    window.location.href = '/camera';  // Redirect to camera page
});

document.getElementById('exit-app').addEventListener('click', function() {
    fetch('/shutdown', { method: 'POST' })
        .then(response => {
            if (response.ok) {
                window.close();  // Close the browser window (optional)
            }
        });
});
