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

document.addEventListener('DOMContentLoaded', function () {
    const fuelfinderLink = document.querySelector('#fuelfinder-link');
    const addstationLink = document.querySelector('#addstation-link');
    const modal = document.getElementById('login-required-modal');
    const closeBtn = document.querySelector('.close');

    // Function to show the modal
    function showModal() {
        modal.style.display = 'block';
    }

    // Function to hide the modal
    function hideModal() {
        modal.style.display = 'none';
    }

    // Event listener for the fuelfinder link
    fuelfinderLink.addEventListener('click', function (e) {
        e.preventDefault(); // Prevent the default click behavior
        showModal();
    });

    // Event listener for the addstation link
    addstationLink.addEventListener('click', function (e) {
        e.preventDefault(); // Prevent the default click behavior
        showModal();
    });

    // Event listener for the close button
    closeBtn.addEventListener('click', hideModal);

    // Event listener for clicking outside the modal
    window.addEventListener('click', function (e) {
        if (e.target === modal) {
            hideModal();
        }
    });
});


