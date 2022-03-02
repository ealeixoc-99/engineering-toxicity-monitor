import React from "react";
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
        <form data-testid="form-test" onSubmit={submitSentence}>
          <label>Write a sentence :<textarea data-testid="text-area-test" type='text' value={sentence} onChange={onChange} /></label>
          <input type="submit" value="Send" />
        </form>
        <h1 className="App-title">{loading === true ? (<p>Loading</p>) : response === null ? <p></p> : ( 
          <table>
            <thead>
              <tr><th>Statistics</th></tr>
            </thead>
            <tbody>
              <tr>
                <td>Identity Attack</td>
                <td>{response?.identity_attack[0]}</td>
              </tr>
              <tr>
                <td>Insult</td>
                <td>{response?.insult[0]}</td>
              </tr>
              <tr>
                <td>Obscene</td>
                <td>{response?.obscene[0]}</td>
              </tr>
              <tr>
                <td>Severe Toxicity</td>
                <td>{response?.severe_toxicity[0]}</td>
              </tr>
              <tr>
                <td>Threat</td>
                <td>{response?.threat[0]}</td>
              </tr>
              <tr>
                <td>Toxicity</td>
                <td data-testid="test-toxicity">{response?.toxicity[0]}</td>
              </tr>
            </tbody>
          </table>)}
          </h1>
      </header>
    </div>
  );
}

export default App;
