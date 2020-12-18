import React, {useState} from 'react';
import "./login.css"
import ReactDOM from 'react-dom';
import { BrowserRouter as Router } from "react-router-dom";
import Auth0ProviderWithHistory from "./auth/auth0-provider-with-history";
import "./index.css"


//arrow function examples

/*
hello= () =>{
  return "Hello World!";
}
*/

/* with parameters
hello= () =>"Hello World!";
*/

/*
hello= (val) => "Hello" + val;
*/
/*for one parameter
hello= val =>"Hello" + val;

*/
/*
const myfirstelement = <h1>Hello React!</h1>

ReactDOM.render(myfirstelement, document.getElementById('root'));*/
/*
const myelement=(
  <div>
    <h1> I am a Header.</h1>
    <h1>I am a Header too.</h1>  
  </div>
);

ReactDOM.render(myelement, document.getElementById('root'));

*/
ReactDOM.render(
  <Router>
    <Auth0ProviderWithHistory>
      <App />
    </Auth0ProviderWithHistory>
  </Router>,
  document.getElementById("root")
);