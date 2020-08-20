import React, {useState} from 'react';
import './login.css';
import PattooLogo from './assets/pattoo-light 1.png';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const updateLoginField = e => setUsername(e.target.value);
    const updatePasswordField = e => setPassword(e.target.value);

    return (
        <div className='login'>
            <div className='login_container'>

                <div className='container_header'>
                    <img src={PattooLogo} />
                    <h2>SIGN IN</h2>
                    <p>Hello! Sign in and start managing your Pattoo data!</p>
                </div>

                <div className='container_credentials'>
                    <input type='text' placeholder='Login' value={username} onChange={updateLoginField} />
                    <input type='password' placeholder='Password' value={password} onChange={updatePasswordField} />
                </div>

            </div>
        </div>
    )
}

export default Login;
