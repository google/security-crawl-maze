import React from 'react';
import {Nav, Navbar} from 'react-bootstrap';
import {LinkContainer} from 'react-router-bootstrap'
import {BrowserRouter as Router, Link, Route} from 'react-router-dom';

import Home from '../components/Home';
import QueryResult from '../components/QueryResult'
import SearchWidget from '../components/SearchWidget';

const Index = () => {
  return <Home />;
};

const NavLink = () => {
  return <h2>NavLink</h2>;
};

class Navigation extends React.Component {

  render() {
    return (
      <Router basename="/javascript/frameworks/react">
        <div>
          <Navbar bg="dark" variant="dark" expand="lg">
            <Navbar.Brand className="brand">
              <Link to = '/index.html'>Security crawl maze</Link>
            </Navbar.Brand>
              <br></br>
            <Nav className = 'top-nav mr-auto'>
              <LinkContainer to = '/index.html'>
                <Nav.Link>Home</Nav.Link>
              </LinkContainer>
              <br></br>
              <LinkContainer to = '/route-path.found'>
                <Nav.Link>NavLink</Nav.Link>
              </LinkContainer>
            </Nav>
            <Nav>
              <SearchWidget/>
            </Nav>
            <br></br>
        </Navbar>

        <Route path='/index.html' component={Index}/>
        <Route path='/route-path.found' component={NavLink}/>
        <Route path='/search.found/:query' component={QueryResult}/>
      </div>
    </Router>
    );
}
}

export default Navigation;
