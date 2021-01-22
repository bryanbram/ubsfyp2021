import {
    LOGIN_SUCCESS,
    LOGIN_FAIL,
    USER_LOADED_SUCCESS,
    USER_LOADED_FAIL,
    AUTHENTICATED_SUCCESS,
    AUTHENTICATED_FAIL,
    PASSWORD_RESET_SUCCESS,
    PASSWORD_RESET_FAIL,
    PASSWORD_RESET_CONFIRM_SUCCESS,
    PASSWORD_RESET_CONFIRM_FAIL,
    SIGNUP_SUCCESS,
    SIGNUP_FAIL,
    ACTIVATION_SUCCESS,
    ACTIVATION_FAIL,
    LOGOUT
} from '../actions/types';

const initialState = {
    access: localStorage.getItem('access'),
    refresh: localStorage.getItem('refresh'),
    isAuthenticated: null,
    error: null, 
    message: null,
    user: null
};

export default function(state = initialState, action) {
    const { type, payload } = action;

    switch(type) {
        case AUTHENTICATED_SUCCESS:
            return {
                ...state,
                isAuthenticated: true,
                error: null,
                message: null
            }
        case AUTHENTICATED_FAIL:
            return {
                ...state,
                isAuthenticated: false, 
                error: null,
                message: null
            }
        case LOGIN_SUCCESS:
            localStorage.setItem('access', payload.access);
            localStorage.setItem('refresh', payload.refresh);
            return {
                ...state,
                isAuthenticated: true,
                access: payload.access,
                refresh: payload.refresh, 
                error: null,
                message: null
            }
        case SIGNUP_SUCCESS:
            return {
                ...state,
                isAuthenticated: false,
                error: null,
                message: "Please check your email for the activation link."
            }
        case USER_LOADED_SUCCESS:
            return {
                ...state,
                user: payload
            }
        
        case USER_LOADED_FAIL:
            return {
                ...state,
                user: null
            }

        case LOGIN_FAIL:
            return {
                ...state,
                error: "login_fail",
                message: null
            }
        case SIGNUP_FAIL:
            return {
                message: null,
                error: null
            }
        case LOGOUT:
            localStorage.removeItem('access');
            localStorage.removeItem('refresh');
            return {
                ...state,
                access: null,
                refresh: null,
                isAuthenticated: false,
                user: null,
                error: null
            }
        case PASSWORD_RESET_SUCCESS:
            return {
                ...state,
                message: "Password reset link has been sent to your email.",
                error: null
            }
        
        case PASSWORD_RESET_FAIL:
            return {
                ...state,
                message: null,
                error: "User with given email does not exist."
            }
        case PASSWORD_RESET_CONFIRM_SUCCESS:
            return{
                ...state,
                message: "Password reset success.",
                error: null
            }
        case PASSWORD_RESET_CONFIRM_FAIL:
            return {
                ...state,
                message: null,
                error: "Password Reset failed."
            }
        case ACTIVATION_SUCCESS:
        case ACTIVATION_FAIL:
            return {
                ...state
            }
        default:
            return state
    }
};
