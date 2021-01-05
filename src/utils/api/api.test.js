import {
    userAuth,
    userFavorite,
    createChart,
    createDatapoint,
    createFavorite,
} from "./api.js";
import uuid from "uuid";

test("Tests the userAuth function", () => {
    const randomUname = uuid.v4();
    const randomPass = uuid.v4();
    const result = {
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
    expect(userAuth(randomUname, randomPass)).toEqual(result);
});
uuid.v4();
test("Tests the userFavorite function", () => {
    // Initiaizing test variables
    const randomUserId = Math.floor(Math.random() * 100 + 1).toString();
    const randomAccessToken = uuid.v4();
    const result = {
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

    expect(userFavorite(randomUserId, randomAccessToken)).toEqual(result);
});

test("Tests the createFavorite function", () => {
    // Initializing test variables
    const userID = uuid.v4();
    const chartID = uuid.v4();
    const order = "0";
    const enabled = "0";
    const accessToken = uuid.v4();
    let expected = createFavorite(userID, chartID, order, enabled, accessToken);
    expected.query = expected.query.trim();
    let result = {
        query: "\n" +
            "        mutation createFavorite($userID: String!, $chartID: String!, $order: String!, $enabled: String!, $token: String!){\n" +
            "          createFavorite(Input: {idxUser: $userID, idxChart: $chartID, order: $order, enabled: $enabled}, token: $token) {\n" +
            "            favorite {\n" +
            "              __typename\n" +
            "              ... on Favorite {\n" +
            "                idxFavorite\n" +
            "                idxChart\n" +
            "              }\n" +
            "              __typename\n" +
            "              ... on AuthInfoField {\n" +
            "                message\n" +
            "              }\n" +
            "            }\n" +
            "          }\n" +
            "        }",
        variables: {
            userID: userID,
            chartID: chartID,
            order: order,
            enabled: enabled,
            token: accessToken,
        },
    };
    result.query = result.query.trim();
    expect(expected).toEqual(result);
});

test("Tests the createChart function", () => {});

test("Tests the createDatapoint function", () => {});