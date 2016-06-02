//引入events模块
var events = require("events");
var os = require("os");
console.log(os.hostname());
console.log(os.type());
console.log(os.platform());
console.log(os.arch());
console.log(os.release());
console.log(os.cpus());
//创建eventEmitter对象
var eventEmitter = new events.EventEmitter();

//创建事件处理程序
var connectHandler = function connected(){
	console.log("连接成功...");
	//触发data_received事件
	eventEmitter.emit("data_received");
}

//绑定connection事件处理程序
eventEmitter.on("connection", connectHandler);

//使用匿名函数绑定data_received事件
eventEmitter.on("data_received", function(){
	console.log("数据接收成功");
});

//触connection事件
eventEmitter.emit("connection");

console.log("程序执行完毕！");
