import './App.css';
import { useState } from 'react';
import axios from 'axios';
import { ListTopics } from './ListTopics.js';




function App() {
  
  const [Userinput, setUserinput] = useState("");
  const[DataRecieved, setDataRecieved] = useState(false);
  const[Azure_data, setAzure_Data]=useState({Phrases:[]});

  
  function handleSubmit(e) {
    const userData = {username: Userinput};
    const testval=e.target.value;
    e.preventDefault();
    //setUserinput(e.target.value);
    console.log(Userinput);
    axios.post("/Twitterapi", userData)
    .then(response => { // Response from backend
                console.log("@@@@@@@@@")
                console.log(response.data.phrases)
                setAzure_Data({Phrases: response.data.phrases});
                setDataRecieved(true);
    })
    .catch(err => console.log(err));
            
  }

  
  
  if (!DataRecieved)
  {
      
      return (
        <body>
          
          <div className="App">
            <form onSubmit={handleSubmit}>

            <label>Please input username:</label>
            <div className="field">
              <input placeholder="@ExampleHandle" value={Userinput} onInput={e => setUserinput(e.target.value)}/>
              <button type="submit">Submit</button>
            </div>
          </form>
          </div>
          
        </body>  
      );
  }
  
  if (DataRecieved)
  {
      
      return (
        <body>
          
          <div className="App">
            <form onSubmit={handleSubmit}>

            <label>Please input username:</label>
            <div className="field">
              <input placeholder="@ExampleHandle" value={Userinput} onInput={e => setUserinput(e.target.value)}/>
              <button type="submit">Submit</button>
            </div>
          </form>
          

          </div>
          <div className="phrases">
            <h3>main Topics of tweets</h3>
            {Azure_data.Phrases.map(Topic => <ListTopics Phrase={Topic} />)}
          </div>
          
        </body>  
      );
  }
  
  
  
  
}

export default App;
