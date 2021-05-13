$("#link_questions").click(function(){
  window.location = "/questions";
})

$("#link_users").click(function(){
  window.location = "/users";
})

$("#return_home").click(function(){
  window.location = "/";
})

$('table tr td:nth-child(5)').click(function(){
  index = $('table tr td:nth-child(5)').index(this);
  console.log(index);
  window.open($(this).text(), '_blank');
  })
