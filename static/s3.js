var getData = $.get('/disj');
getData.done(function(disj){
    var ctx = document.getElementById('disdis').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',
        // The data for our dataset
        data: {
            labels: ["Density","Workplaces","Residential","Retail","Grocery","Parks","Stations","Air quality","Water accessibility","Thermal anomalies","Confirmed","Active"],
            datasets: [{
                label: 'District',
                fill: true,
                borderWidth: 1,
                backgroundColor: 'rgb(255, 0, 30)',
                backgroundColor: ["red", "blue", "green", "yellow", "pink","orange","purple","red", "blue", "green", "yellow", "pink","orange","purple"],
                data: disj.a
            }]
        },

        // Configuration options go here
        options: {
            scales: {
                xAxes: [{
                   gridLines: {
                      display: true
                   },
                   scaleLabel: {
                    display: true,
                    labelString: ''
                  }
                }],
                yAxes: [{
                   gridLines: {
                      display: true
                   },
                   scaleLabel: {
                    display: true,
                    labelString: ''
                  }
                }]
             }
        }
    });
});