if(typeof nclk=="undefined"){nclk={}
}if(typeof nclkMaxDepth=="undefined"){var nclkMaxDepth=8
}if(typeof ccsrv=="undefined"){var ccsrv="cc.naver.com"
}if(typeof nclkModule=="undefined"){var nclkModule="cc"
}if(typeof nsc=="undefined"){var nsc="decide.me"
}if(typeof g_pid=="undefined"){var g_pid=""
}if(typeof g_sid=="undefined"){var g_sid=""
}var nclkImg=[];
if(typeof nclkMaxEvtTarget=="undefined"){var nclkMaxEvtTarget=4
}if(typeof nclk_evt=="undefined"){var nclk_evt=0
}nclk.nclktagVersion="1.0.9";
nclk.addEvent=function(e,b,a){if(e.addEventListener){e.addEventListener(b,a,false)
}else{if(e.attachEvent){e["e"+b+a]=a;
e[b+a]=function(){e["e"+b+a](window.event)
};
e.attachEvent("on"+b,e[b+a])
}}};
nclk.generateCC=function(l){var r=l||window.event;
if(!r){return false
}var f=r.target||r.srcElement;
var o=f.nodeName;
var m,p;
var q;
var b="",t="",k="",g="";
var a=0,n=0;
var h,s;
var i;
var j=-1;
if(r.button==2){return
}if(f.nodeType==3){f=f.parentNode
}if(f.parentNode&&f.parentNode.nodeName=="A"){f=f.parentNode
}p=f;
while(j<=nclkMaxEvtTarget){if(j>=nclkMaxEvtTarget){if(nclk_evt==2||nclk_evt==4){h=0;
m=p;
break
}else{return
}}else{i=nclk.getTag(f);
h=i[0];
s=i[1];
if(h==0){if(f.parentNode){f=f.parentNode;
j++
}else{h=0;
m=p;
break
}}else{m=f;
break
}}}switch(h){case 0:case 1:case 2:case 3:if(nclk_evt==2||nclk_evt==4){b="ncs.blank"
}else{return
}break;
case 4:b=nclk.findArea(m,1);
if(b==undefined){b=""
}q=nclk.parseNCStr(h,s);
b=b+"."+q[0];
break;
case 5:b=nclk.findArea(m,2);
if(b==undefined){b=""
}q=nclk.parseNCStr(h,s);
break;
case 6:q=nclk.parseNCStr(h,s);
b=q[0];
break;
default:return
}if(h==4||h==5||h==6){k=q[1];
t=q[2];
g=q[3];
n=q[4]
}if(n=="2"){return
}else{a=n
}if(g){clickcr(m,b,t,k,r,a,g)
}else{clickcr(m,b,t,k,r,a)
}};
nclk.searchNextObj=function(a){var b=a.nextSibling;
if(b&&b.nodeType==3){b=b.nextSibling
}return b
};
nclk.getTag=function(g){var b=0;
if(!g){return 0
}var i;
var f;
var h;
var a="";
if(nclk_evt==1||nclk_evt==2){var e=nclk.searchNextObj(g);
if(e){if(e!=null&&e.nodeType==8&&e.data.indexOf("=")>0){a=nclk.trim(e.data)
}else{return[0,""]
}}else{return[0,""]
}}else{if(nclk_evt==3||nclk_evt==4){if(g.className){a=nclk.getClassTag(g.className);
if(!a){return[0,""]
}}else{return[0,""]
}}}a=nclk.trim(a);
i=a.split("=");
f=i[0].charAt(0);
h=i[0].substring(1);
if(f!="N"){return[0,""]
}if(h=="E"){b=1
}else{if(h=="I"){b=2
}else{if(h=="EI"||h=="IE"){b=3
}else{if(h=="IP"||h=="PI"){b=4
}else{if(h=="P"){b=5
}else{if(i[0].length==1){b=6
}else{b=0
}}}}}}return[b,a]
};
nclk.findArea=function(b,h){var j=0;
var g;
var k;
var m,f;
var e="";
var a=0;
var l;
var i;
if(!b){return
}if(h==1){a=1
}else{if(h==2){a=0
}}while(b=b.parentNode){g=b;
while(1){if(nclk_evt==1||nclk_evt==2){g=g.previousSibling;
if(g){if(g.nodeType==8){k=nclk.trim(g.data)
}else{continue
}}else{break
}}else{if(nclk_evt==3||nclk_evt==4){k=b.className;
if(k){k=nclk.getClassTag(k)
}else{break
}}}if(k.indexOf("=")>0){m=k.split("=");
if(m[0].charAt(0)!="N"){continue
}i=m[0].substring(1);
if(i=="I"&&a==0){f=m[1].split(":");
if(f[0]=="a"){if(f[1]!=""&&f[1]!=undefined){e=f[1]
}}a++;
break
}else{if(i=="E"&&a==1){if(a==1){f=m[1].split(":");
if(f[0]=="a"){if(e==""){e=f[1]
}else{e=((f[1]==undefined)?"":f[1])+"."+e
}}}a++;
break
}else{if((i=="EI"||i=="IE")&&a==0){f=m[1].split(":");
if(f[0]=="a"){e=f[1]
}a+=2;
break
}}}}if(nclk_evt==3||nclk_evt==4){break
}}j++;
if(a>=2){l=e;
break
}if(j>=nclkMaxDepth){l="";
break
}}return l
};
nclk.getServiceType=function(){var a;
if(typeof g_ssc!="undefined"&&typeof g_query!="undefined"){a=1
}else{a=0
}return a
};
nclk.parseNCStr=function(h,o){var a;
var m;
var l;
var e;
var b="",k="",p="",f="",n=0;
var g=2;
o=nclk.trim(o);
switch(h){case 4:g=4;
break;
case 5:g=3;
break;
case 6:g=2;
break;
case 1:case 2:case 3:default:return
}m=o.substring(g);
l=m.split(",");
for(var j=0;
j<l.length;
j++){e=l[j].split(":");
if(e[0]=="a"){b=e[1]
}else{if(e[0]=="r"){k=e[1]
}else{if(e[0]=="i"){p=e[1]
}else{if(e[0]=="g"){f=e[1]
}else{if(e[0]=="t"){n=e[1]
}}}}}}return[b,k,p,f,n]
};
nclk.trim=function(a){return a.replace(/^\s\s*/,"").replace(/\s\s*$/,"")
};
nclk.getClassTag=function(g){var f="";
if(typeof(g)=="string"){f=g
}else{if(g.baseVal){f=g.baseVal
}else{f=""+g
}}var b=new RegExp("N[^=]*=([^ $]*)");
var e=f.match(b);
var a="";
if(e){a=e[0]
}return a
};
function nclk_do(){if(nclk_evt==1||nclk_evt==2||nclk_evt==3||nclk_evt==4){nclk.addEvent(document,"click",nclk.generateCC)
}}nclk.getScrollBarWidth=function(){var e=document.createElement("p");
e.style.width="200px";
e.style.height="200px";
var f=document.createElement("div");
f.style.position="absolute";
f.style.top="0px";
f.style.left="0px";
f.style.visibility="hidden";
f.style.width="200px";
f.style.height="150px";
f.style.overflow="hidden";
f.appendChild(e);
document.body.appendChild(f);
var b=e.offsetWidth;
f.style.overflow="scroll";
var a=e.offsetWidth;
if(b==a){a=f.clientWidth
}document.body.removeChild(f);
return(b-a)
};
nclk.findPos=function(b){var f=curtop=0;
try{if(b.offsetParent){do{f+=b.offsetLeft;
curtop+=b.offsetTop
}while(b=b.offsetParent)
}else{if(b.x||b.y){if(b.x){f+=b.x
}if(b.y){curtop+=b.y
}}}}catch(a){}return[f,curtop]
};
nclk.windowSize=function(e){if(!e){e=window
}var a=0;
if(e.innerWidth){a=e.innerWidth;
if(typeof(e.innerWidth)=="number"){var b=nclk.getScrollBarWidth();
a=e.innerWidth-b
}}else{if(document.documentElement&&document.documentElement.clientWidth){a=document.documentElement.clientWidth
}else{if(document.body&&(document.body.clientWidth||document.body.clientHeight)){a=document.body.clientWidth
}}}return a
};
nclk.checkIframe=function(i){var f=document.URL;
var h=i.parentNode;
var a;
var b;
if(h==null||h==undefined){return false
}while(1){if(h.nodeName.toLowerCase()=="#document"){if(h.parentWindow){a=h.parentWindow
}else{a=h.defaultView
}try{if(a.frameElement!=null&&a.frameElement!=undefined){if(a.frameElement.nodeName.toLowerCase()=="iframe"){b=a.frameElement.id;
if(!b){return false
}return b
}else{return false
}}else{return false
}}catch(g){return false
}}else{h=h.parentNode;
if(h==null||h==undefined){return false
}}}};
nclk.absPath=function(a){var e=window.location;
var f=e.href;
var b=e.protocol+"//"+e.host;
if(a.charAt(0)=="/"){if(a.charAt(1)=="/"){return e.protocol+a
}else{return b+a
}}if(/^\.\//.test(a)){a=a.substring(2)
}while(/^\.\./.test(a)){if(b!=f){f=f.substring(0,f.lastIndexOf("/"))
}a=a.substring(3)
}if(b!=f){if(a.charAt(0)!="?"&&a.charAt(0)!="#"){f=f.substring(0,f.lastIndexOf("/"))
}}if(a.charAt(0)=="/"){return f+a
}else{if(a.charAt(0)=="?"){f=f.split("?")[0];
return f+a
}else{if(a.charAt(0)=="#"){f=f.split("#")[0];
return f+a
}else{return f+"/"+a
}}}};
function clickcr(g,I,u,E,F,B,z){if(arguments.length==1){if(typeof nclk.generateCC!="undefined"){nclk.generateCC(arguments[0])
}return
}var G=navigator.userAgent.toLowerCase();
var k=(G.indexOf("safari")!=-1?true:false);
var D=/msie/.test(G)&&!/opera/.test(G);
var l=(window.location.protocol=="https:")?"https:":"http:";
var a=ccsrv.substring(ccsrv.indexOf(".")+1);
var t=window.event?window.event:F;
var s=-1;
var q=-1;
var p=-1;
var n=-1;
var S,f,i;
var r,j,m;
var N,K,J,M,A,C,w;
var P;
var H=0;
if(!B){B="0"
}else{B=String(B)
}if(!z){z=""
}if(B.indexOf("n")==0){H=0
}else{if(window.g_ssc!=undefined&&window.g_query!=undefined){H=1
}else{H=0
}}try{M=nclk.windowSize(window);
i=nclk.checkIframe(g);
if(i){var v=nclk.findPos(document.getElementById(i));
if(t.clientX&&t.clientX!=undefined){S=document.body;
if(S.clientLeft&&S.clientTop){ifrSx=t.clientX-S.clientLeft;
ifrSy=t.clientY-S.clientTop
}else{ifrSx=t.clientX;
ifrSy=t.clientY
}}p=v[0]+ifrSx;
n=v[1]+ifrSy;
if(document.body&&(document.body.scrollTop||document.body.scrollLeft)){S=document.body;
s=p-S.scrollLeft;
q=n-S.scrollTop
}else{if(document.documentElement&&(document.documentElement.scrollTop||document.documentElement.scrollLeft)){f=document.documentElement;
s=p-f.scrollLeft;
q=n-f.scrollTop
}else{s=p;
q=n
}}}else{if(t.clientX&&t.clientX!=undefined){S=document.body;
if(S.clientLeft&&S.clientTop){s=t.clientX-S.clientLeft;
q=t.clientY-S.clientTop
}else{s=t.clientX;
q=t.clientY
}}if(document.body&&(document.body.scrollTop||document.body.scrollLeft)){p=document.body.scrollLeft+(s<0?0:s);
n=document.body.scrollTop+(q<0?0:q)
}else{if(document.documentElement&&(document.documentElement.scrollTop||document.documentElement.scrollLeft)){f=document.documentElement;
if(f.scrollLeft!=undefined){p=f.scrollLeft+(s<0?0:s)
}if(f.scrollTop!=undefined){n=f.scrollTop+(q<0?0:q)
}}else{p=(s<0?0:s);
n=(q<0?0:q)
}}if(t.pageX){p=t.pageX
}if(t.pageY){n=t.pageY
}}}catch(Q){}if(I==""||typeof I=="undefined"){return
}if(B.indexOf("1")!=-1){r=0
}else{if(g.href){A=g.nodeName.toLowerCase();
C=g.href.toLowerCase();
if((g.target&&g.target!="_self"&&g.target!="_top"&&g.target!="_parent")||(C.indexOf("javascript:")!=-1)||(g.getAttribute("href",2)&&g.getAttribute("href",2).charAt(0)=="#")||(C.indexOf("#")!=-1&&(C.substr(0,C.indexOf("#"))==document.URL))||A.toLowerCase()=="img"||D&&window.location.host.indexOf(a)==-1){r=0
}else{r=1
}}else{r=0
}}if(g.href&&g.href.indexOf(l+"//"+ccsrv)==0){j=g.href
}else{j=l+"//"+ccsrv+"/"+nclkModule+"?a="+I+"&r="+E+"&i="+u;
j+="&bw="+M+"&px="+p+"&py="+n+"&sx="+s+"&sy="+q+"&m="+r;
if(H==0){j+="&nsc="+nsc
}else{if(H==1){j+="&ssc="+g_ssc+"&q="+encodeURIComponent(g_query)+"&s="+g_sid+"&p="+g_pid+"&g="+z
}}if(C&&C.indexOf(l+"//"+ccsrv)!=0&&A.toLowerCase()!="img"){var O=g.href;
if(g.outerHTML&&!window.XMLHttpRequest){O=(/\shref=\"([^\"]+)\"/i.test(g.outerHTML)&&RegExp.$1).replace(/\\/g,"\\\\").replace(/%([A-Z0-9]{2})/ig,"\\$1");
(d=document.createElement("div")).innerHTML=O;
O=d.innerText.replace(/\\([A-Z0-9]{2})/gi,"%$1").replace(/\\\\/g,"\\")
}C=O.toLowerCase();
if(C.indexOf("http:")==0||C.indexOf("https:")==0||C.indexOf("javascript:")==0){j+="&u="+encodeURIComponent(O)
}else{w=nclk.absPath(O);
j+="&u="+encodeURIComponent(w)
}}else{if(g.href){if(g.href.length>0){j+="&u="+encodeURIComponent(g.href)
}else{j+="&u=about%3Ablank"
}}else{j+="&u=about%3Ablank"
}}}if(r==1){P=g.innerHTML;
g.href=j;
if(g.innerHTML!=P){g.innerHTML=P
}}else{if(document.images){var L=new Date().getTime();
j+="&time="+L;
if(k&&!g.href){var R=c=new Date();
while((R.getTime()-c.getTime())<100){R=new Date()
}var N=new Image();
nclkImg.push(N);
N.src=j
}else{var N=new Image();
nclkImg.push(N);
N.src=j
}}}return true
}(function(exportTarget){var lcs_options={nnb:true};
var lcs_version="v0.7.0";
var lcs_add={};
var lcs_bc={};
var lcs_perf={};
var lcs_do_count=0;
var lcs_waiting_pageshow=false;
function lcs_do(etc){if(lcs_waiting_pageshow){return
}if(document.readyState!=="complete"){var eventName="onpageshow" in window?"pageshow":"load";
var retry=function(__etc){return function(){window.setTimeout(function(){lcs_waiting_pageshow=false;
lcs_do(__etc)
},10)
}
}(etc);
if(document.addEventListener){window.addEventListener(eventName,retry,false)
}else{window.attachEvent("on"+eventName,retry)
}lcs_waiting_pageshow=true;
return
}if(!window.lcs_SerName){window.lcs_SerName="lcs.naver.com"
}var rs="";
var index;
var itarVal;
var doc=document;
var wlt=window.location;
var lcsServerAddr;
try{lcsServerAddr=(wlt.protocol?wlt.protocol:"http:")+"//"+window.lcs_SerName+"/m?"
}catch(e){return
}try{rs=lcsServerAddr+"u="+encodeURIComponent(wlt.href)+"&e="+(doc.referrer?encodeURIComponent(doc.referrer):"")
}catch(e){}try{if(typeof lcs_add.i=="undefined"){lcs_add.i=""
}if(lcs_do_count<1){lcs_setBrowserCapa();
if(lcs_options.nnb){lcs_setNNB()
}lcs_add.ct=lcs_getConnectType();
lcs_setNavigationTiming();
lcs_setPaintTiming();
lcs_setNavigationType()
}for(index in lcs_bc){if(typeof lcs_bc[index]!=="function"){rs+="&"+index+"="+encodeURIComponent(lcs_bc[index])
}}for(index in lcs_add){itarVal=lcs_add[index];
if(itarVal!==undefined&&typeof itarVal!=="function"){rs+="&"+index+"="+encodeURIComponent(itarVal)
}}if(lcs_do_count<1){for(index in lcs_perf){itarVal=lcs_perf[index];
if(itarVal){rs+="&"+index+"="+encodeURIComponent(itarVal)
}}}for(index in etc){if((index.length>=3&&typeof etc[index]!=="function")||index==="qy"){rs+="&"+index+"="+encodeURIComponent(etc[index])
}}if(!!etc===false||!!etc.pid===false){var pidFallback;
if(window.g_pid){pidFallback=g_pid
}else{pidFallback=lcs_get_lpid()
}rs+="&pid="+encodeURIComponent(pidFallback)
}var timeStr=new Date().getTime();
rs+="&ts="+timeStr;
rs+="&EOU";
var obj=document.createElement("img");
obj.src=rs;
obj.onload=function(){obj.onload=null;
return
};
lcs_do_count++
}catch(e){return
}}function lcs_do_gdid(gdid,etc){try{if(gdid){lcs_add.i=gdid;
if(etc){lcs_do(etc)
}else{lcs_do()
}}}catch(e){}}function lcs_setNNB(){try{var lsg=localStorage;
if(lsg){if(lsg.ls){var lc=lsg.ls;
if(lc.length==13){lcs_add.ls=lc;
return
}}var nnb=lcs_getNNBfromCookie();
if(nnb!=null&&nnb!=""){lsg.ls=nnb;
lcs_add.ls=nnb
}}}catch(e){}}function lcs_setBrowserCapa(){lcs_bc.os=lcs_getOS();
lcs_bc.ln=lcs_getlanguage();
lcs_bc.sr=lcs_getScreen();
lcs_bc.pr=window.devicePixelRatio||1;
var windowSize=lcs_getWindowSize();
lcs_bc.bw=windowSize.bw;
lcs_bc.bh=windowSize.bh;
lcs_bc.c=lcs_getColorDepth();
lcs_bc.j=lcs_getJavaEnabled();
lcs_bc.k=lcs_getCookieEnabled()
}function lcs_getOS(){var lcs_os="";
try{navigator.platform?(lcs_os=navigator.platform):""
}catch(e){}return lcs_os
}function lcs_getlanguage(){var lcs_ln="";
try{navigator.userLanguage?(lcs_ln=navigator.userLanguage):navigator.language?(lcs_ln=navigator.language):""
}catch(e){}return lcs_ln
}function lcs_getScreen(){var lcs_sr="";
try{if(window.screen&&screen.width&&screen.height){lcs_sr=screen.width+"x"+screen.height
}else{if(window.java||self.java){var sr=java.awt.Toolkit.getDefaultToolkit().getScreenSize();
lcs_sr=sr.width+"x"+sr.height
}}}catch(e){lcs_sr=""
}return lcs_sr
}function lcs_getWindowSize(){var doc=document;
var size={bw:"",bh:""};
try{size.bw=doc.documentElement.clientWidth?doc.documentElement.clientWidth:doc.body.clientWidth;
size.bh=doc.documentElement.clientHeight?doc.documentElement.clientHeight:doc.body.clientHeight
}catch(e){}return size
}function lcs_getColorDepth(){var colorDepth="";
try{if(window.screen){colorDepth=screen.colorDepth?screen.colorDepth:screen.pixelDepth
}else{if(window.java||self.java){var c=java.awt.Toolkit.getDefaultToolkit().getColorModel().getPixelSize();
colorDepth=c
}}}catch(e){colorDepth=""
}return colorDepth
}function lcs_getJavaEnabled(){var jsEnable="";
try{jsEnable=navigator.javaEnabled()?"Y":"N"
}catch(e){}return jsEnable
}function lcs_getCookieEnabled(){var cookieEnable="";
try{cookieEnable=navigator.cookieEnabled?"Y":"N"
}catch(e){}return cookieEnable
}function lcs_getNNBfromCookie(){try{var ck=document.cookie;
var k,v,i,ArrCookies=ck.split(";");
for(i=0;
i<ArrCookies.length;
i++){k=ArrCookies[i].substr(0,ArrCookies[i].indexOf("="));
v=ArrCookies[i].substr(ArrCookies[i].indexOf("=")+1);
k=k.replace(/^\s+|\s+$/g,"");
if(k=="NNB"){return unescape(v)
}}}catch(e){}}function lcs_getConnectType(){var ct="";
try{var conn=navigator.connection||navigator.mozConnection||navigator.webkitConnection;
if(conn&&typeof conn.type!="undefined"){switch(conn.type){case conn.CELL_2G:ct="2g";
break;
case conn.CELL_3G:ct="3g";
break;
case conn.CELL_4G:ct="4g";
break;
case conn.WIFI:ct="wifi";
break;
case conn.ETHERNET:ct="eth";
break;
case conn.UNKNOWN:ct="unknown";
break;
case conn.NONE:ct="none";
break;
default:ct=""
}}else{if(typeof blackberry!="undefined"&&typeof blackberry.network!="undefined"){var bnet=blackberry.network;
if(bnet=="Wi-Fi"){ct="wifi"
}else{if(bnet=="3G"){ct="3g"
}else{ct=bnet
}}}else{var lcs_isie=navigator.appName=="Microsoft Internet Explorer";
var lcs_ismac=navigator.userAgent.indexOf("MAC")>=0;
if(lcs_isie&&!lcs_ismac&&bd&&bd.addBehavior){var bd=document.body;
var lcs_ct="";
var obj=bd.addBehavior("#default#clientCaps");
ct=bd.connectionType;
bd.removeBehavior(obj)
}}}}catch(e){console.warn(e)
}return ct
}function lcs_setNavigationTiming(){var performance=window.performance||{};
if(performance.timing){var pt=performance.timing;
for(var key in pt){var value=pt[key];
if(typeof value==="number"){lcs_perf[key]=value
}}}}function lcs_setPaintTiming(){var performance=window.performance||{};
try{if(performance.getEntriesByType){var performanceEntries=performance.getEntriesByType("paint");
performanceEntries.forEach(function(performanceEntry,i,entries){var name=performanceEntry.name;
switch(name){case"first-paint":case"first-contentful-paint":lcs_perf[name]=performanceEntry.startTime;
break;
default:break
}})
}else{}}catch(e){console.warn(e)
}}function lcs_setNavigationType(){var ngt=getNavigationType();
if(ngt!==undefined){lcs_perf.ngt=ngt
}}function getNavigationType(){var performance=window.performance||{};
if(performance.navigation){return performance.navigation.type
}return
}var lpid=null;
function lcs_create_lpid(){var uaID;
var nnb=localStorage.ls;
if(nnb){uaID=nnb
}else{var nnbFallback;
nnbFallback=navigator.userAgent+Math.random();
uaID=nnbFallback
}var performance=window.performance||{};
var pageURL=location.href;
var currentTime;
if(performance.now){currentTime=performance.now()
}else{currentTime=new Date().getTime()
}lpid=hashFunction.md5(uaID+pageURL+currentTime);
return lpid
}function lcs_get_lpid(){if(lpid===null){lpid=lcs_create_lpid()
}return lpid
}function lcs_update_lpid(){lpid=lcs_create_lpid();
return lpid
}var hashFunction={};
(function(exportTarget){function safeAdd(x,y){var lsw=(x&65535)+(y&65535);
var msw=(x>>16)+(y>>16)+(lsw>>16);
return(msw<<16)|(lsw&65535)
}function bitRotateLeft(num,cnt){return(num<<cnt)|(num>>>(32-cnt))
}function md5cmn(q,a,b,x,s,t){return safeAdd(bitRotateLeft(safeAdd(safeAdd(a,q),safeAdd(x,t)),s),b)
}function md5ff(a,b,c,d,x,s,t){return md5cmn((b&c)|(~b&d),a,b,x,s,t)
}function md5gg(a,b,c,d,x,s,t){return md5cmn((b&d)|(c&~d),a,b,x,s,t)
}function md5hh(a,b,c,d,x,s,t){return md5cmn(b^c^d,a,b,x,s,t)
}function md5ii(a,b,c,d,x,s,t){return md5cmn(c^(b|~d),a,b,x,s,t)
}function binlMD5(x,len){x[len>>5]|=128<<len%32;
x[(((len+64)>>>9)<<4)+14]=len;
var i;
var olda;
var oldb;
var oldc;
var oldd;
var a=1732584193;
var b=-271733879;
var c=-1732584194;
var d=271733878;
for(i=0;
i<x.length;
i+=16){olda=a;
oldb=b;
oldc=c;
oldd=d;
a=md5ff(a,b,c,d,x[i],7,-680876936);
d=md5ff(d,a,b,c,x[i+1],12,-389564586);
c=md5ff(c,d,a,b,x[i+2],17,606105819);
b=md5ff(b,c,d,a,x[i+3],22,-1044525330);
a=md5ff(a,b,c,d,x[i+4],7,-176418897);
d=md5ff(d,a,b,c,x[i+5],12,1200080426);
c=md5ff(c,d,a,b,x[i+6],17,-1473231341);
b=md5ff(b,c,d,a,x[i+7],22,-45705983);
a=md5ff(a,b,c,d,x[i+8],7,1770035416);
d=md5ff(d,a,b,c,x[i+9],12,-1958414417);
c=md5ff(c,d,a,b,x[i+10],17,-42063);
b=md5ff(b,c,d,a,x[i+11],22,-1990404162);
a=md5ff(a,b,c,d,x[i+12],7,1804603682);
d=md5ff(d,a,b,c,x[i+13],12,-40341101);
c=md5ff(c,d,a,b,x[i+14],17,-1502002290);
b=md5ff(b,c,d,a,x[i+15],22,1236535329);
a=md5gg(a,b,c,d,x[i+1],5,-165796510);
d=md5gg(d,a,b,c,x[i+6],9,-1069501632);
c=md5gg(c,d,a,b,x[i+11],14,643717713);
b=md5gg(b,c,d,a,x[i],20,-373897302);
a=md5gg(a,b,c,d,x[i+5],5,-701558691);
d=md5gg(d,a,b,c,x[i+10],9,38016083);
c=md5gg(c,d,a,b,x[i+15],14,-660478335);
b=md5gg(b,c,d,a,x[i+4],20,-405537848);
a=md5gg(a,b,c,d,x[i+9],5,568446438);
d=md5gg(d,a,b,c,x[i+14],9,-1019803690);
c=md5gg(c,d,a,b,x[i+3],14,-187363961);
b=md5gg(b,c,d,a,x[i+8],20,1163531501);
a=md5gg(a,b,c,d,x[i+13],5,-1444681467);
d=md5gg(d,a,b,c,x[i+2],9,-51403784);
c=md5gg(c,d,a,b,x[i+7],14,1735328473);
b=md5gg(b,c,d,a,x[i+12],20,-1926607734);
a=md5hh(a,b,c,d,x[i+5],4,-378558);
d=md5hh(d,a,b,c,x[i+8],11,-2022574463);
c=md5hh(c,d,a,b,x[i+11],16,1839030562);
b=md5hh(b,c,d,a,x[i+14],23,-35309556);
a=md5hh(a,b,c,d,x[i+1],4,-1530992060);
d=md5hh(d,a,b,c,x[i+4],11,1272893353);
c=md5hh(c,d,a,b,x[i+7],16,-155497632);
b=md5hh(b,c,d,a,x[i+10],23,-1094730640);
a=md5hh(a,b,c,d,x[i+13],4,681279174);
d=md5hh(d,a,b,c,x[i],11,-358537222);
c=md5hh(c,d,a,b,x[i+3],16,-722521979);
b=md5hh(b,c,d,a,x[i+6],23,76029189);
a=md5hh(a,b,c,d,x[i+9],4,-640364487);
d=md5hh(d,a,b,c,x[i+12],11,-421815835);
c=md5hh(c,d,a,b,x[i+15],16,530742520);
b=md5hh(b,c,d,a,x[i+2],23,-995338651);
a=md5ii(a,b,c,d,x[i],6,-198630844);
d=md5ii(d,a,b,c,x[i+7],10,1126891415);
c=md5ii(c,d,a,b,x[i+14],15,-1416354905);
b=md5ii(b,c,d,a,x[i+5],21,-57434055);
a=md5ii(a,b,c,d,x[i+12],6,1700485571);
d=md5ii(d,a,b,c,x[i+3],10,-1894986606);
c=md5ii(c,d,a,b,x[i+10],15,-1051523);
b=md5ii(b,c,d,a,x[i+1],21,-2054922799);
a=md5ii(a,b,c,d,x[i+8],6,1873313359);
d=md5ii(d,a,b,c,x[i+15],10,-30611744);
c=md5ii(c,d,a,b,x[i+6],15,-1560198380);
b=md5ii(b,c,d,a,x[i+13],21,1309151649);
a=md5ii(a,b,c,d,x[i+4],6,-145523070);
d=md5ii(d,a,b,c,x[i+11],10,-1120210379);
c=md5ii(c,d,a,b,x[i+2],15,718787259);
b=md5ii(b,c,d,a,x[i+9],21,-343485551);
a=safeAdd(a,olda);
b=safeAdd(b,oldb);
c=safeAdd(c,oldc);
d=safeAdd(d,oldd)
}return[a,b,c,d]
}function binl2rstr(input){var i;
var output="";
var length32=input.length*32;
for(i=0;
i<length32;
i+=8){output+=String.fromCharCode((input[i>>5]>>>i%32)&255)
}return output
}function rstr2binl(input){var i;
var output=[];
output[(input.length>>2)-1]=undefined;
for(i=0;
i<output.length;
i+=1){output[i]=0
}var length8=input.length*8;
for(i=0;
i<length8;
i+=8){output[i>>5]|=(input.charCodeAt(i/8)&255)<<i%32
}return output
}function rstrMD5(s){return binl2rstr(binlMD5(rstr2binl(s),s.length*8))
}function rstrHMACMD5(key,data){var i;
var bkey=rstr2binl(key);
var ipad=[];
var opad=[];
var hash;
ipad[15]=opad[15]=undefined;
if(bkey.length>16){bkey=binlMD5(bkey,key.length*8)
}for(i=0;
i<16;
i+=1){ipad[i]=bkey[i]^909522486;
opad[i]=bkey[i]^1549556828
}hash=binlMD5(ipad.concat(rstr2binl(data)),512+data.length*8);
return binl2rstr(binlMD5(opad.concat(hash),512+128))
}function rstr2hex(input){var hexTab="0123456789abcdef";
var output="";
var x;
var i;
for(i=0;
i<input.length;
i+=1){x=input.charCodeAt(i);
output+=hexTab.charAt((x>>>4)&15)+hexTab.charAt(x&15)
}return output
}function str2rstrUTF8(input){return unescape(encodeURIComponent(input))
}function rawMD5(s){return rstrMD5(str2rstrUTF8(s))
}function hexMD5(s){return rstr2hex(rawMD5(s))
}function rawHMACMD5(k,d){return rstrHMACMD5(str2rstrUTF8(k),str2rstrUTF8(d))
}function hexHMACMD5(k,d){return rstr2hex(rawHMACMD5(k,d))
}function md5(string,key,raw){if(!key){if(!raw){return hexMD5(string)
}return rawMD5(string)
}if(!raw){return hexHMACMD5(key,string)
}return rawHMACMD5(key,string)
}exportTarget.md5=md5
})(hashFunction);
exportTarget.lcs_do=lcs_do;
exportTarget.lcs_do_gdid=lcs_do_gdid;
exportTarget.lcs_get_lpid=lcs_get_lpid;
exportTarget.lcs_update_lpid=lcs_update_lpid;
exportTarget.lcs_version=lcs_version
})(window);