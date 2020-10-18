/** @module App
 *  @since 2020.10.18, 21:16
 *  @changed 2020.10.18, 22:17
 */

import React from 'react';
import logo from './logo.svg';
import './App.pcss';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
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

export default App;
