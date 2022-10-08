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
            
            // Create HTML Elements
            var node = document.createElement('div')
            var h2 = document.createElement('h2')
            var span1 = document.createElement('span')
            var span2 = document.createElement('span')
            var span3 = document.createElement('span')
            var span4 = document.createElement('span')
            var span5 = document.createElement('span')
            var span6 = document.createElement('span')
            var span7 = document.createElement('span')
            var span8 = document.createElement('span')
            var span9 = document.createElement('span')
            // create form & form inputs
            var form = document.createElement('form')
            var nameInput = document.createElement('input')
            var symbolInput = document.createElement('input')
            var exchangeInput = document.createElement('input')
            var datetimeInput = document.createElement('input')
            var volumeInput = document.createElement('input')
            var openInput = document.createElement('input')
            var highInput = document.createElement('input')
            var lowInput = document.createElement('input')
            var closeInput = document.createElement('input')
            var changeInput = document.createElement('input')
            var button = document.createElement('button')
            var submit = document.createTextNode('Save Stock to Watchlist')
            button.appendChild(submit)
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
            // Create form attributes
            form.setAttribute('method', 'post')
            form.setAttribute('action', '/images/create/')
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
            datetimeInput.setAttribute('type', 'hidden')
            datetimesrc = `${data.datetime}`
            datetimeInput.setAttribute('name', 'datetime')
            datetimeInput.setAttribute('value', datetimesrc)
            volumeInput.setAttribute('type', 'hidden')
            volumesrc = `${data.volume}`
            volumeInput.setAttribute('name', 'volume')
            volumeInput.setAttribute('value', volumesrc)
            openInput.setAttribute('type', 'hidden')
            opensrc = `${data.open}`
            openInput.setAttribute('name', 'open')
            openInput.setAttribute('value', opensrc)
            highInput.setAttribute('type', 'hidden')
            highsrc = `${data.high}`
            highInput.setAttribute('name', 'high')
            highInput.setAttribute('value', highsrc)
            lowInput.setAttribute('type', 'hidden')
            lowsrc = `${data.low}`
            lowInput.setAttribute('name', 'low')
            lowInput.setAttribute('value', lowsrc)
            closeInput.setAttribute('type', 'hidden')
            closesrc = `${data.close}`
            closeInput.setAttribute('name', 'close')
            closeInput.setAttribute('value', closesrc)
            changeInput.setAttribute('type', 'hidden')
            changesrc = `${data.change}`
            changeInput.setAttribute('name', 'change')
            changeInput.setAttribute('value', changesrc)
            // Append form attributes to the form
            form.appendChild(nameInput)
            form.appendChild(symbolInput)
            form.appendChild(exchangeInput)
            form.appendChild(datetimeInput)
            form.appendChild(volumeInput)
            form.appendChild(openInput)
            form.appendChild(highInput)
            form.appendChild(lowInput)
            form.appendChild(closeInput)
            form.appendChild(changeInput)
            form.appendChild(button)
            // Append API variables to HTML elements 
            h2.appendChild(name)
            span1.appendChild(symbol)
            span2.appendChild(exchange)
            span3.appendChild(datetime)
            span4.appendChild(volume)
            span5.appendChild(open)
            span6.appendChild(high)
            span7.appendChild(low)
            span8.appendChild(close)
            span9.appendChild(change)
            // Append all HTML elements to the node DIV element
            node.appendChild(h2)
            node.appendChild(span1)
            node.appendChild(span2)
            node.appendChild(span3)
            node.appendChild(span4)
            node.appendChild(span5)
            node.appendChild(span6)
            node.appendChild(span7)
            node.appendChild(span8)
            node.appendChild(span9)
            node.appendChild(form)
            // Appened node div to the HTML template (ID = stock)
            document.getElementById('stock').appendChild(node)
        // }
    })
}


