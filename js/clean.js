$(document).ready(function(){
   // set inital values
   $('.email').hide()
   $('.cpwd').hide()
   $('#Guide').hide()
})

function switchNew(){
   $('#formArea').hide('slow', function(){
       $('#heading').text('New Users')
       $('#whichForm').val('Choice')
       $('#switch').text('Returning Users')
                   .attr('onclick', 'switchOld()')
       $('#submit').text('Make Account')
       $('#forgotPwd').hide()
       $('.email').show()
       $('.cpwd').show()
       $('#formArea').show('slow')
   })
   
   

}
function switchOld(){
   $('#formArea').hide('slow', function(){
       $('#heading').text('Login')
       $('#whichForm').val('Auto')
       $('#switch').text('New User')
                   .attr('onclick', 'switchNew()')
       $('#submit').text('Login')
       $('.email').hide()
       $('.cpwd').hide()
       $('#forgotPwd').show()
       $('#formArea').show('slow')
   })
   
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

