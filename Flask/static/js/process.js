const processTable = document.querySelector(".processes table");

fetch('http://127.0.0.1:5000/static/json/process.json')
  .then(response => response.json())
  .then(jsonContent => {
    jsonContent.forEach(element => {
        let newProcess = document.createElement('tr');
        newProcess.className = 'process';
        let processName = document.createElement('td');
        processName.textContent = `${element["index"]}`;
        let processSid = document.createElement('td');
        processSid.textContent = `${element["name"]}`;
        let processIndex = document.createElement('td');
        processIndex.textContent = `${element["sid"]}`
        let processStatus = document.createElement('td');
        if (element["sid"] === 0) {
            processStatus.textContent = "SAFE";
            processStatus.className = "safe"
        } else if (element["sid"] === 1) {
            processStatus.textContent = "SUSPECT";
            processStatus.className = "suspect"
        } else if (element["sid"] === 2) {
            processStatus.textContent = "THREAT";
            processStatus.className = "threat"
        } else {
            processStatus.textContent = "NOT MAPPED";
        }
        newProcess.appendChild(processName);
        newProcess.appendChild(processSid);
        newProcess.appendChild(processIndex);
        newProcess.appendChild(processStatus);
        processTable.appendChild(newProcess);
    });
  })