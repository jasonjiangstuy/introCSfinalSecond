$(document).ready(function(){
   initial();
}).ajaxSend(function(){alert('Image sent, Please Standby')})


var otow 
var otoh
var markerColorFinal
var backgroundColorFinal
var drawnImage = false;
var stage = 0

function second(){
   // only show dropper
   $('#Guide').hide('slow');
   $('#submitImg').hide('slow');
   $('#dropper').show('slow');
   $('#dropperPanel').hide('slow');
   $('#finalSubmit').hide()
}
function initial(){
   // only show submit image
   $('#responseImage').hide()
   stage = 0
   console.log('stage:', stage);
   console.log('start or restart');
   $('#finalSubmit').hide()
   $('#Guide').hide()
   $('#submitImg').show();
   $('#dropper').hide();
   $('#dropperPanel').hide();   
}

function rgbToHex(r, g, b) {
   if (r > 255 || g > 255 || b > 255){throw "Invalid color component";}
   else{return ((r << 16) | (g << 8) | b).toString(16);}
       
   
}

function eyeDropperMoveAction(e, which, me){
   console.log(which);
   //  * otow  * otoh
   var pixelData = me.getContext('2d').getImageData(e.offsetX, e.offsetY, 1, 1).data;
   $('#currentColor').css("background-color", 'rgba('+ pixelData[0] + ','+ pixelData[1] +','+ pixelData[2] + ','+ pixelData[3] +')');

}

function eyeDropperFinal(e, which, me){
   console.log(which);
   var pixelData = me.getContext('2d').getImageData(e.offsetX, e.offsetY, 1, 1).data;
   $('#currentColor').css("background-color", 'rgba('+ pixelData[0] + ','+ pixelData[1] +','+ pixelData[2] + ','+ pixelData[3] +')');
   if (which == 0){
      // marker
      $('#markerColor').css("background-color", 'rgba('+ pixelData[0] + ','+ pixelData[1] +','+ pixelData[2] + ','+ pixelData[3] +')');
      markerColorFinal = JSON.stringify([pixelData[0], pixelData[1], pixelData[2]])
      console.log(backgroundColorFinal); // figure out how to convert later
      move(0)

   }else if (which == 1){
      // background color
      $('#backColor').css("background-color", 'rgba('+ pixelData[0] + ','+ pixelData[1] +','+ pixelData[2] + ','+ pixelData[3] +')');
      backgroundColorFinal = JSON.stringify([pixelData[0], pixelData[1], pixelData[2]])
      console.log(markerColorFinal);
      move(0)
   }else{
      alert('That function isn\'t allowed')
      return
   }
}

function eyeDropper(which){
   if (stage == 1){
      // marker color
      if (which == 0){
         $('#DropperHeading').text('Pick the Marker Color to Continue')
         $('#mainCanvas').off('mousemove')
                        .mousemove(function(e) {eyeDropperMoveAction(e, which, this)})
                        .one('click', function(e) {
                           eyeDropperFinal(e, which, this);
                        });
      }
      // background color
      else if (which == 1){
         $('#DropperHeading').text('Pick the Background Color to Continue')
         $('#mainCanvas').off('mousemove')
                        .mousemove(function(e) {eyeDropperMoveAction(e, which, this)})
                        .one('click', function(e) {
                           eyeDropperFinal(e, which, this);
                        });
      }else{
         alert('That function isn\'t allowed')
         console.log(stage);
         return
      }
   }else{
      alert('That function isn\'t allowed at this stage')
      console.log(stage)
      return
   }
   $('#dropper').hide('slow');
   $('#dropperPanel').show('slow');
      
   
}
// hide / show objects based on stage


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
              var blockSprite = document.createElement("IMG");
              blockSprite.onload = function(){
                  var canvas = $('#mainCanvas')[0]
                  
                  otow = blockSprite.width / 300
                  otoh = blockSprite.height /620
                  canvas.width = 300;
                  canvas.height = 620; 
                  console.log(canvas);
                  c = canvas.getContext('2d')
                  c.drawImage(blockSprite, 0, 0, 300, 620);
                 
               }
               blockSprite.setAttribute("src", e.target.result); 
               //  .width(150)
               //  .height(200);
               
                  
               
               // call back
               second()
            };
            
            reader.readAsDataURL(myImg.files[0]);
            $('#picture').click(function(e){
               e.preventDefault();
               location.reload()
            })
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
   else if(stage == 2){
      //allow user to change variables// work in progress
      move(1)
      return
   }else if(stage == 3){
      // send ajax method to sever
      $('#dropper').hide('slow');   
      $('#finalSubmit').show('slow')
      $('#submit').one('click', submit);
                  // .click(submit);
                  //testing
      
   }
   // testing remove later
   else{//#endregion
      initial()
   }
}
function move(step, stop=false){
   if (stop){
      if (!backgroundColorFinal){
         alert('Please give us the background color')
         throw 'Stop step foward'
      }
      // if (!markerColorFinal){
      //    alert('Please give us the marker color')
      //    throw 'Stop step foward'
      // }
   }
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

   }
   else{
      $('#Guide').hide();
      guide = false;
      $('#formArea').show('slow');

   }
      
}

function opentab(code) {
   console.log(code);
   
   var win = window.open(code, '_blank');
   win.focus();
}


function submit(){
   //credit to https://www.sanwebe.com/2016/07/ajax-form-submit-examples-using-jquery
      // check all items are filled
      var go = true
      // if (!markerColorFinal || markerColorFinal == ''){
      //    go = false;
      //    alert('You have not specified the marker color, aborting')
      // }
      if (!backgroundColorFinal || backgroundColorFinal == ''){
         go = false;
         alert('You have not specified the background color, aborting')
      }

      var files = $('#picture')[0].files[0];

      if (!files){
         go = false;
      }

      var fd = new FormData();

      // console.log(markerColorFinal);
      console.log(backgroundColorFinal);
      
      fd.append('submit', 'True')
      fd.append('myImg',files);
      // fd.append('markerColor', markerColorFinal)
      fd.append('backgroundColor', backgroundColorFinal)
           

      if (go){
         // var fd = $(this).serialize(); //Encode form elements for submission
         console.log(fd);
         
         $.ajax({
            url : window.location.hostname + '/main.py',
            type: 'POST',
            processData: false,
            contentType: false,
            data : fd,
            success: function(data){
               window.location.href = data;
            },
            error: function(textStatus, error){
               alert(textStatus, error);
            }
         }).done(function(response){ //work on feedback div later
            console.log('request complete');
            alert('Image Processed')
         })
      }else{
         throw 'missing component of submission, aborting'
         
      }

}

