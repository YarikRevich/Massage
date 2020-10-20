function hidden_off() {
    document.getElementById("hidder").hidden = false;
    document.getElementById("user-static").style.setProperty("display", "flex")
}

function hidden_on() {
    document.getElementById("hidder").hidden = true;
    document.getElementById("user-static").style.setProperty("display", "none")
}