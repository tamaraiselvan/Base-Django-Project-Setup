const BarGraph = document.getElementById("BarGraphChart");
new Chart(BarGraph, {
  type: "bar",
  data: {
    labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [
      {
        label: "# of Votes",
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1
      }
    ]
  },
  options: {
    scales: {
      y: {
        beginAtZero: true
      }
    }
  }
});

const LineGraph = document.getElementById("LineGraphChart");
new Chart(LineGraph, {
  type: "line",
  data: {
    labels: ["Jan", "Feb", "Mar", "Apr", "May", "Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    datasets: [{
        label: 'Loss',
        data: [50, 40, 39, 60, 75, 66, 48, 50, 60, 53, 36, 25],
        fill: false,
        borderColor: 'rgb(255, 0, 0)'
      },
      {
        label: 'Gain',
        data: [15, 35, 49, 68, 80, 75, 77, 60, 52, 42, 59, 75],
        fill: false,
        borderColor: 'rgb(72, 255, 0)'
      }
    ]
  },
  options: {
    plugins: {
      title: {
        display: true,
        text: 'Gain & Loss of (2023)'
      }
    },
    scales: {
      y: {
        beginAtZero: true
      },
      
    },
  }
});


const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))

function preview() {
  frame.src = URL.createObjectURL(event.target.files[0]);
}

function clearImage() {
  document.getElementById('formFile').value = null;
  frame.src = "";
}

