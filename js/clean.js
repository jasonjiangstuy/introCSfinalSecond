
$(document).ready(function(){
   initial();
})
var stage = 0
function second(){

   $('#Guide').hide('slow');
   $('#submitImg').hide('slow');
   $('#dropper').show('slow');
}
function initial(){
   // only show submit image
   
   stage = 0
   console.log('stage:', stage);
   console.log('start or restart');
   $('#Guide').hide('slow')
   $('#dropper').hide('slow');
   $('#submitImg').show('slow');
}
// hide / show objects based on stage

var drawnImage = false;
function showStage(step){ 

   stage = stage + step
   console.log('stage:', stage);
   
   if (stage == 0) {
      initial();
   }
   else if (stage == 1){
      var myImg = $('#picture')
      var imgVal = myImg.val(); 
      if(imgVal=='') { 
         alert("empty input file, please try again"); 
         // back to start
         initial();

      }
      // // test if img is an animated gif
      // var fs = require('fs')
      // , animated = require('animated-gif-detector');



      else if (myImg[0].files && myImg[0].files[0] && FileReader) {
         if (!drawnImage){
            myImg = myImg[0] // change to native js
            var reader = new FileReader();
            reader.onload = function (e) {
              var blockSprite = new Image();
              blockSprite.src = e.target.result;
              blockSprite.onload = function(){
                  var canvas = $('#mainCanvas')[0]
                  canvas.style.width = blockSprite.naturalWidth;
                  canvas.style.height = blockSprite.naturalHeight; 
                  console.log(canvas);
                  c = canvas.getContext('2d')
                  c.drawImage(blockSprite, 0, 0);
               }
               //  .width(150)
               //  .height(200);
               
                  
               
               // call back
               second()
            };
            
            reader.readAsDataURL(myImg.files[0]);
            drawnImage = true;
         }else{
            second()
         }
         
         

         
         
       }
      else{
         alert("Your browser doesnt support the FileReader API please try using another browser"); 
         // back to start
         initial();
      }
      
      

   }
   // testing
   else{
      initial()
   }
}
function move(step){
   showStage(step)   
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
