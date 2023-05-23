google.charts.load('current', {'packages':['corechart']});

//avocado is a boolean
//if they clicked avocado, then true
//if they clicked the other stock, then false
function whenClicked(stock,avocado_data,stock_data, location, avocado_type) {
  var data = new google.visualization.DataTable();
  var avocadoName = `${location} ${avocado_type} Avocados`

  data.addColumn('date', 'Date');
  data.addColumn('number', avocadoName);
  data.addColumn('number', stock);

  var dates = Object.keys(avocado_data);

  for (var i = 0; i < dates.length; i++) {
    var date = dates[i];

    var avocadoPrice = avocado_data[date];
    var stockPrice = stock_data[date];

    data.addRow([new Date(date), avocadoPrice, stockPrice]);
  }
  /*
  data.addRows([
    [new Date (2016, 8, 6), 1, 1],
    [new Date (2016, 8, 13), 0.99, 1.15],
    [new Date (2016, 8, 20), 1.04, 1.12],
    [new Date (2016, 8, 27), 1.05, 1],
  ]);
  */
  //{{location}} {{avocado_type}} Avocados
  var options = {
    title: `${avocadoName} vs ${stock}`,
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
