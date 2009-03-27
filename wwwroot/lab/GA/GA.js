/* GA.js
 *
 */

(function () {
	GA = function (params) {
		if (!params) params = {};
		this.xRate = params.xRate || 0.7;
		this.mutationRate = params.mutationRate || 0.005;
		this.generation = 0;
		this.liveCount = params.lives || 50;
		this.geneLength = params.geneLength || 100;
	};

	GA.prototype = {
	};

	GA.Life = function (park, params) {
		this.park = park;
		if (!params) params = {};
		if (typeof(params.gene) == "number") {
			this.gene = this.gene.toString(2);
		} else if (typeof(params.gene) == "string") {
			this.gene = params.gene;
		} else {
		}
	};

	GA.Life.prototype = {
	}
})();
