
/* Get theme information from cookie */
cookie_theme = document.cookie.split(";")[0];

if( cookie_theme == "dark" || cookie_theme == "light") {
    theme(cookie_theme);
}

/* Information about cookies */
else {
    document.getElementById("cookie_info").innerHTML= "<div class='alert alert-warning alert-dismissible fade show' role='alert'>" +
                                                            "<strong>This website uses cookies!</strong>" +
                                                            "Check out the Readme for more information: " +
                                                            "<a href='/readme'> Learn more!</a>" +
                                                            "<button type='button' class='close' data-dismiss='alert' aria-label='Close'>" +
                                                                "<span aria-hidden='true'>&times;</span>" +
                                                            "</button>" +
                                                      "</div>";
    theme("light");
}

/* Set theme */
function theme(theme) {
    document.cookie = theme + "; path=/";

    if(theme == "dark") {
        document.body.setAttribute("class", "bg-dark text-light");
        document.getElementById('navbar').setAttribute("class", "navbar navbar-expand-lg navbar-dark bg-secondary");
    }

    else if(theme == "light") {
        document.body.setAttribute("class", "bg-white text-dark");
        document.getElementById('navbar').setAttribute("class", "navbar navbar-expand-lg navbar-light bg-success");
            }

    try {
        document.getElementById("top_logo").setAttribute("src", "/static/images/" + theme + "logo.png");
        document.getElementById("logo").setAttribute("src", "/static/images/" + theme + "logo.png");
    }
    catch (TypeError) { console.log("no main-html") }


    try {
        document.getElementById("navdocumentation").setAttribute("class", "navbar navbar-" + theme + "bg-" + theme + "flex-column");
    }
    catch (TypeError) { console.log("no documentation-html") }


    try {
         document.getElementsByClassName("table1").setAttribute("class", "table table-" + theme);
    }
    catch (TypeError) { console.log("no table-html") }

    try {
         document.getElementById("tbl").setAttribute("class", "table table-" + theme);
    }
    catch (TypeError) { console.log("no table-html") }

    try {
        var i = 1;
        while(i != 5) {
            card = "card" + i.toString();
            document.getElementById(card).setAttribute("class", "card bg-" + theme);
            i++;

        }
    }
    catch (TypeError) { console.log("no readme-html") }
}