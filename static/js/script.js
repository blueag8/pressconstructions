
var request = new XMLHttpRequest()

request.open('GET', 'https://www.facebook.com/pg/pressconstructions/reviews/?ref=page_internal', true)
request.onload = function() {
  // Begin accessing JSON data here
  var data = JSON.parse(this.response)

  if (request.status >= 200 && request.status < 400) {
    data.forEach(review => {
      console.log(review)
    })
  } else {
    console.log('error')
  }
}

request.send()