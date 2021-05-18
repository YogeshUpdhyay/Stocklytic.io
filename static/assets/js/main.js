
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
            console.log("here")
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
    console.log(data)
    data.forEach(i => {
      var temp = {
        x: new Date(i.date).getTime(),
        y: i.close.toFixed(2)
      };
      parsed_values.push(temp);
    });
    console.log(parsed_values);
    return parsed_values;
  }

  if (type == 'candlestick') {
    var parsed_values = []
    data = JSON.parse(localStorage.getItem('graphData'));
    data.forEach(i => {
      var temp = {
        x: new Date(i.date).getTime(),
        y: [i.open.toFixed(2), i.high.toFixed(2), i.low.toFixed(2), i.close.toFixed(2)]
      };
      parsed_values.push(temp);
    });
    console.log(parsed_values);
    return parsed_values;
  }
}


function onLineTab() {
  try {
    var data = JSON.parse(localStorage.getItem('graphData'));
    var series = [];
    if ( data.indicator != null ){
      series.push(parseData('indicator'));
    }

    series.push(parseData('line'));


    var options = {
      chart: {
        type: 'line',
        height: 350,
        sparkline: {
          enabled: true,
        }
      },
      colors: [colors.gray[200]],
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
    var options = {
      chart: {
        type: 'candlestick',
        height: 350,
        sparkline: {
          enabled: true,
        },
      },
      series: [{
        data: parseData('candlestick')
      }],
      plotOptions: {
        candlestick: {
          colors: {
            upward: colors.gray[200],
            downward: colors.theme.primary
          }
        }
      },
      xaxis: {
        type: 'datetime'
      },
      yaxis: {
        tooltip: {
          enabled: true
        }
      },
    }
    
    var chartDiv = document.getElementById('chart');
    chartDiv.innerHTML = null;
    var chart = new ApexCharts(chartDiv, options);
    chart.render();

  } catch (error) {
    console.log(error);
  }
  
}
