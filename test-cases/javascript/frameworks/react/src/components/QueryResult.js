import React from 'react';
import {connect} from 'react-redux';
import {reset} from '../actions/actions';

class QueryResult extends React.Component {
  componentDidMount() {
    this.props.reset();
  }

  componentDidUpdate() {
    this.props.reset();
  }

  render() {
    return (<h2>You have searched '{this.props.match.params.query}'</h2>);
  }
}

export default connect(
    null,
    { reset }
)(QueryResult);