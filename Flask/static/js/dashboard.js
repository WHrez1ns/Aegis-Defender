const checkbtn = document.querySelector(".dashboard-header-button");
const dashboard_header_title = document.querySelector(".dashboard-header-left-title");
const dashboard_checks = document.querySelector(".dashboard-checks");
let detection_in_real_time = false;

// button logic
checkbtn.addEventListener("click", () => {
    checkbtn.classList.toggle("selected");
    if ( checkbtn.classList.contains("selected") ) { 
        detection_in_real_time = true;
        dashboard_header_title.innerHTML = "Estamos protegendo você <i class='bx bx-shield-quarter'></i>";
        dashboard_checks.children.item(0).innerHTML = "<div class='dashboard-check-button checked'></div> Modo de detecção em tempo real ativado";
    } else {
        detection_in_real_time = false;
        dashboard_header_title.innerHTML = "Ative o modo de execução <i class='bx bxs-error'></i>";
        dashboard_checks.children.item(0).innerHTML = "<div class='dashboard-check-button unchecked'></div> Modo de detecção em tempo real desativado";
    }
})