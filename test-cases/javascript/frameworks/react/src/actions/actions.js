import {RESET, SEARCH} from './actionTypes';

export const reset = () => ({type: RESET});

export const search = query => ({type: SEARCH, payload: {query}});