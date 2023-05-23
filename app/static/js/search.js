google.charts.load('current', {'packages':['corechart']});

function drawChart() {
  var data = new google.visualization.DataTable();
  data.addColumn('date', 'Dato');
  data.addColumn('number', 'Avocado');
  data.addColumn('number', 'Apple');

  data.addRows([
    [new Date (2016, 8, 6), 1, 1],
    [new Date (2016, 8, 13), 0.99, 1.15],
    [new Date (2016, 8, 20), 1.04, 1.12],
    [new Date (2016, 8, 27), 1.05, 1],
  ]);

  var options = {
    title: 'AVOCADO vs APPLE INC',
    curveType: 'function',
    colors: ['#568203', '#a52714'],
    legend: { position: 'bottom' },
    vAxis: {
      format: 'percent'
    },
    hAxis: { format: "MM/dd/yy"}

  };

  var chart = new google.visualization.LineChart(document.getElementById('curve_chart'));

  chart.draw(data, options);
}

google.setOnLoadCallback(drawChart);