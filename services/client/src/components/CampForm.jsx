import React, { useState } from 'react';
import 'react-widgets/dist/css/react-widgets.css';

import Form from 'react-bootstrap/Form';
import Collapse from 'react-bootstrap/Collapse'
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

import Moment from 'moment';
import momentLocalizer from 'react-widgets-moment';
import DateTimePicker from 'react-widgets/lib/DateTimePicker';

const CampForm = (props) => {

	Moment.locale('en');
	momentLocalizer();

	const [isParkSelected, selectPark] = useState(false);
	const [isCampSelected, selectCamp] = useState(false);

	return (
		<Form style={{ width: "inherit" }}>
		 <Row>
		  <Col>
		    <Form.Group controlId="exampleForm.ControlSelect1">
			  <Form.Label>Select A Park</Form.Label>
			  <Form.Control 
			    name="park" 
			    as="select" 
			    onChange={(event) => { 
			    	selectPark(true); 
			    	props.setChange(event) 
			    }}>
			      <option>1</option>
			      <option>2</option>
			      <option>3</option>
			      <option>4</option>
			      <option>5</option>
			  </Form.Control>
		    </Form.Group>
		   </Col>
		  </Row>
		  <Collapse in={isParkSelected}>
		    <Row>
		      <Col>
			    <Form.Group controlId="exampleForm.ControlSelect1">
				  <Form.Label>Select A Campground</Form.Label>
				  <Form.Control 
				    name="camp" 
				    as="select" 
				    onChange={(event) => {
				    	selectCamp(true);
				    	props.setChange(event);
				    }}>
				      <option>1</option>
				      <option>2</option>
				      <option>3</option>
				      <option>4</option>
				      <option>5</option>
				  </Form.Control>
			    </Form.Group>
			  </Col>
			</Row>
		  </Collapse>
		  <Collapse in={isCampSelected}>
		    <Row>
		      <Col xs={8}>
		        <Form.Group controlId="formDatepicker">
		          <Form.Label>Arrival Date</Form.Label>
		          <DateTimePicker 
		          	name="arrivalDate"
		            defaultValue={ null } 
		            time={ false }
		            onChange={(value) => props.setChange(
		            		{ target: {name: "arrivalDate", value: value}}
		            	)}
		          />
		        </Form.Group>
		      </Col>
		      <Col>
		        <Form.Group controlId="formNoNights">
		          <Form.Label>Number of Nights</Form.Label>
		          <Form.Control 
		            as="select"
		            name="noNights"
		            onChange={(event) => props.setChange(event)}
		          >
		            {[...Array(14)].map((e, i) => 
		          			<option>{i + 1}</option>
		            )}
		          </Form.Control>
		        </Form.Group>
		      </Col>
		    </Row>
		  </Collapse>
		  <Collapse in={isCampSelected}>
		    <Row>
		      <Col>
			   <Form.Group controlId="formBasicEmail">
			     <Form.Label>Email address</Form.Label>
			     <Form.Control 
			    	type="email" 
			    	name="email" 
			    	placeholder="Enter email" 
			    	onChange={(event) => props.setChange(event)}
			    />
			     <Form.Text className="text-muted">
			      Enter the email you want your notification sent to
			     </Form.Text>
			   </Form.Group>
			  </Col>
			</Row>
		  </Collapse>
	  </Form>	
	)
} 

export default CampForm;