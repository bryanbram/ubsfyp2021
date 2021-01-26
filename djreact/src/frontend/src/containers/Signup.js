import React, { useState } from 'react';
import { Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import { signup } from '../actions/authenticate';
import registerLogo from './picture/microchip.jpg';
import axios from 'axios';
import './css/login.css'

const Signup = ({ signup, message,isAuthenticated }) => {
    const [accountCreationError, setAccountCreationError] = useState("");

    const [registerFormData, setRegisterFormData] = useState({
        token: '',
        username: '',
        email: '',
        password: '',
        re_password: ''
    });

    const config = {
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    };

    const {token, username, email, password, re_password } = registerFormData;

    // to check whether an email has been registered
    async function has_email_registered(company_email) {
     
        try {
            const res = await axios.get(`${process.env.REACT_APP_API_URL}/api/account/?email=${company_email}`,config);
            
            if(res.data.length > 0){// if this email has been registered
                setAccountCreationError("This email has been registered.");

            }else{
                is_valid_email_token(token, email);
            }

        } catch (err) {
            setAccountCreationError("Invalid email.");

        }
    };

    // to validate token and company email address
    async function is_valid_email_token(token, token_email) {

        try {
            const res = await axios.get(`${process.env.REACT_APP_API_URL}/api/token/?token=${token}`,config);
            // if token does not exist or the email provided does not match the token provided
            if(res.data[0].email === token_email){
                has_username_registered(username);
                
            }else{
                setAccountCreationError("Invalid email or token.");
            }

        } catch (err) {
            setAccountCreationError("Invalid email or token.");
        }
    };

    // to check whether an username has been registered
    async function has_username_registered(created_username) {

        try {
            const res = await axios.get(`${process.env.REACT_APP_API_URL}/api/account/?username=${created_username}`,config);
            // if this username has been registered
            if(res.data.length > 0){
                setAccountCreationError("This username has been registered.");
            }else{
                passwordsMatch(password, re_password)
            }

        } catch (err) {
            setAccountCreationError("Invalid username");
        }
    };

    // check if the passwords match
    const passwordsMatch = (pwd1, pwd2) =>{
        if (password !== re_password ) {
            setAccountCreationError("Passwords do not match.");
        }else{
            signup(username, email, password);;
            setAccountCreationError("");

        }

    }


    const onChange = e => setRegisterFormData({ ...registerFormData, [e.target.name]: e.target.value });

    const onSubmit = e => {
        e.preventDefault();
        has_email_registered(email);  
    };
    
    
    if (isAuthenticated) {
        return <Redirect to='/' />
    }

    // if(message != null){
    //     document.getElementById("enterbutton2").disabled = true;
    // }
    const success_msg ="Password reset link has been sent to your email.";
    return (
        <div>
            <nav>
                <label className="logo"><span>!</span>H05T4G3S</label>
            </nav>
            <section>
                <div className="container">
                    <div className="user signinBx">
                        <div className="imgBx"><img src={registerLogo} alt="" /></div>
                        <div className="formBx">
                            <form action="" onSubmit={e => onSubmit(e)}>
                                <p style={{color: '#677eff'}}>{message}</p>
                                <p style={{color: '#A52A2A'}}>{accountCreationError}</p>
                                <h2>Create an account</h2>
                                <input type="text" id="tkn" name="token" placeholder="Pre-assigned Token" onChange={e => onChange(e)} required/>
                                <input type="email" name="email" value={email} placeholder="Company Email Address"onChange={e => onChange(e)} required/>
                                <input type="text" name="username" value={username} placeholder="Create username" onChange={e => onChange(e)} required/>
                                <input type="password" id="pw" name="password" value ={password}placeholder="Create Password" pattern="(?=.*\d).{10,20}" title="Must contain at least one letter, one number and 10-20 characters" onChange={e => onChange(e)} required/>
                                <input type="password" id="cpw" name="re_password" value ={re_password} placeholder="Confirm Password" onChange={e => onChange(e)} required/>
                                <input type="submit" id="enterbutton2" name="submit" value="Register" disabled={message==success_msg}/>
                                
                                <p className="signup">
                                    Already have an account ?
                                    <a href="/login" >Sign in.</a>
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
    message: state.auth.message
});

export default connect(mapStateToProps, { signup })(Signup);
