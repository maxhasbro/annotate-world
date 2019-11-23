import './index.css';
import React from 'react';
import { Provider } from 'react-redux'
import { render } from 'react-dom';
import { BrowserRouter as Router, Route } from 'react-router-dom'
import { createStore } from 'redux'
import { annotateWorldApp } from './reducers/reducers'
import App from './App';

const store = createStore(annotateWorldApp);

const Root = () => (
  <Provider store={store}>
      <Router>
        <Route path="/:route?" component={App} />
      </Router>
  </Provider>
);

render(<Root />, document.getElementById("root"));