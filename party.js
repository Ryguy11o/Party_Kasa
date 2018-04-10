const TPLSmartDevice = require('tplink-lightbulb')

const light = new TPLSmartDevice('192.168.0.30')


try {
	partyTime();
} catch(err){

}



async function partyTime(){ 

light.send({
  'smartlife.iot.smartbulb.lightingservice': {
    'transition_light_state': {
      'hue': getRandomInt(360),
      'saturation': 100,
      'transition_period': 0
    }
}});

}
function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

function on_or_off(){ 

if(getRandomInt(20) < 3){
	return 0;
}else{
	return 1;
}

}