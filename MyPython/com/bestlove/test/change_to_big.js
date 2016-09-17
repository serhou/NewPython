
// 引入readline模块
var readline = require('readline');

//创建readline接口实例
var  rl = readline.createInterface({
    input:process.stdin,
    output:process.stdout
});

// question方法
rl.question("输入要转换的金额：\n",function(answer){
    console.info(getBigMoney(answer));
    // 不加close，则不会结束
    rl.close();
});

// close事件监听
rl.on("close", function(){
   // 结束程序
    process.exit(0);
});


function getBigMoney(str) {
	//金额格式
	var reg = /^[0-9]{1,13}[.]{0,1}[0-9]{0,2}$/;
	//判断是否为空
	if (str!=null && str.trim()!="") {
		//去除逗号,
		var str1 = restoreMoney(str.trim());
		//开头是负号-
		if(str1.indexOf("-")==0){
			//正则表达式来过滤用户输入的数字
			if(!str1.substring(1).match(reg)){
				return "您输入的数字金额不符合要求：(-)###,###.##或(-)######.##";
			}
			return "负" + changetobig(str1.substring(1));//去除负号
		}else{
			if(!str1.match(reg)){
				return "您输入的数字金额不符合要求：(-)###,###.##或(-)######.##";
			}
			return changetobig(str1);
		}

	} else {
		//返回空
		return str;
	}
}




//转换大小写
function changetobig(str){
	//0; 0.0 ; 0.00 这三种情况要单列出来,还有0.这种情况，一般不会发生，这里也考虑上
	if("0" == str || "0." == str || "0.0" == str || "0.00" == str){
		return "零元整";
	}else{
		if(str.indexOf(".") < 0){//只有整数部分没有小数部分的问题100; 9; 1000
	        str = str + ".00";
		}
	}
	var str1=str;
	var i=0;
	var ss="";
	i=str1.indexOf(".");
	var t=0;

	for(var k=i;k>=0;k--){

	if(str1.charAt(k)=="0"){
	    if(t!=0){
	    ss+="零";
	    }

	  }
	  if(str1.charAt(k)=="1"){
	    ss+="壹";
	  }
	  if(str1.charAt(k)=="2"){
	    ss+="贰";
	  }
	  if(str1.charAt(k)=="3"){
	    ss+="叁";
	  }
	  if(str1.charAt(k)=="4"){
	    ss+="肆";
	  }
	  if(str1.charAt(k)=="5"){
	    ss+="伍";
	  }
	  if(str1.charAt(k)=="6"){
	    ss+="陆";
	  }
	  if(str1.charAt(k)=="7"){
	    ss+="柒";
	  }
	  if(str1.charAt(k)=="8"){
	    ss+="捌";
	  }
	  if(str1.charAt(k)=="9"){
	    ss+="玖";
	  }

	  if(t==1){  ss+="元";}
	  if(t==2){  ss+="拾";}
	  if(t==3){  ss+="佰";}
	  if(t==4){  ss+="仟";}
	  if(t==5){  ss+="万";}
	  if(t==6){  ss+="拾";}
	  if(t==7){  ss+="佰";}
	  if(t==8){  ss+="仟";}
	  if(t==9){  ss+="亿";}
	  if(t==10){ ss+="拾";}
	  if(t==11){ ss+="佰";}
	  if(t==12){ ss+="仟";}
	  if(t==13){ ss+="万";}
	  ss+=",";t++;

	}
	var jm=ss.split(",");
	var re="";
	var mu="";
	var u=jm.length-1;
	for(u;u>=0;u--){
	re+=jm[u];
	}
	var f=0;
	var mm=i+1;
	for(mm;mm<str1.length;mm++){
	 if(str1.charAt(mm)=="0"){
	    mu+="零";
	  }
	  if(str1.charAt(mm)=="1"){
	    mu+="壹";
	  }
	  if(str1.charAt(mm)=="2"){
	    mu+="贰";
	  }
	  if(str1.charAt(mm)=="3"){
	    mu+="叁";
	  }
	  if(str1.charAt(mm)=="4"){
	    mu+="肆";
	  }
	  if(str1.charAt(mm)=="5"){
	    mu+="伍";
	  }
	  if(str1.charAt(mm)=="6"){
	    mu+="陆";
	  }
	  if(str1.charAt(mm)=="7"){
	    mu+="柒";
	  }
	  if(str1.charAt(mm)=="8"){
	    mu+="捌";
	  }
	  if(str1.charAt(mm)=="9"){
	    mu+="玖";
	  }
	  if(f==0){mu+="角";}
	  if(f==1){mu+="分";}
	  f++;
	}
	if(mu=="零角零分"){
	re+="整";
	}else{
	re+=mu;
	}
	var results="";
	var mresults="";
	var temp="";
	var lflags='false';
	var lflag1='false';

	for(var ink=0;ink<re.length;ink++){
	  if(lflags=='true'){

		  if(re.charAt(ink)=="亿"||re.charAt(ink)=="万"||re.charAt(ink)=="元")


		    results+=re.charAt(ink);


	     lflags="false";
	      continue;
	  }
	  if(re.charAt(ink)!="零"){
		  if(lflag1=='true'&&re.charAt(ink)!="整"){
		  results+="零";
		   }
		results+=re.charAt(ink);
		lflags="false";
		lflag1="false";

	  }else {

	     lflags="true";
	     lflag1="true";
	  }

	}
	  for(var mts=0;mts<results.length;mts++){
	   mresults+=results.charAt(mts);
	   if(results.charAt(mts)=="亿"){

	   if(results.charAt(mts+1)=="万"){

	   mts++;
	   }

	   }

	   }

	 if(mresults.indexOf("元零")==0 )
	     mresults=mresults.substring(2);

	 return mresults;
}
function restoreMoney(inStr)
{
	var outStr="";
	var ch;

	for(i=0;i<inStr.length;i++)
	{
		ch = inStr.charAt(i);
		if(ch!=',')
		{
			outStr += ch;
		}
		else {
			continue;
		}
	}
	return outStr;
}