/* React Imports */
import React from "react";
import { Route, Redirect } from "react-router-dom";
import PropTypes from 'prop-types';

function ProtectedRoute({isAuth:isAuth, component: Component, ...props}) {
    return (
      <Route
        {...props}
        render={(props) => {
          if (isAuth) {
            return <Component {...props} />;
          }else{
            return <Redirect to="/login" />;
          }
        }}
      />
    );
}

export default ProtectedRoute;

ProtectedRoute.propTypes = {
    isAuth: PropTypes.bool,
    component: PropTypes.component
};