var getData = $.get('/df2');
getData.done(function(df2){
console.log(df2.district[0]);
for(var i=0;i<692;i++){
    document.getElementById("sel1").innerHTML += '<option value="'+df2.district[i]+'">'+df2.district[i]+'</option>';
}
});