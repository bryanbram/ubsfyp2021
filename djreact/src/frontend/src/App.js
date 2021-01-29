import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

import Home from './Login/Home';
import Login from './Login/Login';
import Signup from './Login/Signup';
import Activate from './Login/Activate';
import ResetPassword from './Login/ResetPassword';
import ResetPasswordConfirm from './Login/ResetPasswordConfirm';


import { Provider } from 'react-redux';
import store from './store';

import Layout from './hocs/Layout';


const App = () => (
    <Provider store={store}>
        <Router>
            <Layout>
                <Switch>
                    <Route exact path='/' component={Home} />
                    <Route exact path='/login' component={Login} />
                    <Route exact path='/signup' component={Signup} />
                    <Route exact path='/activate/:uid/:token' component={Activate} />
                    <Route exact path='/ResetPassword' component={ResetPassword} />
                    <Route exact path='/password/reset/confirm/:uid/:token' component={ResetPasswordConfirm} />
                    
                </Switch>
            </Layout>
        </Router>
    </Provider>
);

export default App;