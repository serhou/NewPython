console.log("Hello World!");
var http = require("http");

http.createServer(function (request, response) {
	//发送HTTP头部
	//HTTP 状态值 200 : OK
	response.writeHead(200, {'Content-Type':'text/plain'});
	//发送相应数据
	response.end('Hello World\n');
}).listen(9999);

console.log('Server running at http://127.0.0.1:9999/');
