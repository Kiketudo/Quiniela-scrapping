const fs = require('fs');
const { Client, LocalAuth } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');

// Use the saved values
const client = new Client({
    authStrategy: new LocalAuth()
});
/*client.on('qr', qr => {
    qrcode.generate(qr, {small: true});
});*/

client.on('ready', () => {
    console.log('Client is ready!');
});

client.initialize();
 
// Save session values to the file upon successful auth
client.on('message', message => {
	if(message.body === '!ping') {
		client.sendMessage(message.from, lista);
	}
});/*
client.isRegisteredUser("34692265512@c.us").then(function(isRegistered) {
    if(isRegistered) {
        client.sendMessage("34692265512@c.us", "hello");
    }
})
/*var array=[{title:'sectionTitle',rows:[{id:'customId', title:'ListItem2', description: 'desc'},{id:'ID1', title:'ListItem2'}]}]
var lista = new List("texto cuerpo","texto buton",array);*/