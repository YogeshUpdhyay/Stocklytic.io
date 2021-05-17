
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
}


function onLineTab() {
  try {
    var options = {
      chart: {
        type: 'line',
        stacked: false,
        height: 350,
        zoom: {
          type: 'x',
          enabled: true,
          autoScaleYaxis: true
        },
        toolbar: {
          autoSelected: 'zoom'
        },
        sparkline: {
          enabled: true,
        },
        tooltip: {
          enabled: false
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
      series: [{
        name: 'Close Price',
        data: parseData('line')
      }],
      xaxis: {
        type: 'datetime'
      }
    }
    
    var chart = new ApexCharts(document.getElementById('chart'), options);
    
    chart.render();
  } catch (e) {
    console.log(e)
  }
  
}

function onCandleTab() {
  var options = {
    chart: {
      type: 'candlestick',
    },
    series: {
      data: parseData('candlestick')
    }
  }
}
