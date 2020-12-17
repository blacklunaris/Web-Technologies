import React from 'react';
import ReactDOM from 'react-dom';
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

class Header {
  constructor(){
    this.color = "Red";
  }

  //regular function
  changeColor = function(){
    document.getElementById("demo").innerHTML += this;
  }
}

myHeader= new Header ();
//The window calls the function:
window.addEventListener("load",myHeader.changeColor);

// A button object calls the function:
document.getElementById("btn").addEventListener("click", myHeader.changeColor);