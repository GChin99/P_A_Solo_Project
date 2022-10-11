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
            .then( data => {
            console.log(data)
            //we need a JavaScript for loop to go through the array of objects 
        // for (let i=0; i < data.length; i++){
            // However,this API just returns a single object so we do not need to loop through an array of objects
            

            var node = document.createElement('div')
            var h2 = document.createElement('h2')
            // Create HTML table 
            var table = document.createElement('table')
            var thead = document.createElement('thead')
            var tbody = document.createElement('tbody')
            table.appendChild(thead)
            table.appendChild(tbody)
            // Creating and adding data to first row of the table
            var row_1 = document.createElement('tr')
            var heading_1 = document.createElement('th')
            heading_1.innerHTML = "Symbol"
            var heading_2 = document.createElement('th')
            heading_2.innerHTML = "Exchange"
            var heading_3 = document.createElement('th')
            heading_3.innerHTML = "Date"
            var heading_4 = document.createElement('th')
            heading_4.innerHTML = "Volume"
            var heading_5 = document.createElement('th')
            heading_5.innerHTML = "Open"
            var heading_6 = document.createElement('th')
            heading_6.innerHTML = "High"
            var heading_7 = document.createElement('th')
            heading_7.innerHTML = "Low"
            var heading_8 = document.createElement('th')
            heading_8.innerHTML = "Close"
            var heading_9 = document.createElement('th')
            heading_9.innerHTML = "% Change"

            row_1.appendChild(heading_1)
            row_1.appendChild(heading_2)
            row_1.appendChild(heading_3)
            row_1.appendChild(heading_4)
            row_1.appendChild(heading_5)
            row_1.appendChild(heading_6)
            row_1.appendChild(heading_7)
            row_1.appendChild(heading_8)
            row_1.appendChild(heading_9)
            thead.appendChild(row_1)
            
            // Create Variables from API data
            var name = document.createTextNode(data.name)
            var symbol = document.createTextNode(data.symbol)
            var exchange = document.createTextNode(data.exchange)
            var datetime = document.createTextNode(data.datetime)
            var volume = document.createTextNode(data.volume)
            var open = document.createTextNode(data.open)
            var high = document.createTextNode(data.high)
            var low = document.createTextNode(data.low)
            var close = document.createTextNode(data.close)
            var change = document.createTextNode(data.change)

            // Creating and adding data to second row of the table
            var row_2 = document.createElement('tr')
            var row_2_data_1 = document.createElement('td')
            row_2_data_1.appendChild(symbol)
            var row_2_data_2 = document.createElement('td')
            row_2_data_2.appendChild(exchange)
            var row_2_data_3 = document.createElement('td')
            row_2_data_3.appendChild(datetime)
            var row_2_data_4 = document.createElement('td')
            row_2_data_4.appendChild(volume)
            var row_2_data_5 = document.createElement('td')
            row_2_data_5.appendChild(open)
            var row_2_data_6 = document.createElement('td')
            row_2_data_6.appendChild(high)
            var row_2_data_7 = document.createElement('td')
            row_2_data_7.appendChild(low)
            var row_2_data_8 = document.createElement('td')
            row_2_data_8.appendChild(close)
            var row_2_data_9 = document.createElement('td')
            row_2_data_9.appendChild(change)

            row_2.appendChild(row_2_data_1)
            row_2.appendChild(row_2_data_2)
            row_2.appendChild(row_2_data_3)
            row_2.appendChild(row_2_data_4)
            row_2.appendChild(row_2_data_5)
            row_2.appendChild(row_2_data_6)
            row_2.appendChild(row_2_data_7)
            row_2.appendChild(row_2_data_8)
            row_2.appendChild(row_2_data_9)
            tbody.appendChild(row_2)

            // create form & form inputs
            var form = document.createElement('form')
            var nameInput = document.createElement('input')
            var symbolInput = document.createElement('input')
            var exchangeInput = document.createElement('input')
            var button = document.createElement('button')
            var submit = document.createTextNode('Save Stock to Watchlist')
            var watchlistID = document.querySelector(".wOption")
            console.log(watchlistID)
            var value = watchlistID.options[watchlistID.selectedIndex].value
            console.log("the value of var value:", value)
            // var valueInt = parseInt(value)
            // console.log(valueInt)
            // console.log(typeof(valueInt ))
            var watchlistInput = document.createElement('input')
            button.appendChild(submit)

            // Create form attributes
            form.setAttribute('method', 'post')
            form.setAttribute('action', '/stock/save/')
            nameInput.setAttribute('type', 'hidden')
            namesrc = `${data.name}`
            nameInput.setAttribute('name', 'name')
            nameInput.setAttribute('value', namesrc)
            symbolInput.setAttribute('type', 'hidden')
            symbolsrc = `${data.symbol}`
            symbolInput.setAttribute('name', 'symbol')
            symbolInput.setAttribute('value', symbolsrc)
            exchangeInput.setAttribute('type', 'hidden')
            exchangesrc = `${data.exchange}`
            exchangeInput.setAttribute('name', 'exchange')
            exchangeInput.setAttribute('value', exchangesrc)
            watchlistInput.setAttribute('type', 'hidden')
            // console.log(typeof value)
            valuesrc = parseInt(value)
            // parseInt here isnt necessary becuase the type hidden will turn the value back into a string 
            // we need to change the string to an int in the stock/save route in the stock controller file
            console.log("this is valuesrc:", valuesrc)
            console.log("the type of valuesrc:", typeof(valuesrc ))
            watchlistInput.setAttribute('name', 'watchlist_id')
            watchlistInput.setAttribute('value', valuesrc)
            console.log("wathclistInput is:", watchlistInput)
            console.log(form)


            // Append form attributes to the form
            form.appendChild(nameInput)
            form.appendChild(symbolInput)
            form.appendChild(exchangeInput)
            form.appendChild(watchlistInput)
            form.appendChild(button)

            h2.appendChild(name)
            node.appendChild(h2)
            node.appendChild(table)
            node.appendChild(form)

            // Appened table to the HTML template (ID = stock)
            document.getElementById('stock').appendChild(node)
            document.getElementById("stock").value = ""

    })
}


// When we have more time, come back and make the create watchlist with JS.  
// This way, the page is not reloading and we are not rendering different templates. 
//also look up request.JSON instead of request.form and JSON post request
