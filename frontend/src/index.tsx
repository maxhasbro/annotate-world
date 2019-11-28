import './index.css';
import React from 'react';
import { Provider } from 'react-redux'
import { render } from 'react-dom';
import { BrowserRouter as Router, Route } from 'react-router-dom'
import { createStore } from 'redux'
import { annotateWorldApp } from './reducers/reducers'
import App from './App';
import About from './components/About'
import Modify from './components/Modify'

const store = createStore(annotateWorldApp);

const Root = () => (
  <Provider store={store}>
      <Router>
        <Route exact path="/" component={App} />
        <Route path="/modify/:route?" component={Modify} />
        <Route path="/about" component={About} />
      </Router>
  </Provider>
);

render(<Root />, document.getElementById("root"));