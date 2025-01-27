/**
 * util.js
 */

function centroid (points){
	
	var i, j, len, p1, p2, f, area, x, y;
	
	area = x = y = 0;
	
	for(i = 0, len = points.length, j = len -1; i < len; j= i++){
		p1 = points[i];
		p2 = points[j];
		
		f = p1.y * p2.x - p2.y * p1.x;
		x += (p1.x + p2.x) * f;
		y += (p1.y + p2.y) * f;
		area += f * 3;
		
		
	}
	
	return new kakao.maps.LatLng(x / area, y / area);
}


HashMap = function(){
	this.map = new Array();
}

HashMap.prototype = {
	put: function(key, value){
		this.map[key] = value;
	},
	get: function(key){
		return this.map[key];
	},
	length: function(){
		return Object.keys(this.map).length
	},
	keys: function(){
		return Object.keys(this.map)
	}
}
