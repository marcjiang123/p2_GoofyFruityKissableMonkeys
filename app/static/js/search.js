google.charts.load('current', {'packages':['corechart']});

function drawChart(stock,stock_data,avocado_data) {
  var data = new google.visualization.DataTable();
  data.addColumn('date', 'Dato');
  data.addColumn('number', 'Avocado');
  data.addColumn('number', stock);

  var dates = Object.keys(avocado_data);

  for (var i = 0; i < dates.length; i++) {
    var date = dates[i];

    var avocadoPrice = avocado_data[date];
    var stockPrice = stock_data[date];

    data.addRow([new Date(date), avocadoPrice, stockPrice]);
  }
  /*
        var data = google.visualization.arrayToDataTable([
          ['Year', 'AVOCADO', 'APPLE'],
          [Date(2011, 0, 1),  1,      1],
          [Date(2011, 0, 2),  0.99,      1.15],
          [Date(2011, 0, 3),  1.04,       1.12],
          [Date(2011, 0, 4),  1.05,      1]
        ]);*/

  var options = {
    title: stock.concat(' vs AVOCADO'),
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