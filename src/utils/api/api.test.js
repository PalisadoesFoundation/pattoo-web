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

test("Tests the userFavorite function", () => {
    // Initiaizing test variables
    const randomUserId = Math.floor(Math.random() * 100 + 1);
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

test("Tests the createChart function", () => {});

test("Tests the createDatapoint function", () => {});

test("Tests the createFavorite function", () => {});