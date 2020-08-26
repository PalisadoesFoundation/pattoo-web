/* Makes queries to graphql server */

/* Imports */
const axios = require("axios").default;

const serverUrl = "http://localhost:20202/pattoo/api/v1/web/graphql";

function queryResource(query) {}

// Authenticates and saves access and refresh tokesn for `username` and `password`
function authenticate(username, password) {
  const auth_query = `
    mutation {
        authenticate(Input: {
            username: ${username},
            password: ${password}
        }){
            accessToken
            refreshToken
        }
    }
    `;

  axios({
    method: "post",
    url: serverUrl,
    data: {
      query: auth_query,
    },
  })
    .then((response) => console.log(response))
    .catch((err) => console.log(`Error: ${err}`));
}

function refreshToken(refreshToken) {}

export default queryResource;
export { authenticate, refreshToken };
