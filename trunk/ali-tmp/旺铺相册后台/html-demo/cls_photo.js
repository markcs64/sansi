/* ’’∆¨ */

function WP_Photo(p) {
	this.id = p.id || "";
	this.title = p.title || "";
	this.src = p.src || "";
	this.datetime = p.datetime || new Date();
	this.desc = p.desc || "";

	WP_photo.items.push(this);
}

WP_photo.prototype = {
	
};

WP_photo.items = [];
