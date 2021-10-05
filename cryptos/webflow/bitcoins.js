const Webflow = require('webflow-api');

const api = new Webflow({token: '50d90d36dde7ec35a20b58519c3c326e4ab35ce3e456afcdbbf9704fd3f7d009'});

const sites = api.domains({ siteId: '604c20ea813f94deaf58b0c5' });

sites.then(d => console.log(d));