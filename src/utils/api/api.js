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

const createChart = (chartTitle, checksum, enabled, accessToken) => {
    return {
        query: `
    mutation createNewChart($name: String!, $checksum: String!, $enabled: String!, $token: String!){
        createChart(Input: {name: $name, checksum: $checksum, enabled: $enabled}, token: $token) {
            chart {
              __typename
              ... on Chart {
                    idxChart
                    name
                }
              __typename
              ... on AuthInfoField {
                    message
                }
            }
        }
    }
        `,
        variables: {
            name: chartTitle,
            checksum: checksum,
            enabled: enabled,
            token: accessToken,
        },
    };
};

const createDatapoint = (datapointID, chartID, enabled, accessToken) => {
    return {
        query: `
        mutation addDatapoint($datapointID: String!, $chartID: String!, $enabled: String!, $token: String!){
          createChartDataPoint(Input: {idxDatapoint: $datapointID, idxChart: $chartID, enabled: $enabled}, token: $token) {
            chartDatapoint {
              __typename
              ... on ChartDataPoint {
                idxChartDatapoint
                idxDatapoint
                idxChart
                }
              __typename
              ... on AuthInfoField {
                message
                }
            }
        }
    }
        `,
        variables: {
            datapointID: datapointID,
            chartID: chartID,
            enabled: enabled,
            token: accessToken,
        },
    };
};

const createFavorite = (userID, chartID, order, enabled, accessToken) => {
    return {
        query: `
        mutation createFavorite($userID: String!, $chartID: String!, $order: String!, $enabled: String!, $token: String!){
          createFavorite(Input: {idxUser: $userID, idxChart: $chartID, order: $order, enabled: $enabled}, token: $token) {
            favorite {maica fall relative to the others? 🤔 
              https://appinventiv.com/guide/mobile-app-development-cost/amp/
              “Apps Developed by Large App Development Companies, with a team size of cost 3000+ experts – cost $450,000 to $1,500,000”
              2:34 PM
              “3000 experts”
              2:34 PM
              +1 (876) 544-6673Pablooo
              Lol do I divide or multiply?
              2:39 PM
              +1 (876) 287-4267Jordan
              +1 (876) 544-6673Pablooo
              Lol do I divide or multiply?
              Divide by nuff
              2:40 PM
              
              __typename
              ... on Favorite {
                idxFavorite
                idxChart
              }
              __typename
              ... on AuthInfoField {
                message
              }
            }
          }
        }
        `,
        variables: {
            userID: userID,
            chartID: chartID,
            order: order,
            enabled: enabled,
            token: accessToken,
        },
    };
};

export { userAuth, userFavorite, createChart, createFavorite, createDatapoint };