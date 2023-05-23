google.charts.load('current', {'packages':['corechart']});

const delay = ms => new Promise(res => setTimeout(res, ms));

//avocado is a boolean
//if they clicked avocado, then true
//if they clicked the other stock, then false
async function whenClicked(stock,avocado_data,stock_data, location, avocado_type, avocado) {
  var data = new google.visualization.DataTable();
  var avocadoName = `${location} ${avocado_type} Avocados`

  var x = new URLSearchParams(window.location.search);
  
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
  
  await delay(2000)

  var right = determineRightWrong(avocado, avocado_data, stock_data);
  const urlParams = new URLSearchParams(window.location.search);
  const score = urlParams.get('score');
  console.log(avocado)
  if (right) {
    alert("You got it right!")
    if (score == null) {
      window.location.assign(window.location.origin + `/higher-Lower?score=1`);
    } else {
      window.location.assign(window.location.origin + `/higher-Lower?score=${parseInt(score) + 1}`);
    }
  
  } else {
    alert("WRONG!!!")
    if (score == null) {
      window.location.assign(window.location.origin + `/you-lost?score=0`);
    } else {
      window.location.assign(window.location.origin + `/you-lost?score=${score}`);
    }
  }
  


}


function determineRightWrong(userGuess, avocado_data, stock_data) {

  lastAvocadoPrice = avocado_data[Object.keys(avocado_data)[Object.keys(avocado_data).length - 1]];
  lastStockPrice = stock_data[Object.keys(stock_data)[Object.keys(stock_data).length - 1]];
  console.log(userGuess, lastAvocadoPrice, lastStockPrice)
  return userGuess == (lastAvocadoPrice > lastStockPrice);
}