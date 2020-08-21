/* This code was made to maintain the functionality of 
   review mark machanism.There are 5 sections for the five 
   stars.Each of them has 4 functions made for such events as:
   -> mouseover
   -> mouseout
   -> click

*/



//This section works for the elements with id 'icon5'


//This func made for the mouseover event
function iconfive_over() {

    for (var i = 1; i <= 5; i++) {
        var fail_elements = document.getElementById("icon" + String(i) + "_fail");
        fail_elements.hidden = true;
        var normal_elements = document.getElementById("icon" + String(i));
        normal_elements.hidden = false;

    }

    for (var b = 1; b <= 5; b++) {
        if (b == 5) {
            continue;
        }
        var inputs = document.getElementById("input" + String(b));
        inputs.disabled = true;

    }

    var elem = document.getElementById("icon5");
    elem.addEventListener("mouseout", iconfive_out);

}

//This func was made for the mouseout event
function iconfive_out() {

    for (var i = 1; i <= 5; i++) {
        var fail_elements = document.getElementById("icon" + String(i) + "_fail");
        fail_elements.hidden = false;
        var normal_elements = document.getElementById("icon" + String(i));
        normal_elements.hidden = true;
    }

    for (var b = 1; b <= 5; b++) {
        var inputs = document.getElementById("input" + String(b));
        inputs.disabled = false;

    }
}


//This func was made for the click event
function iconfive_click() {

    if (document.getElementById("icon5_fail").hidden == true) {
        var elem = document.getElementById("icon5");
        elem.removeEventListener("mouseout", iconfive_out);
        elem.removeEventListener("click", iconfive_click);
        elem.addEventListener("click", icon_five_click_off);
    }


}

//This func was made as the addition for the click event for that when you want to turn off the stars
function icon_five_click_off() {


    for (var i = 1; i <= 5; i++) {
        var fail_elements = document.getElementById("icon" + String(i) + "_fail");
        fail_elements.hidden = false;
        var normal_elements = document.getElementById("icon" + String(i));
        normal_elements.hidden = true;
    }

    for (var b = 1; b <= 5; b++) {
        var inputs = document.getElementById("input" + String(b));
        inputs.disabled = false;

    }

    var elem = document.getElementById("icon5");
    elem.addEventListener("mouseout", iconfive_out);
    elem.addEventListener("click", iconfive_click);
    elem.removeEventListener("click", icon_five_click_off);
}


//This section works for the elements with id 'icon4'

//This func made for the mouseover event
function iconfour_over() {

    for (var i = 1; i <= 4; i++) {
        var fail_elements = document.getElementById("icon" + String(i) + "_fail");
        fail_elements.hidden = true;
        var normal_elements = document.getElementById("icon" + String(i));
        normal_elements.hidden = false;

    }

    for (var b = 1; b <= 5; b++) {
        if (b == 4) {
            continue;
        }
        var inputs = document.getElementById("input" + String(b));
        inputs.disabled = true;

    }

    var elem = document.getElementById("icon4");
    elem.addEventListener("mouseout", iconfour_out);

}

//This func was made for the mouseout event
function iconfour_out() {

    for (var i = 1; i <= 4; i++) {
        var fail_elements = document.getElementById("icon" + String(i) + "_fail");
        fail_elements.hidden = false;
        var normal_elements = document.getElementById("icon" + String(i));
        normal_elements.hidden = true;
    }

    for (var b = 1; b <= 5; b++) {
        var inputs = document.getElementById("input" + String(b));
        inputs.disabled = false;

    }
}

//This func was made for the click event
function iconfour_click() {

    if (document.getElementById("icon4_fail").hidden == true) {
        var elem = document.getElementById("icon4");
        elem.removeEventListener("mouseout", iconfour_out);
        elem.removeEventListener("click", iconfour_click);
        elem.addEventListener("click", icon_four_click_off);
    }


}

//This func was made as the addition for the click event for that when you want to turn off the stars
function icon_four_click_off() {


    for (var i = 1; i <= 5; i++) {
        var fail_elements = document.getElementById("icon" + String(i) + "_fail");
        fail_elements.hidden = false;
        var normal_elements = document.getElementById("icon" + String(i));
        normal_elements.hidden = true;
    }

    for (var b = 1; b <= 5; b++) {
        var inputs = document.getElementById("input" + String(b));
        inputs.disabled = false;

    }

    var elem = document.getElementById("icon5");
    elem.addEventListener("mouseout", iconfour_out);
    elem.addEventListener("click", iconfour_click);
    elem.removeEventListener("click", icon_four_click_off);
}


//This section works for the elements with id 'icon3'

//This func made for the mouseover event
function iconthree_over() {

    for (var i = 1; i <= 3; i++) {
        var fail_elements = document.getElementById("icon" + String(i) + "_fail");
        fail_elements.hidden = true;
        var normal_elements = document.getElementById("icon" + String(i));
        normal_elements.hidden = false;

    }

    for (var b = 1; b <= 5; b++) {
        if (b == 3) {
            continue;
        }
        var inputs = document.getElementById("input" + String(b));
        inputs.disabled = true;

    }

    var elem = document.getElementById("icon3");
    elem.addEventListener("mouseout", iconthree_out);

}

//This func was made for the mouseout event
function iconthree_out() {

    for (var i = 1; i <= 6; i++) {
        var fail_elements = document.getElementById("icon" + String(i) + "_fail");
        fail_elements.hidden = false;
        var normal_elements = document.getElementById("icon" + String(i));
        normal_elements.hidden = true;
    }

    for (var b = 1; b <= 5; b++) {
        var inputs = document.getElementById("input" + String(b));
        inputs.disabled = false;

    }
}

