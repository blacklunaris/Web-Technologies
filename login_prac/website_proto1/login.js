function validate(){
    let username=document.getElementById("username").value;
    let password=document.getElementById("password").value;
    if(username==null || username==""){
        alert("Please enter username.");
        return false;
    }
    if(password==null || password==""){
        alert("Please enter password.");
        return false;
    }
    if(username=="admin" && password=="pass")
    {
        alert("Login successful");
        window.location="homepage.html";
    
    }
    else{
        alert("Login failed");
    
    }
}
function register(){
    alert("Please enter your credentials.");
    window.location="register.html";
}


validate();

