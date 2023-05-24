var place = "Houston";
var conv = "Organic";

var avoPrice = JSON.parse(document.getElementById("avoPrice").innerHTML);
var avoVolume = JSON.parse(document.getElementById("avoVolume").innerHTML);
var avoBaggage = JSON.parse(document.getElementById("avoBaggage").innerHTML);
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
    title: 'AVOCADO PRICES: ',
    curveType: 'function',
    colors: ['#AA471F'],
    legend: { position: 'bottom' },
    hAxis: { format: "MM/dd/yy"}

  };

  var chart = new google.visualization.LineChart(document.getElementById('main-chart'));

  chart.draw(data, options);
}

function drawVolumeChart(volData) {
  var data = new google.visualization.DataTable();
  data.addColumn('date', 'Date');
  data.addColumn('number', 'Avocado');

  dates = Object.keys(avoVolume);
  console.log(dates);
  for (var i = 0; i < dates.length; i++) {
    var date = dates[i];
    var vol = avoVolume[date];
    data.addRow([new Date(date), vol]);

  }

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
  data.addColumn('number', 'Large Bags');
  data.addColumn('number', 'Medium Bags');

  for (var i = 0; i < dates.length; i++) {
    var date = dates[i];
    var small = avoBaggage[0][date];
    var large = avoBaggage[1][date];
    var extralarge = avoBaggage[2][date];
    data.addRow([new Date(date), small, large, extralarge]);

  }

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
      avoVolume = JSON.parse(jsonny["avoVolume"])
      avoBaggage = JSON.parse(jsonny["avoBaggage"])
      console.log(avoPrice)
      drawPriceChart(convention, place, avoPrice);
      drawVolumeChart(avoVolume);
      drawBagsChart(avoBaggage)
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

