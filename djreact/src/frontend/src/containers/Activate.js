import React, { useState } from 'react';
import { Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import { verify_email_for_activation } from '../actions/authenticate';
import './css/login.css'
import logo from './picture/eye.jpg';

const Activate = ({ verify_email_for_activation, match }) => {
    const [verified, setVerified] = useState(false);

    const verify_account = e => {
        const uid = match.params.uid;
        const token = match.params.token;

        verify_email_for_activation(uid, token);
        setVerified(true);
    };

    if (verified) {
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
                         <form action="" onSubmit={e => verify_account(e)}>
                             <h2>Activate your Account:</h2>
                             <input type="submit" id="enterbutton2" name="submit" value="Activate" />
            
                         </form>
                     </div>
                 </div>
             </div>
         </section>

        </div>
    );
};

export default connect(null, { verify_email_for_activation })(Activate);
