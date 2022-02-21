import React from "react";
import logo from './logo.svg';
import './App.css';

function App() {
  const [response, setResponse] = React.useState(null);
  const [loading, setLoading] = React.useState(false);

  React.useEffect(
    () => {
      setLoading(true)
      fetch('/index')
        .then((res) => res.json())
        .then((resJson) => {setResponse(resJson.message)
        setLoading(false)});
    }, []
  );

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1 className="App-title">{loading === true ? (<p>Loading</p>) : (response)}</h1>
      </header>
    </div>
  );
}

export default App;
