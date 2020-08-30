/* Project Queries */

const userAuth = (username, password) => {
  return {
    query: `
    mutation auth($username: String!, $password: String!){
        authenticate(Input: {
            username: $username,
            password: $password
        }){
            accessToken
            refreshToken
            idxUser
        }
    }`,
    variables: { username: username, password: password },
  };
};

const userFavorite = (idxUser, accessToken) => {
  return {
    query: `
    query userFavorite($idxUser: String! ,$token: String!){
      allFavorite(idxUser: $idxUser, token: $token) {
        edges {
          node {
            chart {
              name
              chartDatapointChart {
                edges {
                  node {
                    datapoint {
                      idxDatapoint
                      dataChecksum {
                        edges {
                          node {
                            value
                            timestamp
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    `,
    variables: { idxUser: idxUser, token: accessToken },
  };
};

export { userAuth, userFavorite };
