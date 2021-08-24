import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';

const appDiv = document.getElementById('app');

ReactDOM.render(
		<App></App>,
	appDiv
);

if (module.hot) {
	module.hot.accept();
}
