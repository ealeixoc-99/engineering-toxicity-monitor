import React from "react";
import logo from './florian.jpg';
import './App.css';

function App() {
  const [response, setResponse] = React.useState(null);
  const [loading, setLoading] = React.useState(false);
  const [sentence, setSentence] = React.useState('');

  function submitSentence(evt){
    setLoading(true);
    evt.preventDefault();
    fetch('http://localhost:5000/index?sentence='+sentence , {
      method: "GET",
      headers: {
        'Content-type': 'application/json'
      },
    })
    .then((res) => res.json())
    .then((resJson) => {setResponse(resJson.message)
      setLoading(false)})
  }

  function onChange(evt){
    setSentence(evt.target.value);
  }

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <br />
        <br />
        <form onSubmit={submitSentence}>
          <label>Write a sentence :<textarea value={sentence} onChange={onChange} /></label>
          <input type="submit" value="Send" />
        </form>
        <h1 className="App-title">{loading === true ? (<p>Loading</p>) : (response)}</h1>
      </header>
    </div>
  );
}

export default App;
