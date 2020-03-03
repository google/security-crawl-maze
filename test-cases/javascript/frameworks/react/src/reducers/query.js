import {RESET, SEARCH} from '../actions/actionTypes';

const initialState = {
  query: '',
  loadQueryResult: false
};

export default function queryActions(state = initialState, action) {
  switch (action.type) {
    case RESET: {
      return {...state, query: '', loadQueryResult: false};
    }
    case SEARCH: {
      return {...state, query: action.payload.query, loadQueryResult: true};
    }
    default:
      return state;
  }
}
