$(document).ready(function(){
    $("#add_input_row").click(function(e){
        $("#dynamic_container").append('<div id="dynamic_container"><input placeholder="Назва" name="a" required minlength="1" size="20"> <input placeholder="Кількість" name="b" required minlength="1" size="20"> <input type="button" value="Видалити ряд" id="delete_input_row"></div>')
    });

    $("#dynamic_container").on("click", "#delete_input_row", function(e){
        $(this).parent("div").remove();
    });
});