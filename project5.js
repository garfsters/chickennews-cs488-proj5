function list_files(url, func) {
    let xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        if (xhttp.status != 200) {
            console.log("Error");
        } else {
            func(xhttp.response);
        }
    }
    xhttp.open("GET", url);
    xhttp.send();
}

function upload_file(url, func, formData) {
    let xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        if (xhttp.status != 200) {
            console.log("Error");
        } else {
            func(xhttp.response);
        }
    }
    xhttp.open("POST", url, true);
    xhttp.send(formData);
}

function login() {
    window.location.replace("/project5/login");
}

function logout() {
    window.location.replace("/project5/logout");
}

function homepage() {
    window.location.replace("/project5");
}

function uploadfile() {
    var formData = new FormData();
    formData.append("title", document.getElementById("title").value);
    formData.append("description", document.getElementById("description").value);

    upload_file("/project5/uploadfile", uploadfile_response,formData);
}

function uploadfile_response(response) {
    location.reload();
}

function log_acc() {
    var formData = new FormData();
    formData.append("email", document.getElementById("txtEmail").value);
    formData.append("password", document.getElementById("txtPassword").value);

    upload_file("/acc_login", login_response, formData);
}

function login_response() {
    location.reload();
}

function deleteBlog(id) {
    var formData = new FormData();
    formData.append("ID", id);

    upload_file("/project5/deletefile", deletefile_response, formData);
}

function deletefile_response(response) {
    location.reload();
}

function listblogs() {
    list_files("/project5/listfiles", listblogs_response);
}

function list_myblogs() {
    list_files("/project5/listfiles", listmyblogs_response);
}

function listblogs_response(response) {
    var data = JSON.parse(response);
    var items = data["items"];

    var temp = "<div>";

    for (var i = 0; i < items.length; i++) {
        var title = items[i]["title"];
        var description = items[i]["description"];
        var time = items[i]["time"];
        var email = items[i]["email"];
        var username = email.split('@')[0];

        temp += `<div class="blog">`;
        temp += `<h2>${title}</h2>`;
        temp += `<h3>${description}</h3>`;
        temp += `<h3>${time}</h3>`;
        temp += `<h4>Posted by: ${username}</h4>`;
        temp += "</div>";
    }

    temp += "</div>"

    document.getElementById("divResults").innerHTML = temp;
}

function listmyblogs_response(response) {
    var data = JSON.parse(response);
    var items = data["items"];

    var temp = "<div>";

    for (var i = 0; i < items.length; i++) {
        var id = items[i]["ID"];

        var title = items[i]["title"];
        var description = items[i]["description"];
        var time = items[i]["time"];
        var email = items[i]["email"];
        var username = email.split('@')[0];

        temp += `<div class="blog">`;
        temp += `<h2>${title}</h2>`;
        temp += `<h3>${description}</h3>`;
        temp += `<h3>${time}</h3>`;
        temp += `<button onclick="deleteBlog('${id}');">Delete</button>`;
        temp += `<h4>Posted by: ${username}</h4>`;
        temp += "</div>";

    }

    temp += "</div>"

    document.getElementById("divResults").innerHTML = temp;
}







console.log("Script Loaded");