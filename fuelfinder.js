document.addEventListener('DOMContentLoaded', function () {
    const gasStations = JSON.parse(localStorage.getItem('gasStations')) || [];

    const filterButton = document.getElementById('filter-btn');
    const searchInput = document.getElementById('search');
    const priceInput = document.getElementById('price');

    // Add event listener for the filter button
    filterButton.addEventListener('click', applyFilters);

    // Add event listener for the search input
    searchInput.addEventListener('input', applyFilters);

    // Add event listener for the price input
    priceInput.addEventListener('input', applyFilters);

    // Function to apply filters based on user input
    function applyFilters() {
        // Get selected filter values
        const selectedRating = Number(document.getElementById('rating').value);
        const selectedCustomerService = Number(document.getElementById('customer-service').value);
        const searchQuery = searchInput.value.toLowerCase();
        const priceQuery = priceInput.value.toLowerCase(); // Get price input value

        // Filter gas stations based on criteria
        const filteredStations = gasStations.filter(station => {
            const matchesRating = selectedRating === 0 || station.rating === selectedRating;
            const matchesCustomerService = selectedCustomerService === 0 || station.customerService === selectedCustomerService;
            const matchesSearchQuery = station.name.toLowerCase().includes(searchQuery);
            const matchesPrice = station.price.toLowerCase().includes(priceQuery); // Check price match
            
            return matchesRating && matchesCustomerService && matchesSearchQuery && matchesPrice;
        });

        // Display filtered stations
        displayGasStations(filteredStations);
    }

    // Function to display gas stations in the results section
    function displayGasStations(stations) {
        const resultsContainer = document.getElementById('results');
        resultsContainer.innerHTML = '';

        if (stations.length === 0) {
            resultsContainer.innerHTML = '<p>No results found.</p>';
            return;
        }

        stations.forEach(station => {
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
    displayGasStations(gasStations);
});
