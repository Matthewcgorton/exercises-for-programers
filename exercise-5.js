$(document).ready(


  function() {
    function display_results() {
      $( "#sum" ).html( "Sum: " + (Number($("#number_1").val()) + Number($("#number_2").val()))  )
      $( "#subtraction" ).html( "Difference: " + (Number($("#number_1").val()) - Number($("#number_2").val())) )
      $( "#multiply" ).html( "Product: " + (Number($("#number_1").val()) * Number($("#number_2").val())) )
      $( "#divide" ).html( "Division: " + (Number($("#number_1").val()) / Number($("#number_2").val())) )
    }

    $( "#number_1" ).keyup(function() {
      display_results();
    });

    $( "#number_2" ).keyup(function() {
      display_results();
    });

  }
)
