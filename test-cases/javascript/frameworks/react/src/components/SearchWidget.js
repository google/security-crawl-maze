import React from 'react';
import {Button, Form, FormControl} from 'react-bootstrap';
import {connect} from 'react-redux';
import {Redirect} from 'react-router-dom';

import {search} from '../actions/actions';


class SearchWidget extends React.Component {
  handleSubmit = (e) => {
    e.preventDefault();
    this.props.search(e.target.elements.query.value);
  };

  render() {
    if (this.props.loadQueryResult) {
      return <Redirect to={`/search.found/${this.props.query}`} />
    }

    return (<Form inline onSubmit={this.handleSubmit}>
            <FormControl required type = 'text' placeholder =
                 'Search' className = 'mr-sm-2' name = 'query'
            />
            <Button variant = 'outline-primary' type = 'submit'>
                Search</Button>
        </Form>);
    }
  }

  const mapStateToProps =
      state => {
        return {
          query: state.queryActions.query,
          loadQueryResult: state.queryActions.loadQueryResult
        };
      }

  export default connect(mapStateToProps, {search})(SearchWidget);
