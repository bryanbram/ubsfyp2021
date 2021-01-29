import React, { useState } from 'react';
import { Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import { reset_password } from '../actions/authenticate';
import logo from './picture/microchip.jpg';

const ResetPassword = ({ reset_password, message, error }) => {
    //const [requestSent, setRequestSent] = useState(false);
    const [formData, setFormData] = useState({
        email: ''
    });

    const { email } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = e => {
        e.preventDefault();

        reset_password(email);
        // setRequestSent(true);
    };

    // if (requestSent) {
    //     return <Redirect to='/' />
    // }

    return (
        <div>
        <nav>
            <label className="logo"><span>!</span>H05T4G3S</label>
        </nav>
        <section>
            <div className="container">
                <div className="user signinBx">
                    <div className="imgBx"><img src={logo} alt="" /></div>
                    <div className="formBx">
                        <form action="" onSubmit={e => onSubmit(e)}>
                            <p style={{color: '#677eff'}}>{message}</p> 
                            <p style={{color: '#A52A2A'}}>{error}</p>
                            <h2>Password Reset Request</h2>
                            <input type="email" name="email" value={email} placeholder="Company Email Address" onChange={e => onChange(e)} required/>
                            <input type="submit" id="enterbutton2"  value="Reset" />
                            <p className="signup">
                                Already have an account ?
                                <a href="/login" >Sign in.</a>
                            </p>
                            <p className="signup">
                                Don't have an account ?
                                <a href="/signup">Register.</a>
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
    error: state.auth.error,
    message: state.auth.message
});
export default connect(mapStateToProps , { reset_password })(ResetPassword);
