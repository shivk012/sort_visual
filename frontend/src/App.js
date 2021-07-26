import { useEffect, useState } from "react";

async function hello() {
  let response = await fetch("http://localhost:5000/");
  console.log(response.json());
  return response.json();
}

function App() {
  const [a, b] = useState(0);
  useEffect(b(hello()),[]);
  return (
    <div className="App">
      <header className="App-header">{a}</header>
    </div>
  );
}

export default App;
