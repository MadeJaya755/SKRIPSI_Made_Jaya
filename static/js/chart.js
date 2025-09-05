const ctx = document.getElementById('chartCuaca').getContext('2d');

// Periksa apakah cuacaAcc dan awanAcc valid, jika tidak set default
let cuacaAcc = parseFloat("{{ cuaca_acc|default(0)|tojson }}") || 0;
let awanAcc = parseFloat("{{ awan_acc|default(0)|tojson }}") || 0;

// Membuat chart dengan konfigurasi yang lebih baik
const chartCuaca = new Chart(ctx, {
  type: 'bar',
  data: {
    labels: ['Cuaca', 'Awan'],
    datasets: [{
      label: 'Kemungkinan (%)',
      data: [cuacaAcc, awanAcc],
      backgroundColor: ['rgba(54, 162, 235, 0.7)', 'rgba(255, 99, 132, 0.7)'],
      borderColor: ['#007bff', '#dc3545'],
      borderWidth: 1
    }]
  },
  options: {
    responsive: true, 
    maintainAspectRatio: false, 
    scales: {
      y: {
        beginAtZero: true,
        max: 100, // Nilai maksimal untuk sumbu y adalah 100
        ticks: {
          stepSize: 10 // Setiap kenaikan adalah 10
        }
      }
    },
    plugins: {
      legend: {
        position: 'top', // Posisi legenda di atas grafik
        labels: {
          font: {
            size: 14 // Ukuran font legenda
          }
        }
      }
    }
  }
});
