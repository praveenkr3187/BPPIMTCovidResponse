  var getstate = $.get('/state');
getstate.done(function(state){
for(var i=0;i<34;i++){
    document.getElementById("sel2").innerHTML += '<option value="'+state.state[i]+'">'+state.state[i]+'</option>';
}
});

$(document).ready(function() {

  $("#sel2").change(function() {

    var datastate = $(this).val() ;
    document.getElementById("sel1").innerHTML="";
    console.log(datastate);
        $.ajax({
            type: "POST",
            url: "/df2",
            data: { st : datastate } 
        }).done(function(df2){
          for(var i=0;i<df2.district.length;i++){
            document.getElementById("sel1").innerHTML += '<option value="'+df2.district[i]+'">'+df2.district[i]+'</option>';
                            }
        });

  });

});

function fung(){
    var ds=$("#sel1").val();
    $.ajax({
            type: "POST",
            url: "/district",
            data: { district : ds } 
        }).done(function(df2){
        console.log(ds);
document.getElementById("g").innerHTML = "";
document.getElementById("g").innerHTML ="<canvas id='disj' ></canvas>";
var getData2 = $.get('/disj');
getData2.done(function(disj){
    var ctx = document.getElementById('disj').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'bar',
        // The data for our dataset
        data: {
            labels: ["Density","Workplaces","Residential","Retail","Grocery","Parks","Stations","Air quality","Water accessibility","Thermal anomalies","Confirmed","Active"],
            datasets: [{
                label: ds,
                fill: true,
                borderWidth: 1,
                borderColor: 'rgb(255, 0, 30)',
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
        });


}

var getData3 = $.get('/getChartData');
getData3.done(function(data){
    var ctxa = document.getElementById('a').getContext('2d');
    var charta = new Chart(ctxa, {
        // The type of chart we want to create
        type: 'pie',
        // The data for our dataset
        data: {
            labels: data.fIKeys,
            datasets: [{
                label: 'District',
                fill: true,
                borderWidth: 1,
                backgroundColor: 'rgb(255, 0, 30)',
                backgroundColor: ["red", "blue", "green", "yellow", "pink","orange","purple","red", "blue", "green", "yellow", "pink","orange","purple"],
                data: data.fIvalues
            }]
        },

        // Configuration options go here

    });

    var ctxb = document.getElementById('b').getContext('2d');
    var chartb = new Chart(ctxb, {
        // The type of chart we want to create
        type: 'pie',
        // The data for our dataset
        data: {
            labels: data.fIMKeys,
            datasets: [{
                label: 'District',
                fill: true,
                borderWidth: 1,
                backgroundColor: 'rgb(255, 0, 30)',
                backgroundColor: ["red", "blue", "green", "yellow", "pink","orange","purple","red", "blue", "green", "yellow", "pink","orange","purple"],
                data: data.fIMValues
            }]
        },

        // Configuration options go here

    });

    var ctxc = document.getElementById('c').getContext('2d');
    var chartc = new Chart(ctxc, {
        // The type of chart we want to create
        type: 'pie',
        // The data for our dataset
        data: {
            labels: data.uSKeys,
            datasets: [{
                label: 'District',
                fill: true,
                borderWidth: 1,
                backgroundColor: 'rgb(255, 0, 30)',
                backgroundColor: ["red", "blue", "green", "yellow", "pink","orange","purple","red", "blue", "green", "yellow", "pink","orange","purple"],
                data: data.uSValues
            }]
        },

    });

    var ctxd = document.getElementById('d').getContext('2d');
    var chartd = new Chart(ctxd, {
        // The type of chart we want to create
        type: 'pie',
        // The data for our dataset
        data: {
            labels: data.uSMKeys,
            datasets: [{
                label: 'District',
                fill: true,
                borderWidth: 1,
                backgroundColor: 'rgb(255, 0, 30)',
                backgroundColor: ["red", "blue", "green", "yellow", "pink","orange","purple","red", "blue", "green", "yellow", "pink","orange","purple"],
                data: data.uSMValues
            }]
        },

        // Configuration options go here
    });
});
