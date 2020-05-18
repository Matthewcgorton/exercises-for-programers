$(document).ready(

  function() {
    // alert("loaded")
    $( "#lname" ).keyup(function() {
      console.log( "String length ", $("#lname").val().length );

      $( "#chars_count" ).html( " characters: " + $("#lname").val().length)
    });


    }
)
