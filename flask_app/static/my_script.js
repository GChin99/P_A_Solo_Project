// stock API
var myForm = document.getElementById('myForm');
myForm.onsubmit = function(e){
    // "e" is the js event happening when we submit the form.
    // e.preventDefault() is a method that stops the default nature of javascript.
    // We do not what the form to do anything but wait for the submission
    e.preventDefault();
    // create FormData object from javascript and send it through a fetch post request. We get a key and the value we put into the input
    var form = new FormData(myForm);
    // this how we set up a post request and send the form data.
    fetch("http://localhost:5000/stock_data", { method :'POST', body : form})
        .then( response => response.json() )
        .then( data => console.log(data) )
}


