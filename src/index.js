/* React Imports */
import React, {useState} from "react";
import ReactDOM from "react-dom";
import { BrowserRouter, Switch, Route, Redirect } from "react-router-dom";

/* GraphQL and Apollo imports */
import {
  ApolloClient,
  InMemoryCache,
  ApolloProvider,
  HttpLink,
  from,
} from "@apollo/client";

import { onError } from "@apollo/client/link/error";

/* Styles Imports */
import "./styles/main.css";

/* Component Imports */
import Dashboard from "./components/Dashboard/Dashboard";
import Login from "./components/Login/Login";
import ProtectedRoute from "./routes/ProtectedRoute"

// Catches and logs graphql errors
const errorLink = onError(({ graphqlErrors }) => {
  if (graphqlErrors) {
    graphqlErrors.map(({ message }) => {
      alert(`A graphQl error occurred ${message}`);
    });
  }
});

// Creating the link to fetch data from graphql
const link = from([
  errorLink,
  new HttpLink({ uri: "http://localhost:20202/pattoo/api/v1/web/graphql" }),
]);

// Initialize the Apollo Client
const client = new ApolloClient({
  cache: new InMemoryCache(),
  link: link,
});

function App() {
  // Temporary routing until authentication is complete

  //[isAuth,setAuth]
  const [isAuth] = useState(true); //defaulted to true until authentication is implemented
  return (
        <Switch>
          <ProtectedRoute path="/dashboard" exact component={Dashboard} isAuth={isAuth}/>
          <Route path="/login" exact component={Login}></Route>
          <Route path="/" exact>
            <Redirect to="/dashboard"></Redirect>
          </Route>
        </Switch>
  );
}

ReactDOM.render(
  <React.StrictMode>
    <ApolloProvider client={client}>
      <BrowserRouter>
        <App /> 
      </BrowserRouter>
    </ApolloProvider>
  </React.StrictMode>,
  document.getElementById("root")
);
