/* Authentication query */
import { userAuth } from "utils/api";

/* Imports */
import axios from "axios";

const serverUrl = "http://localhost:20202/pattoo/api/v1/web/graphql";

async function query(data) {
  return await axios({
    method: "post",
    url: serverUrl,
    data: {
      query: data.query,
      variables: data.variables,
    },
  });
}

// Authenticates and saves access and refresh tokesn for `username` and `password`
async function authenticate(username, password) {
  const data = userAuth(username, password);
  const response = await axios({
    method: "post",
    url: serverUrl,
    data: {
      query: data.query,
      variables: data.variables,
    },
  });

  if (response.data.data.authenticate === null) {
    return false;
  }

  localStorage.setItem(
    "accessToken",
    response.data.data.authenticate.accessToken
  );
  localStorage.setItem(
    "refreshToken",
    response.data.data.authenticate.refreshToken
  );

  localStorage.setItem("userID", response.data.data.authenticate.idxUser);

  return true;
}

function refreshToken(refreshToken) {}

export default query;
export { authenticate, refreshToken };
