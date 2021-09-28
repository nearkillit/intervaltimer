import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import { createStore } from 'redux'
import { Provider } from 'react-redux'
import reducer from './modules/reducer'
import { BrowserRouter as Router } from 'react-router-dom' 

const store = createStore(reducer,
  window.__REDUX_DEVTOOLS_EXTENSION__ && window.__REDUX_DEVTOOLS_EXTENSION__() )

ReactDOM.render(
  <Provider store={store}>
    <Router>
      <App />
    </Router>    
  </Provider>,
  document.getElementById('root')
);

