import React, { Component } from "react";
import Logo from '../logo.svg'
class Header extends Component {
  render() {
    return (
      <div className="text-center">
        <img
          src={Logo}
          width="300"
          className="img-thumbnail"
          style={{ marginTop: "20px" }}
        />
        <hr />
        <h5>
          <i>UNIVERSITY OF CALICUT</i>
        </h5>
        <h1>STUDENT FORM</h1>
      </div>
    );
  }
}

export default Header;