import React from 'react';
import './App.css';
import Home from './components/Home'
import { Link } from 'react-router-dom';

const App = () => (
    <div>
      <Home/>
      <Link to='/modify/asdf'>asdf</Link>
      <br/>
      <Link to='/modify/qwerty'>qwerty</Link>
      <br/>
      <br/>
      <Link to='/about'>About us</Link>
    </div>
)

export default App;
