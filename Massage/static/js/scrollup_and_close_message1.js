var t;

function up() {
    var top = Math.max(document.body.scrollTop, document.documentElement.scrollTop);
    if (top > 0) {
        window.scrollBy(0, -100);
        t = setTimeout('up()', 20);
    } else clearTimeout(t);
    return false;
}


function close_window() {

    document.getElementById("window").hidden = true;
    document.getElementById("hidder").hidden = true;

}

function make_form_active() {
    document.getElementById("add_record_form").removeAttribute("hidden");
}

function make_form_inactive() {
    document.getElementById("add_record_form").setAttribute("hidden", true);
}