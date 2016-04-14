//导入mysql模块
var mysql = require("mysql");
var TEST_DATABASE = "webnav";
var TEST_TABLE = "web";

//创建连接
var client = mysql.createConnection({
	host:"192.168.1.108",
	port:"3306",
	user:"webnav",
	password:"webnav",
	database:"webnav"
});

client.connect();
client.query("select * from " + TEST_TABLE, function (err, results, fields){
	if(err){
		throw err;
	}
	if(results){
		for(var i=0; i < results.length; i++){
			console.log("%s\t----%s\t", results[i].webname, results[i].weburl);
		}
	}
});
client.query("select * from weather", function (err, results, fields){
	if(err){
	    throw err;
	}
	if(results){
	    for(var i=0;i<results.length;i++){
		console.log("%s\t%s\t%s\t%s\t",results[i].city, results[i].weatherinfo, results[i].airquality, results[i].liveindex);
	    }
	}
});
client.end();