//This func was made for the click event
function iconthree_click() {

    if (document.getElementById("icon3_fail").hidden == true) {
        var elem = document.getElementById("icon3");
        elem.removeEventListener("mouseout", iconthree_out);
        elem.removeEventListener("click", iconthree_click);
        elem.addEventListener("click", icon_three_click_off);
    }


}

//This func was made as the addition for the click event for that when you want to turn off the stars
function icon_three_click_off() {


    for (var i = 1; i <= 5; i++) {
        var fail_elements = document.getElementById("icon" + String(i) + "_fail");
        fail_elements.hidden = false;
        var normal_elements = document.getElementById("icon" + String(i));
        normal_elements.hidden = true;
    }

    for (var b = 1; b <= 5; b++) {
        var inputs = document.getElementById("input" + String(b));
        inputs.disabled = false;

    }

    var elem = document.getElementById("icon3");
    elem.addEventListener("mouseout", iconthree_out);
    elem.addEventListener("click", iconthree_click);
    elem.removeEventListener("click", icon_three_click_off);
}


//This section works for the elements with id 'icon2'

//This func made for the mouseover event
function icontwo_over() {

    for (var i = 1; i <= 2; i++) {
        var fail_elements = document.getElementById("icon" + String(i) + "_fail");
        fail_elements.hidden = true;
        var normal_elements = document.getElementById("icon" + String(i));
        normal_elements.hidden = false;

    }

    for (var b = 1; b <= 5; b++) {
        if (b == 2) {
            continue;
        }
        var inputs = document.getElementById("input" + String(b));
        inputs.disabled = true;

    }

    var elem = document.getElementById("icon2");
    elem.addEventListener("mouseout", icontwo_out);

}

//This func was made for the mouseout event
function icontwo_out() {

    for (var i = 1; i <= 5; i++) {
        var fail_elements = document.getElementById("icon" + String(i) + "_fail");
        fail_elements.hidden = false;
        var normal_elements = document.getElementById("icon" + String(i));
        normal_elements.hidden = true;
    }

    for (var b = 1; b <= 5; b++) {
        var inputs = document.getElementById("input" + String(b));
        inputs.disabled = false;

    }
}

//This func was made for the click event
function icontwo_click() {

    if (document.getElementById("icon2_fail").hidden == true) {
        var elem = document.getElementById("icon2");
        elem.removeEventListener("mouseout", icontwo_out);
        elem.removeEventListener("click", icontwo_click);
        elem.addEventListener("click", icon_two_click_off);
    }


}

//This func was made as the addition for the click event for that when you want to turn off the stars
function icon_two_click_off() {


    for (var i = 1; i <= 5; i++) {
        var fail_elements = document.getElementById("icon" + String(i) + "_fail");
        fail_elements.hidden = false;
        var normal_elements = document.getElementById("icon" + String(i));
        normal_elements.hidden = true;
    }

    for (var b = 1; b <= 5; b++) {
        var inputs = document.getElementById("input" + String(b));
        inputs.disabled = false;

    }

    var elem = document.getElementById("icon2");
    elem.addEventListener("mouseout", icontwo_out);
    elem.addEventListener("click", icontwo_click);
    elem.removeEventListener("click", icon_two_click_off);
}


//This section works for the elements with id 'icon1'

//This func made for the mouseover event
function iconone_over() {

    for (var i = 1; i <= 1; i++) {
        var fail_elements = document.getElementById("icon" + String(i) + "_fail");
        fail_elements.hidden = true;
        var normal_elements = document.getElementById("icon" + String(i));
        normal_elements.hidden = false;

    }

    for (var b = 1; b <= 5; b++) {
        if (b == 1) {
            continue;
        }
        var inputs = document.getElementById("input" + String(b));
        inputs.disabled = true;

    }

    var elem = document.getElementById("icon1");
    elem.addEventListener("mouseout", iconone_out);

}

//This func was made for the mouseout event
function iconone_out() {

    for (var i = 1; i <= 5; i++) {
        var fail_elements = document.getElementById("icon" + String(i) + "_fail");
        fail_elements.hidden = false;
        var normal_elements = document.getElementById("icon" + String(i));
        normal_elements.hidden = true;
    }

    for (var b = 1; b <= 5; b++) {
        var inputs = document.getElementById("input" + String(b));
        inputs.disabled = false;

    }
}

//This func was made for the click event
function iconone_click() {

    if (document.getElementById("icon1_fail").hidden == true) {
        var elem = document.getElementById("icon1");
        elem.removeEventListener("mouseout", iconone_out);
        elem.removeEventListener("click", iconone_click);
        elem.addEventListener("click", icon_one_click_off);
    }


}

//This func was made as the addition for the click event for that when you want to turn off the stars
function icon_one_click_off() {


    for (var i = 1; i <= 5; i++) {
        var fail_elements = document.getElementById("icon" + String(i) + "_fail");
        fail_elements.hidden = false;
        var normal_elements = document.getElementById("icon" + String(i));
        normal_elements.hidden = true;
    }

    for (var b = 1; b <= 5; b++) {
        var inputs = document.getElementById("input" + String(b));
        inputs.disabled = false;

    }

    var elem = document.getElementById("icon1");
    elem.addEventListener("mouseout", iconone_out);
    elem.addEventListener("click", iconone_click);
    elem.removeEventListener("click", icon_one_click_off);
}