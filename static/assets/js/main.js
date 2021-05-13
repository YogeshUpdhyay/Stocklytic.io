
window.onbeforeunload = function () {
  localStorage.clear();
}

function submitFilter() {
    // ticker field validation
    if (document.getElementById("ticker").value == ""){
        document.getElementById("ticker").className = "form-control is-invalid"
        return;
    } else {
        document.getElementById("ticker").className = "form-control"
    }

    // graph api call
    let data = {
        ticker: document.getElementById("ticker").value,
        startDate: document.getElementById("start-date").value,
        endDate: document.getElementById("end-date").value,
        indicator: document.getElementById("indicator").value,
        intradayMode: document.getElementById("intraday-mode").checked
    }
    
    let graphData;
    $.post(
        "/api/v1/stockdetail", 
        data,
        function(data, status){
            graphData = data;
        }
    )
    
    graphData = {
      labels: ['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
      datasets: [{
        label: 'Performance',
        data: [0, 20, 10, 30, 15, 40, 20, 60, 60]
      }]
    }

    localStorage.setItem('graphData', JSON.stringify(graphData));

    // Initializing line chart
    onLineTab();
}

function onLineTab() {
  console.log("Rendering chart")
  try {
    var options = {
      chart: {
        type: 'line'
      },
      series: [{
        name: 'sales',
        data: [30,40,35,50,49,60,70,91,125]
      }],
      xaxis: {
        categories: [1991,1992,1993,1994,1995,1996,1997, 1998,1999]
      }
    }
    
    var chart = new ApexCharts(document.getElementById('chart'), options);
    
    chart.render();
  } catch (e) {
    console.log(e)
  }
  

}

function onCandleTab() {
  var chart = $('#chart-stock-dark');
  var barCount = 60;
  var initialDateStr = '01 Apr 2017 00:00 Z';

  var candlechart = new Chart(chart, {
    type: 'candlestick',
    data: {
      datasets: [{
        label: 'CHRT - Chart.js Corporation',
        data: getRandomData(initialDateStr, barCount)
      }]
    }
  });
  
  var getRandomInt = function(max) {
    return Math.floor(Math.random() * Math.floor(max));
  };
  
  function randomNumber(min, max) {
    return Math.random() * (max - min) + min;
  }
  
  function randomBar(date, lastClose) {
    var open = +randomNumber(lastClose * 0.95, lastClose * 1.05).toFixed(2);
    var close = +randomNumber(open * 0.95, open * 1.05).toFixed(2);
    var high = +randomNumber(Math.max(open, close), Math.max(open, close) * 1.1).toFixed(2);
    var low = +randomNumber(Math.min(open, close) * 0.9, Math.min(open, close)).toFixed(2);
    return {
      x: date.valueOf(),
      o: open,
      h: high,
      l: low,
      c: close
    };
  
  }
  
  function getRandomData(dateStr, count) {
    var date = luxon.DateTime.fromRFC2822(dateStr);
    var data = [randomBar(date, 30)];
    while (data.length < count) {
      date = date.plus({days: 1});
      if (date.weekday <= 5) {
        data.push(randomBar(date, data[data.length - 1].c));
      }
    }
    return data;
  }
}