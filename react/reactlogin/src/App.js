import React from "react";
import userstore from './stores/userstore';
import loginform from './loginform';
import inputfield from './inputfield';
import submitButton from './submitButton';
import './App.css';

class App extends React.Component {

  async componentDidMount(){
    try {
      let res =await fetch('/isLoggedIn',{
        method:'post',
        headers:{
          'Accept':'application/json',
          'Content-type':'application/json'
        }
      });
      let result =await res.json();

      if(result && result.success){
        userstore.loading=false;
        userstore.isLoggedIn=true;
        userstore.username=result.username;
      }
      else{
        userstore.loading=false;
        userstore.isLoggedIn=false;
      }
    } 
    catch (error) {
      userstore.loading=false;
      userstore.isLoggedIn=false;
      
    }
  }

  async doLogout(){
    try {
      let res =await fetch('/logout',{
        method:'post',
        headers:{
          'Accept':'application/json',
          'Content-type':'application/json'
        }
      });
      let result =await res.json();
      
      if(result && result.success){
        
        userstore.isLoggedIn=false;
        userstore.username='';
      }

    } 
    catch (error) {
      console.log(e);
      
    }
  }
  render() {
    if (userstore.loading) {
      return(
        <div className="app"> 
          <div className="container">
            Loading, please wait..
          </div>
        </div>

      );
      
    }
    return (
      <div className="App">
     
      </div>
    );
  }
}

export default App;
