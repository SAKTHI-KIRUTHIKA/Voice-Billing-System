import React, { useEffect, useState } from 'react';

function Admin() {
  const [bills, setBills] = useState([]);
  const [searchTerm, setSearchTerm] = useState("");
  const [editData, setEditData] = useState(null);

  useEffect(() => {
    fetchBills();
  }, []);

  const fetchBills = () => {
    fetch("http://localhost:5002/api/bills")
      .then((response) => response.json())
      .then((data) => setBills(data))
      .catch((error) => console.error("Error fetching bills:", error));
  };

  const deleteRow = (itemName) => {
    fetch("http://localhost:5002/delete-bill", {
      method: "DELETE",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ItemName: itemName }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data.message);
        setBills(bills.filter((bill) => bill.ItemName !== itemName));
      })
      .catch((error) => console.error("Error deleting bill:", error));
  };

  const editRow = (itemName) => {
    const newPrice = prompt("Enter new price:");
    const newQuantity = prompt("Enter new quantity:");
    if (!newPrice || !newQuantity) return;

    fetch("http://localhost:5002/edit-bill", {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ItemName: itemName, Price: newPrice, Quantity: newQuantity }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data.message);
        setBills(
          bills.map((bill) =>
            bill.ItemName === itemName ? { ...bill, Price: newPrice, Quantity: newQuantity } : bill
          )
        );
      })
      .catch((error) => console.error("Error updating bill:", error));
  };

  const handleSearch = (event) => {
    setSearchTerm(event.target.value);
  };

  const filteredBills = bills.filter((bill) =>
    bill.ItemName.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div>
      <h2>Bill Details</h2>
      <input
        type="text"
        placeholder="Search Item..."
        value={searchTerm}
        onChange={handleSearch}
      />
      <table border="1">
        <thead>
          <tr>
            <th>Item Name</th>
            <th>Price</th>
            <th>Quantity</th>
            <th>Units</th>
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {filteredBills.map((bill) => (
            <tr key={bill._id}>
              <td>{bill.ItemName}</td>
              <td>{bill.Price}</td>
              <td>{bill.Quantity}</td>
              <td>{bill.Units}</td>
              <td>
                <button className='trashBtn' onClick={() => deleteRow(bill.ItemName)}><i className="fa-solid fa-trash"></i></button>
                <button className='editBtn' onClick={() => editRow(bill.ItemName)}><i className="fa-solid fa-pen-to-square"></i></button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Admin;
