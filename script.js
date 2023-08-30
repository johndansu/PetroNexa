document.addEventListener('DOMContentLoaded', function () {
  const gasStations = JSON.parse(localStorage.getItem('gasStations')); // Retrieve gas station data

  const gasStationNames = document.querySelectorAll('.gas-station-name');
  const gasStationBlogContent = document.querySelector('.gas-station-blog-content');

  gasStationNames.forEach(function (station) {
    station.addEventListener('click', function () {
      const name = station.textContent;
      const selectedGasStation = gasStations.find(station => station.name === name);
      const blogContent = selectedGasStation ? selectedGasStation.blogContent : '';

      gasStationBlogContent.innerHTML = `
        <h3>${name}</h3>
        <p>${blogContent}</p>
      `;
    });
  });

  // Additional event listeners and code
  const filterInput = document.getElementById('filterInput');
  const searchButton = document.getElementById('searchButton');

  searchButton.addEventListener('click', function () {
    const filterCriteria = filterInput.value.toLowerCase();
    displayFilteredGasStations(filterCriteria);
  });

  // Function to display filtered gas stations
  function displayFilteredGasStations(filterCriteria) {
    const filteredGasStations = gasStations.filter(station => station.name.toLowerCase().includes(filterCriteria));

    // Update display with filtered gas stations
    const gasStationList = document.querySelector('.gas-station-list');
    gasStationList.innerHTML = '';

    filteredGasStations.forEach(function (station) {
      const stationDiv = document.createElement('div');
      stationDiv.classList.add('gas-station-name');
      stationDiv.textContent = station.name;
      gasStationList.appendChild(stationDiv);
    });
  }

  // ... (other event listeners and code)

  // Function to display gas stations on the fuel finder page
  function displayGasStations() {
    const gasStationList = document.querySelector('.gas-station-list');
    gasStationList.innerHTML = '';

    gasStations.forEach(function (station) {
      const stationDiv = document.createElement('div');
      stationDiv.classList.add('gas-station-name');
      stationDiv.textContent = station.name;
      gasStationList.appendChild(stationDiv);
    });
  }

  displayGasStations();
});


