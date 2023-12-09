// Function to fetch all data from the backend
async function fetchData() {
  try {
      const response = await fetch('http://localhost:5000/api/data'); // Update the URL accordingly
      const data = await response.json();
      return data;
  } catch (error) {
      console.error('Error fetching data:', error);
      return [];
  }
}

// Function to render data table
async function renderTable() {
  const tableBody = document.getElementById('table-body');
  tableBody.innerHTML = '';

  const books = await fetchData();

  books.forEach(book => {
      const row = tableBody.insertRow();
      row.insertCell(0).innerText = book.harga;
      row.insertCell(1).innerText = book.penulis;
      row.insertCell(2).innerText = book.ISBN;
      row.insertCell(3).innerText = book.tahun;
      row.insertCell(4).innerText = book.judul;
  });
}

// Initial rendering
renderTable();
