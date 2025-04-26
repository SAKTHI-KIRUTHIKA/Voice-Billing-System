

// import React, { useState } from "react";
// import "./App.css";

// function App() {
//   const [response, setResponse] = useState(null);
//   const [loading, setLoading] = useState(false);
//   const [receiverName, setReceiverName] = useState("");
//   const [itemName, setItemName] = useState("");
//   const [quantity, setQuantity] = useState("");
//   const [units, setUnits] = useState("");

//   const handleVoiceInput = async () => {
//     setLoading(true);
//     try {
//       const res = await fetch("http://127.0.0.1:5000/voice");
//       const data = await res.json();
//       setResponse(data);
//       setItemName(response["Item name"] || "");
//       setQuantity(response["Quantity"] || "");
//       console.log(response)
//       setUnits(response["Units"])
//     } catch (error) {
//       console.error("Error fetching data:", error);
//     }
//     setLoading(false);
//   };

//   return (
//     <div className="container">
//       <section className="section">
//         <h2>Billing Information</h2>
//         <div className="form-group">
//           <label htmlFor="receiverName">Enter Receiver Name</label>
//           <input
//             type="text"
//             id="receiverName"
//             name="receiverName"
//             value={receiverName}
//             onChange={(e) => setReceiverName(e.target.value)}
//           />
//           <button
//             className="create-button voice-button"
//             onClick={handleVoiceInput}
//             disabled={loading}
//           >
//             {loading ? "Listening..." : "Voice"}
//           </button>
//         </div>
//       </section>

//       <section className="section">
//         <h2>Item Details</h2>
//         <table>
//           <thead>
//             <tr>
//               <th>S/N.</th>
//               <th>Item Name</th>
//               <th>Quantity</th>
//               <th>Units</th>
//             </tr>
//           </thead>
//           <tbody>
//             <tr>
//               <td>1</td>
//               <td>
//                 <input
//                   type="text"
//                   name="itemName"
//                   value={itemName}
//                   onChange={(e) => setItemName(e.target.value)}
//                 />
//               </td>
//               <td>
//                 <input
//                   type="number"
//                   name="quantity"
//                   value={quantity}
//                   min="1"
//                   onChange={(e) => setQuantity(e.target.value)}
//                 />
//               </td>
//             <td><input
//                   type="text"
//                   name="units"
//                   value={units}
//                   onChange={(e) => setQuantity(e.target.value)}
//                 /></td>
//             </tr>
//           </tbody>
//         </table>
//       </section>

//       <section className="section">
//         <h2>Invoice Details</h2>
//         <div className="form-group">
//           <label htmlFor="invoiceDate">Select Invoice Date</label>
//           <input type="date" id="invoiceDate" name="invoiceDate" />
//         </div>
//         <div className="total-section">
//           <label htmlFor="totalAmount">Total</label>
//           <input type="number" id="totalAmount" name="totalAmount" />
//         </div>
//       </section>

//       <button className="create-button">Generate PDF</button>
//     </div>
//   );
// }

// export default App;
import React, { useState } from "react";
import jsPDF from "jspdf";
import "jspdf-autotable";
import autoTable from "jspdf-autotable"; // Import separately
import "../App.css";

function Billing() {
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [receiverName, setReceiverName] = useState("");
  const [items, setItems] = useState([]);

  const handleVoiceInput = async () => {
    setLoading(true);
    try {
      const res = await fetch("http://127.0.0.1:5000/voice");
      const data = await res.json();
      setResponse(data);
      setItems([...items, {
        itemName: data["Item Name"] || "",
        quantity: data["Available Quantity"] || "",
        units: data["Units"] || "",
        price: data["Total Cost"] || ""
      }]);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
    setLoading(false);
  };

  const handleAddRow = () => {
    setItems([...items, { itemName: "", quantity: "", units: "", price: "" }]);
  };

  const handleChange = (index, field, value) => {
    const newItems = [...items];
    newItems[index][field] = value;
    setItems(newItems);
  };

  // Calculate total amount dynamically
  const totalAmount = items.reduce((total, item) => total + (parseFloat(item.price) || 0), 0);

  const generatePDF = () => {
    const doc = new jsPDF();
    doc.text("Invoice", 20, 10);
    doc.text(`Receiver Name: ${receiverName}`, 20, 20);
  
    const tableData = items.map((item, index) => [
      index + 1,
      item.itemName,
      item.quantity,
      item.price,
      item.units,
    ]);
  
    // Call autoTable properly
    autoTable(doc, {
      head: [["S/N", "Item Name", "Quantity", "Price", "Units"]],
      body: tableData,
      startY: 30,
    });
  
    doc.text(`Total Amount: ${totalAmount}`, 20, doc.lastAutoTable.finalY + 10);
    doc.save("invoice.pdf");
  };

  return (
    <div className="container">
      <section className="section">
        <h2>Billing Information</h2>
        <div className="form-group">
          <label htmlFor="receiverName">Enter Receiver Name</label>
          <input
            type="text"
            id="receiverName"
            name="receiverName"
            value={receiverName}
            onChange={(e) => setReceiverName(e.target.value)}
          />
          <button
            className="create-button voice-button"
            onClick={handleVoiceInput}
            disabled={loading}
          >
            {loading ? "Listening..." : "Voice"}
          </button>
        </div>
      </section>

      <section className="section">
        <h2>Item Details</h2>
        <table>
          <thead>
            <tr>
              <th>S/N.</th>
              <th>Item Name</th>
              <th>Quantity</th>
              <th>Price</th>
              <th>Units</th>
            </tr>
          </thead>
          <tbody>
            {items.map((item, index) => (
              <tr key={index}>
                <td>{index + 1}</td>
                <td>
                  <input
                    type="text"
                    name="itemName"
                    value={item.itemName}
                    onChange={(e) => handleChange(index, "itemName", e.target.value)}
                  />
                </td>
                <td>
                  <input
                    type="number"
                    name="quantity"
                    value={item.quantity}
                    min="1"
                    onChange={(e) => handleChange(index, "quantity", e.target.value)}
                  />
                </td>
                <td>
                  <input
                    type="text"
                    name="price"
                    value={item.price}
                    onChange={(e) => handleChange(index, "price", e.target.value)}
                  />
                </td>
                <td>
                  <input
                    type="text"
                    name="units"
                    value={item.units}
                    onChange={(e) => handleChange(index, "units", e.target.value)}
                  />
                </td>
              </tr>
            ))}
          </tbody>
        </table>
        <button onClick={handleAddRow} className="create-button">Add Item</button>
      </section>

      <section className="section">
        <h2>Invoice Details</h2>
        <div className="form-group">
          <label htmlFor="invoiceDate">Select Invoice Date</label>
          <input type="date" id="invoiceDate" name="invoiceDate" />
        </div>
        <div className="total-section">
          <label htmlFor="totalAmount">Total</label>
          <input type="number" id="totalAmount" name="totalAmount" value={totalAmount} readOnly />
        </div>
      </section>

      <button className="create-button" onClick={generatePDF}>Generate PDF</button>
    </div>
  );
}

export default Billing;
