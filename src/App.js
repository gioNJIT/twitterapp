import './App.css';
import { useState } from 'react';
import axios from 'axios';



function App() {
  const [Userinput, setUserinput] = useState("test");

  function handleSubmit(e) {
    const userData = {username: Userinput};
    const testval=e.target.value;
    e.preventDefault();
    //setUserinput(e.target.value);
    console.log(Userinput);
    axios.post("/Twitterapi", userData);
  }

  
  
  
  return (
    <div className="App">
      <form onSubmit={handleSubmit}>
      <label>Please input username:</label>
      <input value={Userinput} onInput={e => setUserinput(e.target.value)}/>
      <button type="submit">Submit</button>
    </form>
    </div>
  );
}

export default App;
