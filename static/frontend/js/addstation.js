document.addEventListener('DOMContentLoaded', function () {
    const gasStationForm = document.getElementById('gas-station-form');
    const addressInput = document.getElementById('address');
    const latitudeInput = document.getElementById('latitude');
    const longitudeInput = document.getElementById('longitude');
    const successMessage = document.getElementById('success-message'); // Get the success message element

    // Initialize the Google Maps map
    const mapContainer = document.getElementById('map');
    const mapOptions = {
        center: {
            lat: 0,
            lng: 0
        }, // Default center
        zoom: 14 // Default zoom level
    };
    const map = new google.maps.Map(mapContainer, mapOptions);

    gasStationForm.addEventListener('submit', function (event) {
        event.preventDefault();

        // Get form values
        const address = addressInput.value;
        const latitude = parseFloat(latitudeInput.value);
        const longitude = parseFloat(longitudeInput.value);
        const formData = new FormData(gasStationForm);

        // Update map center based on input location
        map.setCenter({
            lat: latitude,
            lng: longitude
        });

        // Perform form validation here (if needed)

        // Add your logic to submit the form data to a backend API or process it as needed
        // ...

        // Example using Fetch:
        fetch('/addstation/', {
                method: 'POST',
                body: formData,
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response from the backend (e.g., display a success message)
                successMessage.style.display = 'block'; // Show the success message
                console.log(data.message);
            })
            .catch(error => {
                // Handle errors here (e.g., display an error message)
                console.error(error);
            });
        
    });
});