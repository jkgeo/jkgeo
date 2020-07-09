$('.ui.rating')
  .rating('disable')
;
$('.ui.accordion').accordion();

$('.ui.brewery.dropdown').dropdown({
    onChange: function(value, text){
      if (value == 'add'){
        $('#select-submit').hide();
        $('#add-brewery').show();
      } else {
        $('#add-brewery').hide();
        $('#select-submit').show();
      }
    }
  })
  
$('.ui.style.dropdown').dropdown({
    onChange: function(value, text){
      if (value == '0'){
        $('#add-style').show();
      } else {
        $('.ui.style.form').form('set value', 'style-name', '');
        $('#add-style').hide();
      }
    }
  })
  
$('.ui.substyle.dropdown').dropdown({
    onChange: function(value, text){
      if (value == '0'){
        $('#add-sub-style').show();
      } else {
        $('.ui.style.form').form('set value', 'sub-style-name', '');
        $('#add-sub-style').hide();
      }
    }
  })
  
$('#show-sub-style').on('click', function(){
  $('#select-sub-style').fadeToggle();
  $('.sub-style.icon').toggleClass('plus').toggleClass('minus');
  $('#show-sub-style span').text(function(i, text){
      if(text == 'Remove Sub-Style'){
        $('.ui.substyle.dropdown').dropdown('clear');
        $('.ui.style.form').form('set value', 'sub-style-name', '');
        return 'Add Sub-Style'
      } else {
        return 'Remove Sub-Style'
      }
  })
})

$('.ui.add-beer.dropdown').dropdown();