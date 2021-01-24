/* React Imports */
import React from "react";
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
  return (
    <ApolloProvider client={client}>
      <BrowserRouter>
        <Switch>
          <Route path="/dashboard" component={Dashboard}></Route>
          <Route path="/login" component={Login}></Route>
          <Route path="/">
            <Redirect to="/dashboard"></Redirect>
          </Route>
        </Switch>
      </BrowserRouter>
    </ApolloProvider>
  );
}

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
