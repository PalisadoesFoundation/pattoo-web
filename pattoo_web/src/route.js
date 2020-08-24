/* Routes configuration */

/* Route components */
import Login from "./routes/login";
import Dashboard from "./routes/dashboard";

const ROUTES = [
  {
    paths: ["/login"],
    exact: true,
    component: Login,
  },
  {
    paths: ["/", "/dashboard", "/home"],
    exact: true,
    component: Dashboard,
  },
];
