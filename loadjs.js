function getData() {
  fetch("http://127.0.0.1:5000/getData")
    .then((response) => response.json())
    .then((data) => {
      let tableBody = document.querySelector("#dataTable tbody");
      tableBody.innerHTML = ""; // Xóa dữ liệu cũ

      data.forEach((row, index) => {
        let tr = document.createElement("tr");
        tr.innerHTML = `<td>${index + 1}</td><td>${row.ACC}</td><td>${
          row.PASS
        }</td>`;
        tableBody.appendChild(tr);
      });
      output += "</ol>";
      document.getElementById("result").innerHTML = output;
    });
}
function addData() {
  const ACC = document.getElementById("ACC").value;
  const PASS = document.getElementById("PASS").value;
  fetch("http://127.0.0.1:5000/addData", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ ACC: ACC, PASS: PASS }),
  })
    .then((response) => response.json())
    .then((data) => {
      alert("Congratulation");
      getData();
    });
}
