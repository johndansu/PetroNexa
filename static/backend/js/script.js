document.addEventListener('DOMContentLoaded', function () {
    // Sample data for the charts
    const activityGraphData = {
      labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
      datasets: [
        {
          label: 'User Activity',
          data: [10, 20, 15, 30, 25],
          backgroundColor: 'rgba(75, 192, 192, 0.2)', // Chart background color
          borderColor: 'rgba(75, 192, 192, 1)', // Border color
          borderWidth: 1, // Border width
        },
      ],
    };
  
    const userActivityChartData = {
      labels: ['Logged In', 'Posted Reviews', 'Liked Posts', 'Commented'],
      datasets: [
        {
          data: [50, 30, 20, 15],
          backgroundColor: ['rgba(255, 99, 132, 0.7)', 'rgba(54, 162, 235, 0.7)', 'rgba(75, 192, 192, 0.7)', 'rgba(255, 206, 86, 0.7)'],
        },
      ],
    };
  
    // Create and configure the Activity Graph
    const activityGraphCanvas = document.getElementById('activity-graph');
    const activityGraphCtx = activityGraphCanvas.getContext('2d');
  
    const activityGraph = new Chart(activityGraphCtx, {
      type: 'line', // Line chart
      data: activityGraphData,
      options: {
        scales: {
          y: {
            beginAtZero: true,
          },
        },
      },
    });
  
    // Create and configure the User Activity Pie Chart
    const userActivityChartCanvas = document.getElementById('user-activity-chart');
    const userActivityChartCtx = userActivityChartCanvas.getContext('2d');
  
    const userActivityChart = new Chart(userActivityChartCtx, {
      type: 'pie', // Pie chart
      data: userActivityChartData,
      options: {
        responsive: true,
      },
    });
  });
  