/* Project Queries */

const userFavorite = (accessToken) => {
  return {
    query: `
    query userFavorite($token: String!){
      allFavorite(idxUser: "3", token: $token) {
        edges {
          node {
            chart {
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
    variables: { token: accessToken },
  };
};

export { userFavorite };
