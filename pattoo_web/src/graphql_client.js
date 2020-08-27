/* Makes queries to graphql server */

/* Imports */
const axios = require("axios").default;

const serverUrl = "http://localhost:20202/pattoo/api/v1/web/graphql";

async function queryResource(query) {
  return await axios({
    method: "post",
    url: serverUrl,
    data: { query: query },
  });
}

// Authenticates and saves access and refresh tokesn for `username` and `password`
async function authenticate(username, password) {
  const response = await axios({
    method: "post",
    url: serverUrl,
    data: {
      query: `
    mutation {
        authenticate(Input: {
            username: "${username}",
            password: "${password}"
        }){
            accessToken
            refreshToken
        }
    }`,
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

  return true;
}

function refreshToken(refreshToken) {}

export default queryResource;
export { authenticate, refreshToken };
