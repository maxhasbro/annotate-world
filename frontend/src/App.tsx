import React, { Component } from 'react';
import { Provider } from 'react-redux';
import './App.css';
import { createStore, combineReducers, compose, applyMiddleware } from 'redux';
import { routerForBrowser } from 'redux-little-router';

import routes from './routes';

const { reducer, enhancer, middleware } = routerForBrowser({ routes });
const initialState = {};

const store = createStore(
  combineReducers({router: reducer}),
  initialState,
  compose(enhancer, applyMiddleware(middleware))
);

class App extends Component {
  render() {
    return (
      <Provider store={store}>
      </Provider>
    );
  }
}

export default App;
