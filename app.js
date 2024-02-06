const http = require('http')
const fs = require('fs')
const port = 3000


const server = http.createServer(function(req, res) {
    //res.writeHead(200, { 'Content-Type': 'text/html'})
    let requestedUrl = req.url.substr(1)

    fs.readFile(requestedUrl, function(error, data) {
        if (error) {
            res.writeHead(404)
            res.write('Error: File Not Found')
        }
        else {
            //res.setHeader('Access-Control-Allow-Origin', '*')
            res.write(data)
        }
        res.end()
    })
})

server.listen(port, function(error) {
    if (error) {
        console.log('Something went wrong', error)
    }
    else {
        console.log('Server is listening on port ' + port)
    }
})