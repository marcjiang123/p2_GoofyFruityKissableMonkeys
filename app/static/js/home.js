var place = "Houston";
var conv = "Organic";

var avoPrice = JSON.parse(document.getElementById("avoPrice").innerHTML);
// var avoVolume = JSON.parse(document.getElementById("avoVolume").innerHTML);
place = document.getElementById("place").innerHTML;
conv = document.getElementById("convention").innerHTML;

google.charts.load('current', {'packages':['corechart']});
console.log("first time?")
google.charts.setOnLoadCallback(drawPriceChart, place, conv, avoPrice);
console.log("It worked?")
google.charts.setOnLoadCallback(drawVolumeChart);
google.charts.setOnLoadCallback(drawBagsChart);


function drawPriceChart(avocado_type, location, avoData) {
  var data = new google.visualization.DataTable();
  data.addColumn('date', 'Date');
  data.addColumn('number', 'Avocado');

  //Loop thru the data and add said rows
  dates = Object.keys(avoPrice);
  console.log(dates);
  for (var i = 0; i < dates.length; i++) {
    var date = dates[i];
    var price = avoPrice[date];
    data.addRow([new Date(date), price]);

  }

  var options = {
    title: 'AVOCADO PRICES: ' + avocado_type + 'in ' + location,
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



function drawBagsChart(bagData) {
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
  place = select1.options[(select1.selectedIndex)].value;
  console.log(place)
  convention = select2.options[select2.selectedIndex].value;
  var dataFromForm = new FormData();

  dataFromForm.append("json", JSON.stringify({
    place: place, 
    convention: convention, 
    help: "help"
  }) );
  fetch('/home', {  
    method: 'POST',
    body: dataFromForm,
  }).then(response => {
    if(response.status == 200){
        return response.json();
    } else {
        // handle this somehow
    }
  }).then(json => {
      //console.log('Success! ' + JSON.stringify(json))
      jsonny = JSON.stringify(json)
      jsonny = JSON.parse(jsonny)
      avoPrice = JSON.parse(jsonny["avoPrice"])
      // avoVolume = JSON.parse(jsonny["avoVolume"])
      console.log(avoPrice)
      drawPriceChart(convention, place, avoPrice);
      // drawVolumeChart(avoVolume);
  }).catch(error => {
      console.log('error with access token req!')
  });
  //avoPrice = JSON.parse(document.getElementById("avoPrice").innerHTML);
  console.log(avoPrice)
}

// function onLoadSelectors() {
//   var place = select1.options[select1.selectedIndex].value;
//   var convention = select2.options[select2.selectedIndex].value;
//   drawPriceChart(convention, place, avoPrice)
//   window.location.href = "/home" + "?place=" + place + "&convention=" + convention;
// }

//select1.addEventListener("load", onLoadSelectors)

select1.addEventListener("change", onChangeSelectors);
select2.addEventListener("change", onChangeSelectors);

