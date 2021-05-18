
window.onbeforeunload = function () {
  localStorage.clear();
}

async function submitFilter() {
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
        indicator: document.getElementById("indicator").value,
        intradayMode: document.getElementById("intraday-mode").checked
    }
    
    await $.post(
        "/api/v1/stockdetail", 
        data,
        function(data, status){
          if (status == "success") {
            const name = JSON.parse(data).name;
            document.getElementById('stock-name').innerHTML = name;
            localStorage.setItem('graphData', data);
          } 
        }
    )
    

    // Initializing line chart
    onLineTab();
}

// Colors
var colors = {
  gray: {
    100: '#f6f9fc',
    200: '#e9ecef',
    300: '#dee2e6',
    400: '#ced4da',
    500: '#adb5bd',
    600: '#8898aa',
    700: '#525f7f',
    800: '#32325d',
    900: '#212529'
  },
  theme: {
    'default': '#172b4d',
    'primary': '#5e72e4',
    'secondary': '#f4f5f7',
    'info': '#11cdef',
    'success': '#2dce89',
    'danger': '#f5365c',
    'warning': '#fb6340'
  },
  black: '#12263F',
  white: '#FFFFFF',
  transparent: 'transparent',
};

function parseData(type) {
  if (type === 'line') {
    var parsed_values = [];
    data = JSON.parse(localStorage.getItem('graphData'));
    data.graph_data.forEach(i => {
      var temp = {
        x: new Date(i.date).getTime(),
        y: i.close.toFixed(2)
      };
      parsed_values.push(temp);
    });
    return parsed_values;
  }

  if (type == 'candlestick') {
    var parsed_values = []
    data = JSON.parse(localStorage.getItem('graphData'));
    data.graph_data.forEach(i => {
      var temp = {
        x: new Date(i.date).getTime(),
        y: [i.open.toFixed(2), i.high.toFixed(2), i.low.toFixed(2), i.close.toFixed(2)]
      };
      parsed_values.push(temp);
    });
    return parsed_values;
  }

  if (type == 'indicator') {
    var parsed_values = []
    data = JSON.parse(localStorage.getItem('graphData'));
    data.graph_data.forEach(i => {
      var temp = {
        x: new Date(i.date).getTime(),
        y: [i.indicator.toFixed(2)]
      };
      parsed_values.push(temp);
    });
    return parsed_values;
  }
}


function onLineTab() {
  try {
    var data = JSON.parse(localStorage.getItem('graphData'));
    var series = [];
    if ( data.indicator != null ){
      series.push({
        name: data.indicator,
        data: parseData('indicator')
      });
    }

    series.push({
      name: "Close Price",
      data: parseData('line')
    });

    var options = {
      chart: {
        type: 'line',
        height: 350,
        sparkline: {
          enabled: true,
        }
      },
      colors: [colors.gray[200], colors.theme.primary],
      dataLabels: {
        enabled: false
      },
      markers: {
        size: 0,
      },
      stroke: {
        curve: 'smooth',
      },
      series: series,
      xaxis: {
        type: 'datetime'
      }
    }
    
    var chartDiv = document.getElementById('chart');
    chartDiv.innerHTML = null;
    var chart = new ApexCharts(chartDiv, options);
    chart.render();
    
  } catch (e) {
    console.log(e)
  }
  
}

function onCandleTab() {
  try {

    var data = JSON.parse(localStorage.getItem('graphData'));
    var series = [];
    if ( data.indicator != null ){
      series.push({
        type: 'line',
        name: data.indicator,
        data: parseData('indicator')
      });
    }

    series.push({
      type: 'candlestick',
      data: parseData('candlestick')
    });

    var options = {
      chart: {
        height: 350,
        sparkline: {
          enabled: true,
        }
      },
      series: series,
      plotOptions: {
        candlestick: {
          colors: {
            upward: colors.gray[200],
            downward: colors.theme.primary
          }
        }
      },
      xaxis: {
        type: 'datetime',
      }
    }
    
    if (data.indicator == null) {
      options.chart.type = 'candlestick'
    } else {
      options.tooltip = {
        shared: true,
        custom: [function({seriesIndex, dataPointIndex, w}) {
          return ''
        }, function({ seriesIndex, dataPointIndex, w }) {
          var o = w.globals.seriesCandleO[seriesIndex][dataPointIndex]
          var h = w.globals.seriesCandleH[seriesIndex][dataPointIndex]
          var l = w.globals.seriesCandleL[seriesIndex][dataPointIndex]
          var c = w.globals.seriesCandleC[seriesIndex][dataPointIndex]
          return (
            `Open: ${o}\nHigh: ${h}\nLow: ${l}\nClose: ${c}`
          )
        }]
      }

      options.stroke = {
        width: [3, 1]
      }
    }


    var chartDiv = document.getElementById('chart');
    chartDiv.innerHTML = null;
    var chart = new ApexCharts(chartDiv, options);
    chart.render();

  } catch (error) {
    console.log(error);
  }
  
}
