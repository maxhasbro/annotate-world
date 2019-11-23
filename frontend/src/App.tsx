import React from 'react';
import './App.css';
import Home from './components/Home'
import { RouteComponentProps } from 'react-router-dom';


type Params = { route: string }

const App = ({match}: RouteComponentProps<Params> ) => (
    <div>
      <Home/>
      <h3>{match.params.route}</h3>
    </div>
)

export default App;
