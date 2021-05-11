
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
      
    var $chart = $('#chart-sales-dark');
    
    console.log($chart)
      
    // Methods
      
    function init($chart) {
        var salesChart = new Chart($chart, {
            type: 'line',
            options: {
              scales: {
                yAxes: [{
                  gridLines: {
                    lineWidth: 1,
                    color: Charts.colors.gray[900],
                    zeroLineColor: Charts.colors.gray[900]
                  },
                  ticks: {
                    callback: function(value) {
                      if (!(value % 10)) {
                        return '$' + value + 'k';
                      }
                    }
                  }
                }]
              },
              tooltips: {
                callbacks: {
                  label: function(item, data) {
                    var label = data.datasets[item.datasetIndex].label || '';
                    var yLabel = item.yLabel;
                    var content = '';
      
                    if (data.datasets.length > 1) {
                      content += '<span class="popover-body-label mr-auto">' + label + '</span>';
                    }
      
                    content += `$${yLabel}k`
                    
                    return content;
                  }
                }
              }
            },
            data: {
              labels: ['May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
              datasets: [{
                label: 'Performance',
                data: [0, 20, 10, 30, 15, 40, 20, 60, 60]
              }]
            }
        });
    }

    // Events
    
    if ($chart.length) {
        init($chart);
    }
}
                            