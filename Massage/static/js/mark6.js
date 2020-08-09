
function iconfive() {


	if(document.getElementById("icon5_fail").hidden != true){


		for (var i = 1; i <= 5; i++) {
			var fail_elements = document.getElementById("icon" + String(i) + "_fail");
			fail_elements.hidden = true;
			var normal_elements = document.getElementById("icon" + String(i));
			normal_elements.hidden = false;
			
		}

		for (var b = 1; b<= 5; b++){
			if (b == 5){
				continue;
			}
			var inputs = document.getElementById("input" + String(b));
			inputs.disabled = true;

		}


	}else{

		for (var i = 1; i <= 5; i++) {
			var fail_elements = document.getElementById("icon" + String(i) + "_fail");
			fail_elements.hidden = false;
			var normal_elements = document.getElementById("icon" + String(i));
			normal_elements.hidden = true;
		}

		for (var b = 1; b<= 5; b++){
			var inputs = document.getElementById("input" + String(b));
			inputs.disabled = false;

		}

	}
}


function iconfour(){
	if(document.getElementById("icon4_fail").hidden != true){
		for (var i = 1; i <= 4; i++) {
			var fail_elements = document.getElementById("icon" + String(i) + "_fail");
			fail_elements.hidden = true;
			var normal_elements = document.getElementById("icon" + String(i));
			normal_elements.hidden = false;
		}

		for (var b = 1; b<= 5; b++){
			if (b == 4){
				continue;
			}
			var inputs = document.getElementById("input" + String(b));
			inputs.disabled = true;

		}

	}else{
		for (var i = 1; i <= 5; i++) {
			var fail_elements = document.getElementById("icon" + String(i) + "_fail");
			fail_elements.hidden = false;
			var normal_elements = document.getElementById("icon" + String(i));
			normal_elements.hidden = true;
		}

		for (var b = 1; b<= 5; b++){
			var inputs = document.getElementById("input" + String(b));
			inputs.disabled = false;

		}

	}

}

function iconthree(){
	if(document.getElementById("icon3_fail").hidden != true){
		for (var i = 1; i <= 3; i++) {
			var fail_elements = document.getElementById("icon" + String(i) + "_fail");
			fail_elements.hidden = true;
			var normal_elements = document.getElementById("icon" + String(i));
			normal_elements.hidden = false;
		}

		for (var b = 1; b<= 5; b++){
			if (b == 3){
				continue;
			}
			var inputs = document.getElementById("input" + String(b));
			inputs.disabled = true;

		}

	}else{
		for (var i = 1; i <= 5; i++) {
			var fail_elements = document.getElementById("icon" + String(i) + "_fail");
			fail_elements.hidden = false;
			var normal_elements = document.getElementById("icon" + String(i));
			normal_elements.hidden = true;
		}

		for (var b = 1; b<= 5; b++){
			var inputs = document.getElementById("input" + String(b));
			inputs.disabled = false;

		}


	}	

}

function icontwo(){
	if(document.getElementById("icon2_fail").hidden != true){
		for (var i = 1; i <= 2; i++) {
			var fail_elements = document.getElementById("icon" + String(i) + "_fail");
			fail_elements.hidden = true;
			var normal_elements = document.getElementById("icon" + String(i));
			normal_elements.hidden = false;
		}

		for (var b = 1; b<= 5; b++){
			if (b == 2){
				continue;
			}
			var inputs = document.getElementById("input" + String(b));
			inputs.disabled = true;

		}

	}else{
		for (var i = 1; i <= 5; i++) {
			var fail_elements = document.getElementById("icon" + String(i) + "_fail");
			fail_elements.hidden = false;
			var normal_elements = document.getElementById("icon" + String(i));
			normal_elements.hidden = true;
		}

		for (var b = 1; b<= 5; b++){
			var inputs = document.getElementById("input" + String(b));
			inputs.disabled = false;

		}


	}		
}

function iconone(){
	if(document.getElementById("icon1_fail").hidden != true){
		for (var i = 1; i <= 1; i++) {
			var fail_elements = document.getElementById("icon" + String(i) + "_fail");
			fail_elements.hidden = true;
			var normal_elements = document.getElementById("icon" + String(i));
			normal_elements.hidden = false;
		}

		for (var b = 1; b<= 5; b++){
			if (b == 1){
				continue;
			}
			var inputs = document.getElementById("input" + String(b));
			inputs.disabled = true;

		}

	}else{
		for (var i = 1; i <= 5; i++) {
			var fail_elements = document.getElementById("icon" + String(i) + "_fail");
			fail_elements.hidden = false;
			var normal_elements = document.getElementById("icon" + String(i));
			normal_elements.hidden = true;
		}

		for (var b = 1; b<= 5; b++){
			var inputs = document.getElementById("input" + String(b));
			inputs.disabled = false;

		}


	}
}