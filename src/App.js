

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

import React from "react";
import "./App.css";
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import Billing from "./components/Billing";
import Admin from "./components/Admin";
import Signup from "./components/Signup";
import Login from "./components/Login";
function App() {
return(
  <Router>

    <Routes>
      <Route path='/' element={<Signup/>}></Route>
      <Route path='/admin' element={<Admin/>}></Route>
      <Route path='/dashboard' element={<Billing/>}></Route>
      <Route path='/login' element={<Login/>}></Route>

    </Routes>
    </Router>
  
);
  
}

export default App;
