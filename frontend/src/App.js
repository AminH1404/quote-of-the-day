import React, { useState } from 'react';

function App() {
  const [quote, setQuote] = useState("");

  const fetchQuote = async () => {
    const response = await fetch("https://your-backend-service.onrender.com/api/quote");
    const data = await response.json();
    setQuote(data.quote);
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h1>Quote of the Day</h1>
      <button onClick={fetchQuote}>Get Quote</button>
      <p style={{ marginTop: "20px", fontSize: "24px" }}>{quote}</p>
    </div>
  );
}

export default App;
