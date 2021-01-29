import React, { useState } from 'react';
import { Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import { reset_password_confirm } from '../actions/authenticate';
import logo from './picture/eye.jpg';

const ResetPasswordConfirm = ({ match, message, error, reset_password_confirm }) => {

    const [formData, setFormData] = useState({
        new_password: '',
        new_password2: ''
    });

    const { new_password, new_password2 } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = e => {
        e.preventDefault();

        const uid = match.params.uid;
        const token = match.params.token;

         // check if the passwords match
        if (new_password !== new_password2) {
            alert("Passwords do not match.");
        }else{
            reset_password_confirm(uid, token, new_password);
           
        }

    };

    if (message === "Password reset success.") {
        return <Redirect to='/login' />
    }

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
                                {/* <p style={{color: '#677eff'}}>{message}</p> */}
                                <p style={{color: '#A52A2A'}}>{error}</p>
                                <h2>Password Reset:</h2>
                                <input
                                    type='password'
                                    placeholder='Create New Password'
                                    name='new_password'
                                    value={new_password}
                                    onChange={e => onChange(e)}
                                    pattern="(?=.*\d).{10,20}" 
                                    title="Must contain at least one letter, one number and 10-20 characters"
                                    required
                                />
                                <input
                                    type='password'
                                    placeholder='Confirm New Password'
                                    name='new_password2'
                                    value={new_password2}
                                    onChange={e => onChange(e)}
                                    pattern="(?=.*\d).{10,20}" 
                                    title="Must contain at least one letter, one number and 10-20 characters"
                                    required
                                />
                                <input type="submit" id="enterbutton2" name="submit" value="Confirm" />
            
                            </form>
                        </div>
                    </div>
                </div>
            </section>
       </div>
    );
};

const mapStateToProps = state => ({
    message: state.auth.message,
    error: state.auth.error
});

export default connect(mapStateToProps, { reset_password_confirm })(ResetPasswordConfirm);
