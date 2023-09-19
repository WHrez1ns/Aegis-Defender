const checkbtn = document.querySelector(".dashboard-header-button");
const dashboard_header_title = document.querySelector(".dashboard-header-left-title");
const dashboard_checks = document.querySelector(".dashboard-checks");
let detection_in_real_time = false;

// button logic
checkbtn.addEventListener("click", () => {
    checkbtn.classList.toggle("selected");
    if ( checkbtn.classList.contains("selected") ) { 
        detection_in_real_time = true;
        dashboard_header_title.innerHTML = "We are protecting you <i class='bx bx-shield-quarter'></i>";
        dashboard_checks.children.item(0).innerHTML = "<div class='dashboard-check-button checked'></div> Real-time detection mode activated";
    } else {
        detection_in_real_time = false;
        dashboard_header_title.innerHTML = "Activate run mode <i class='bx bxs-error'></i>";
        dashboard_checks.children.item(0).innerHTML = "<div class='dashboard-check-button unchecked'></div> Real-time detection mode disabled";
    }
})

function processes_analyzed() {
    fetch('http://127.0.0.1:5000/static/json/process.json')
        .then(response => response.json())
        .then(jsonContent => {
            let processesAnalyzed = jsonContent["length"];
            dashboard_checks.children.item(3).innerHTML = `<div class='dashboard-check-button checked'></div> Processes analyzed: ${processesAnalyzed}`;
        })
}

processes_analyzed()