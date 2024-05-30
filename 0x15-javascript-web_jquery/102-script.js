$(document).ready(function(){
  $("#btn_translate").click(function(){
	  var x = $('#language_code').val();
    $.post("https://www.fourtonfish.com/hellosalut/hello/",{language_code : x}, function(data, status){
      $('#hello').text(data);
    });
  });
});
