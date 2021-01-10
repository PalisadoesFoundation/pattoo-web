import {
    userAuth,
    userFavorite,
    createChart,
    createDatapoint,
    createFavorite,
} from "./api.js";

import { v4 as uuidv4 } from "uuid";

test("Tests the userAuth function", () => {
    const randomUname = uuidv4();
    const randomPass = uuidv4();
    const result = userAuth(randomUname, randomPass);
    const expected = {
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
        variables: { username: randomUname, password: randomPass },
    };
    expect(expected).toEqual(result);
});
uuidv4();
test("Tests the userFavorite function", () => {
    // Initiaizing test variables
    const randomUserId = Math.floor(Math.random() * 100 + 1).toString();
    const randomAccessToken = uuidv4();
    const result = userFavorite(randomUserId, randomAccessToken);
    const expected = {
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
        variables: { idxUser: randomUserId, token: randomAccessToken },
    };

    expect(expected).toEqual(result);
});

test("Tests the createFavorite function", () => {
    // Initializing test variables
    const userID = uuidv4();
    const chartID = uuidv4();
    const order = "0";
    const enabled = "0";
    const accessToken = uuidv4();
    const result = createFavorite(userID, chartID, order, enabled, accessToken);
    const expected = {
        query: `
        mutation createFavorite($userID: String!, $chartID: String!, $order: String!, $enabled: String!, $token: String!){
          createFavorite(Input: {idxUser: $userID, idxChart: $chartID, order: $order, enabled: $enabled}, token: $token) {
            favorite {
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
        }`,
        variables: {
            userID: userID,
            chartID: chartID,
            order: order,
            enabled: enabled,
            token: accessToken,
        },
    };
    expect(expected).toEqual(result);
});

test("Tests the createChart function", () => {
    // Initializing test variables
    const chartTitle = uuidv4();
    const checksum = uuidv4();
    const enabled = "0";
    const accessToken = uuidv4();
    const result = createChart(chartTitle, checksum, enabled, accessToken);
    const expected = {
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
    expect(expected).toEqual(result);
});

test("Tests the createDatapoint function", () => {
    const datapointID = uuidv4();
    const chartID = uuidv4();
    const enabled = "0";
    const accessToken = uuidv4();
    const result = createDatapoint(datapointID, chartID, enabled, accessToken);
    const expected = {
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
});