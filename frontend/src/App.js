import React from 'react';
import logo from './logo.svg';
import './App.css';

class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
        day: ""
    };
  }

  componentDidMount() {
      fetch('/api/day')
          .then(response => response.json())
          .then(response => this.setState({'day': response.day}))
  }

  render() {
    return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <h1>Hello There!!!</h1>
        <p>윅슨 리액트 테스트3!!!!!!!!!</p>
        <h3>Hey!  It's {this.state.day}</h3>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>        
      </header>
    </div>
    );
  }
}



// function App() {
//   return (
    // <div className="App">
    //   <header className="App-header">
    //     <img src={logo} className="App-logo" alt="logo" />
    //     <p>
    //       Edit <code>src/App.js</code> and save to reload.
    //     </p>
    //     <h1>Hello There!!!</h1>
    //     <p>윅슨 리액트 테스트</p>
    //     <a
    //       className="App-link"
    //       href="https://reactjs.org"
    //       target="_blank"
    //       rel="noopener noreferrer"
    //     >
    //       Learn React
    //     </a>        
    //   </header>
    // </div>
//   );  
// }


// export default App;

export default App;
