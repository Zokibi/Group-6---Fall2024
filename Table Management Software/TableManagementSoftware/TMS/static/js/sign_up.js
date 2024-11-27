let username = document.getElementById('#id_username');
let email = document.getElementById('#id_email');
let first_name = document.getElementById('#id_first_name');
let last_name = document.getElementById('#id_last_name');
let password1 = document.getElementById('#id_password1');
let password2 = document.getElementById('#id_password2');

function addPlaceholders(){
username.placeholder = " Enter Username";
email.placeholder = " Enter Email";
first_name.placeholder = " Enter First Name";
last_name.placeholder = " Enter Last Name";
password1.placeholder = " Enter Password";
password2.placeholder = " Re-enter Password";
}
