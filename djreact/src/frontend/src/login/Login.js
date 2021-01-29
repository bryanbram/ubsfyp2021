import React, { useState } from 'react';
import { Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import { login, reset_password } from '../actions/authenticate';
import './css/login.css'
import loginLogo from './picture/eye.jpg';
import forgetPwdLogo from './picture/microchip.jpg';

const Login = ({ login, error, message, isAuthenticated, reset_password  }) => {
    //login state
    const [loginFormData, setloginFormData] = useState({
        email: '',
        password: '' 
    });
    // const [loginError, setLoginError] = useState(error === "login_fail"?"Invalid email or password.":"");

    // forget your password states
    // const [forgetPwdError, setForgetPwdError] = useState(error ==="password_reset_fail"?"This email does not exist.":"");
    // const [forgetPwdMsg, setForgetPwdMsg]= useState(message ==="password_reset_success"?"Password reset link has been sent to your email.":"");
    const [forgetPwdFormData, setForgetPwdFormData] = useState({
        forgetPwdEmail: ''
    });


    // login page functions
    const { email, password } = loginFormData;

    const onLoginChange = e => setloginFormData({ ...loginFormData, [e.target.name]: e.target.value });

    const onLoginSubmit = e => {
        e.preventDefault();
        login(email, password);
    };

 
    if (isAuthenticated) {
        return <Redirect to='/' />
    }


    // forget your password page function
    // const { forgetPwdEmail } = forgetPwdFormData;

    // const onForgetPwdChange = e => setForgetPwdFormData({ ...forgetPwdFormData, [e.target.name]: e.target.value });

    // const onForgetPwdSubmit = e => {
    //     e.preventDefault();
    //     reset_password(forgetPwdEmail);
    // };


    // toggle forms
    // const toggleForm = e => {
    //     const container = document.querySelector('.container');
    //     container.classList.toggle('active');
    // };

    return (
        <div>
            <nav>
                <label className="logo"><span>!</span>H05T4G3S</label>
            </nav>
            <section>
            <div className="container">
                <div className="user signinBx">
                <div className="imgBx"><img src={loginLogo} alt="" /></div>
                <div className="formBx">
                    <form action="" onSubmit={e => onLoginSubmit(e)}>
                    <p style={{color: '#A52A2A'}}>{error}</p>
                    <h2>Sign In</h2>
                    <input type="email" name="email" placeholder="Email" value={email} onChange={e => onLoginChange(e)} required/>
                    <input type="password" name="password" placeholder="Password" value={password} onChange={e => onLoginChange(e)}required/>
                    <input type="submit" id="enterbutton1" value="Login" />
                    <p className="signup">
                        Don't have an account ?
                        <a href="/signup">Register.</a>
                    </p>
                    <p className="signup">
                        Forgot your password ?
                        <a href='/ResetPassword' >Reset Password.</a>
                    </p>
                    </form>
                </div>
                </div>
            </div>
            </section>

        </div>
    );
};

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated,
    error: state.auth.error,
    message: state.auth.message
});

export default connect(mapStateToProps, { login ,reset_password })(Login);
