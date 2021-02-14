import { gql } from "@apollo/client";

// Authentication Mutations
const USER_AUTH = gql`
  mutation auth($username: String!, $password: String!) {
    authenticate(Input: { username: $username, password: $password }) {
      accessToken
      refreshToken
      idxUser
    }
  }
`;

// Chart Mutations
const CREATE_CHART = gql`
  mutation createNewChart(
    $name: String!
    $checksum: String!
    $enabled: String!
    $token: String!
  ) {
    createChart(
      Input: { name: $name, checksum: $checksum, enabled: $enabled }
      token: $token
    ) {
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
`;

// Favorites Mutations
const CREATE_FAVORITE = gql`
  mutation createFavorite(
    $userID: String!
    $chartID: String!
    $order: String!
    $enabled: String!
    $token: String!
  ) {
    createFavorite(
      Input: {
        idxUser: $userID
        idxChart: $chartID
        order: $order
        enabled: $enabled
      }
      token: $token
    ) {
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
  }
`;

// Datapoint Mutations
const CREATE_DATAPOINT = gql`
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
`;
