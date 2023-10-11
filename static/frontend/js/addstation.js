document.addEventListener('DOMContentLoaded', function () {
    const gasStationForm = document.getElementById('gas-station-form');
    const addressInput = document.getElementById('address');
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

        // Get the address input value
        const address = addressInput.value;

        // Use the Geocoder to convert the address to latitude and longitude
        const geocoder = new google.maps.Geocoder();
        geocoder.geocode({ address: address }, function (results, status) {
            if (status === google.maps.GeocoderStatus.OK) {
                const location = results[0].geometry.location;

                // Update the map center based on the converted location
                map.setCenter(location);

                // Set the latitude and longitude values in the form data
                gasStationForm.querySelector('input[name="latitude"]').value = location.lat();
                gasStationForm.querySelector('input[name="longitude"]').value = location.lng();

                // Submit the form
                gasStationForm.submit();
            } else {
                // Handle the case where the address couldn't be geocoded (e.g., display an error message)
                console.error('Geocoding failed:', status);
            }
        });
    });
});
