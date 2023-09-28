document.addEventListener('DOMContentLoaded', function () {
    const gasStations = JSON.parse(localStorage.getItem('gasStations')) || [];
    const resultsContainer = document.getElementById('results');
    const filterForm = document.getElementById('filter-form');

    // Add event listener for the filter form submission
    filterForm.addEventListener('submit', function (event) {
        event.preventDefault(); // Prevent the default form submission

        const searchInput = document.getElementById('search').value.toLowerCase();
        const priceInput = document.getElementById('price').value.toLowerCase();
        const ratingSelect = document.getElementById('rating').value;
        const customerServiceSelect = document.getElementById('customer-service').value;

        // Filter gas stations based on individual criteria
        const filteredStations = gasStations.filter(station => {
            const matchesSearchQuery = searchInput.length === 0 || station.name.toLowerCase().includes(searchInput);
            const matchesPrice = priceInput.length === 0 || station.price.toLowerCase().includes(priceInput);
            const matchesRating = ratingSelect === '0' || station.rating === parseInt(ratingSelect);
            const matchesCustomerService = customerServiceSelect === '0' || station.customerService === parseInt(customerServiceSelect);

            return matchesSearchQuery && matchesPrice && matchesRating && matchesCustomerService;
        });

        // Display filtered stations
        displayGasStations(filteredStations);
    });

    // Function to display gas stations in the results section
    function displayGasStations(stations) {
        resultsContainer.innerHTML = ''; // Clear previous results

        if (stations.length === 0) {
            resultsContainer.innerHTML = '<p>No results found.</p>';
            return;
        }

        stations.slice(0, 3).forEach(station => { // Display only the first 3 stations
            const stationCard = document.createElement('div');
            stationCard.classList.add('station-card');

            stationCard.innerHTML = `
                <h3>${station.name}</h3>
                <p>Rating: ${station.rating}</p>
                <p>Customer Service: ${station.customerService}</p>
                <p>Price: ${station.price}</p>
            `;

            resultsContainer.appendChild(stationCard);
        });
    }

    // Initial display of all gas stations
    displayGasStations(gasStations.slice(0, 3)); // Display the first 3 stations
});
