google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawPriceChart);
google.charts.setOnLoadCallback(drawVolumeChart);
google.charts.setOnLoadCallback(drawBagsChart);

console.log("hi")
function test(testparam) {
  console.log("what")
  console.log(testparam)
}
function drawPriceChart() {
  var data = new google.visualization.DataTable();
  data.addColumn('date', 'Date');
  data.addColumn('number', 'Avocado');

  data.addRows([
    [new Date (2016, 8, 6), 2.3],
    [new Date (2016, 8, 13), 6.43],
    [new Date (2016, 8, 20), 4],
    [new Date (2016, 8, 27), 5],
  ]);

  var options = {
    title: 'AVOCADO PRICES',
    curveType: 'function',
    colors: ['#AA471F'],
    legend: { position: 'bottom' },
    hAxis: { format: "MM/dd/yy"}

  };

  var chart = new google.visualization.LineChart(document.getElementById('main-chart'));

  chart.draw(data, options);
}

function drawVolumeChart() {
  var data = new google.visualization.DataTable();
  data.addColumn('date', 'Date');
  data.addColumn('number', 'Avocado');

  data.addRows([
    [new Date (2016, 8, 6), 2.3],
    [new Date (2016, 8, 13), 6.43],
    [new Date (2016, 8, 20), 4],
    [new Date (2016, 8, 27), 5],
  ]);

  var options = {
    title: 'AVOCADO VOLUME',
    curveType: 'function',
    colors: ['#568203'],
    legend: { position: 'bottom' },
    hAxis: { format: "MM/dd/yy"}

  };

  var chart = new google.visualization.ColumnChart(document.getElementById('volume-chart'));

  chart.draw(data, options);
}



function drawBagsChart() {
  var data = new google.visualization.DataTable();
  data.addColumn('date', 'Date');
  data.addColumn('number', 'Small Bags');
  data.addColumn('number', 'Medium Bags');
  data.addColumn('number', 'Large Bags');

  data.addRows([
    [new Date (2016, 8, 6), 2.3, 5, 4],
    [new Date (2016, 8, 13), 6.43, 2, 1],
    [new Date (2016, 8, 20), 4, 3, 3],
    [new Date (2016, 8, 27), 5, 4, 3],
  ]);

  var options = {
    title: 'AVOCADO BAGS',
    curveType: 'function',
    legend: { position: 'bottom' },
    hAxis: { format: "MM/dd/yy"},


  };

  var chart = new google.visualization.LineChart(document.getElementById('bags-chart'));

  chart.draw(data, options);
}

//get the two select params and when they change, redirect user
//to the new url with the new params

var select1 = document.getElementById("place");
var select2 = document.getElementById("convention");

function onChangeSelectors() {
  var place = select1.options[select1.selectedIndex].value;
  var convention = select2.options[select2.selectedIndex].value;
  window.location.href = "/home" + "?place=" + place + "&convention=" + convention;
}

select1.addEventListener("change", onChangeSelectors);
select2.addEventListener("change", onChangeSelectors);

