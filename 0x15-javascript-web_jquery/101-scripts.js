$(document).ready(function(){
$('#add_item').click(function(){
$('<li>Item</li>').appendTo('.my_list);

});
$('#remove_item').click(function(){
$("li:last-child").remove();

});
$('#clear_list').click(function(){
$('li').remove();
});

)}
