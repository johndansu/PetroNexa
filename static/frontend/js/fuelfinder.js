document.addEventListener('DOMContentLoaded', function () {
    const filterForm = document.getElementById('filter-form');
    const resultsContainer = document.getElementById('results');

    filterForm.addEventListener('submit', function (e) {
        e.preventDefault(); // Prevent form submission

        // Get selected filter values
        const searchQuery = document.getElementById('search').value;
        const rating = document.getElementById('rating').value;
        const price = document.getElementById('price').value;
        const customerService = document.getElementById('customer-service').value;

        // Create a query string for filtering
        const queryString = `?q=${searchQuery}&rating=${rating}&price=${price}&customer-service=${customerService}`;

        // Fetch filtered results using AJAX
        fetch(`/fuelfinder/${queryString}`)
            .then(response => response.json())
            .then(data => {
                // Update the results container with new data
                displayGasStations(data.fuel_stations);
            })
            .catch(error => {
                console.error('Error fetching data:', error);
            });
    });

    // Function to display gas stations in the results section
    function displayGasStations(stations) {
        resultsContainer.innerHTML = '';

        if (stations.length === 0) {
            resultsContainer.innerHTML = '<p>No results found.</p>';
            return;
        }

        stations.forEach(station => {
            const stationCard = document.createElement('div');
            stationCard.classList.add('station-card');

            stationCard.innerHTML = `
                <h3>${station.title}</h3>
                <p>Rating: ${station.rating}</p>
                <p>Customer Service: ${station.customer_service}</p>
                <p>Price: ${station.price}</p>
                <!-- Add other station details as needed -->
            `;

            resultsContainer.appendChild(stationCard);
        });
    }
});
