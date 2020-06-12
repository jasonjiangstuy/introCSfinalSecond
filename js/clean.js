function initial(){
   // only show submit image
   $('#Guide').hide()
}
$(document).ready(initial())
var stage = 0

// hide / show objects based on stage
function showStage(step){ 
   stage = stage + step
   if (stage == 0) {
      initial()
   }
   else if (stage == 1){
      
   }
}
function move(step){
   showStage(stage + step)
   
   
}

var guide = false
function toggleGuide(){
   if (guide == false){
      $('#formArea').hide('slow');
      guide = !guide;
      $('#Guide').show('slow');
   }else if (guide == true){
      $('#Guide').hide('slow');
      $('#formArea').show('slow');
      guide = !guide;
       // credit https://www.w3schools.com/howto/howto_js_scroll_to_top.asp
      //  document.body.scrollTop = 0; // For Safari
      //  document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
   }
   else{
      $('#Guide').hide();
      guide = false;
      $('#formArea').show('slow');
      // credit https://www.w3schools.com/howto/howto_js_scroll_to_top.asp
      // document.body.scrollTop = 0; // For Safari
      // document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE and Opera
   }
      
}


$("#form").submit(function(event){ 
//credit to https://www.sanwebe.com/2016/07/ajax-form-submit-examples-using-jquery
   event.preventDefault(); //prevent default action 
   var passward = $('#pwd').val()
   var cpassward = $('#cpwd').val()
   if (passward == cpassward){
       var post_url = $(this).attr("action"); //get form action url
       var request_method = $(this).attr("method"); //get form GET/POST method
       var form_data = $(this).serialize(); //Encode form elements for submission
       
       $.ajax({
           url : main.py,
           type: POST,
           data : form_data
       }).done(function(response){ //work on feedback div later
           $('#responseBox').html(response)
       })
   }else{
       $('#responseBox').html('Passwards must match. Please Try Again')
       
   }

});
