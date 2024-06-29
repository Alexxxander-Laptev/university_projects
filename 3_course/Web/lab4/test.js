$( document ).ready(function() {
    $("#btn").click(
		function(){
			sendAjaxForm();
			return false; 
		}
	);
});
 
function sendAjaxForm() {
    $.ajax({
        url:     "test.php",
        type:     "POST",
        dataType: "html",
        data: $("#ajax_form").serialize(),
        success: function(response) { //Данные отправлены
            // alert(response);
            var result = $.parseJSON(response);
            var form = document.getElementById('result_form');
            form.innerHTML = '';
            console.log(form);
            result.forEach(element => {
                var str = `
                <div>
                <h3>${element['date'][0]}</h3>
                <ul>
                `;
                // console.log(element);
                element['data'].forEach(el => {
                    str += `<dt id='tabtd'>${el['surename']} ${el['name']} ${el['gr_vis']} ${el['pres']}</dt>`
                })
                str += `</ul></div>`;
                form.innerHTML += str;
            }); 

    	},
    	error: function(response) { // Данные не отправлены
            $('#result_form').html('Ошибка. Данные не отправлены.');
    	}
 	});
    
}
function sorttest(num){
    if (num == 1) {
        document.cookie = 'sort=ORDER BY `surename`';
    } else if(num == 2) {
        
        document.cookie = 'sort=ORDER BY `present_absent` DESC';
    }
    // console.log(num);
    sendAjaxForm();
}