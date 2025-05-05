const search = document.getElementById("searchInput");
const purpose = document.getElementById("filterPurpose");
const date = document.getElementById("filterDate");
const rows = Array.from(
  document.getElementById("transactionTable").getElementsByTagName("tr")
);
const noResults = document.getElementById("noResults");

function filterTable() {
  const searchValue = search.value.toLowerCase();
  const purposeValue = purpose.value.toLowerCase();
  const dateValue = date.value.toLowerCase();
  let visibleCount = 0;

  rows.slice(1).forEach((row) => {
    const cells = Array.from(row.getElementsByTagName("td"));
    const [transactionID, name, rowDate, , rowPurpose] = cells.map((cell) =>
      cell.textContent.toLowerCase()
    );

    const matches =
      (transactionID.includes(searchValue) || name.includes(searchValue)) &&
      (!purposeValue || rowPurpose === purposeValue) &&
      (!dateValue || rowDate === dateValue);

    row.style.display = matches ? "" : "none";
    visibleCount += matches ? 1 : 0;
  });

  noResults.style.display = visibleCount ? "none" : "";
}

[search, purpose, date].forEach((input) =>
  input.addEventListener("input", filterTable)
);
