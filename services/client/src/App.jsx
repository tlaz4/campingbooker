import React, { Component } from 'react';

import CampForm from './components/CampForm.jsx';
import './index.css';

import Navbar from 'react-bootstrap/Navbar';
import Nav from 'react-bootstrap/Nav';
import Container from 'react-bootstrap/Container';

class App extends Component {
	constructor(){
		super();
		this.state = {
			users: [],
			camp: null,
			park: null,
			email: null,
			arrivalDate: null,
			noNights: 1

		}

		this.getUsers = this.getUsers.bind(this);
		this.setChange = this.setChange.bind(this);
	}

	getUsers(){
		fetch(`${process.env.REACT_APP_USERS_SERVICE_URL}api/users`)
		.then(results => {
			return results.json()
		}).then(data => {
			if(data.status == 'success'){
				console.log(data);
				this.setState({users: data.data.users});
			}
		});
	}

	setChange(event){
		console.log(event.target.name, event.target.value);
		this.setState({ [event.target.name] : event.target.value })
	}

	componentDidMount(){
		this.getUsers();
	}

	render(){
		return (
			<div>
				<Navbar style={{ backgroundColor: "#6B9169"}} variant="dark">
    			  <Navbar.Brand href="#home">Camp</Navbar.Brand>
    			  <Nav className="ml-auto">
    			    <Nav.Link href="#Watchlist">Watch List</Nav.Link>
    			  	<Nav.Link href="#Register">Register</Nav.Link>
    			  </Nav>
  				</Navbar>
				<ul>
					{this.state.users.map(user => (
						<li key={user.id}>
							<h5>{user.email}</h5>
						</li>
					))}
				</ul>
				<div className="container">
					<CampForm setChange={this.setChange}/>
				</div>
			</div>
		)
	}
}

export default App;
