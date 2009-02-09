// 动画演示
package {
	import flash.display.Bitmap;
	import flash.display.DisplayObject;
	import flash.display.Sprite;
	import flash.display.Stage;
	import flash.geom.Point;
	import flash.utils.clearTimeout;
	import flash.utils.setTimeout;
	
	public class animDemo {
		public var couldShow:Boolean = true;
		public var cursor:Sprite = new Sprite();
		public var step:int = 5;	//每次移动的距离
		private var stage:Stage;
		private var su:Object;
		
		public function animDemo(su:Object, cursor:Bitmap) {
			this.cursor.addChild(cursor);
			this.cursor.visible = false;
			
			su.stage.addChild(this.cursor);
			this.stage = su.stage;
			this.su = su;
		}
		
		public function show():void {
			if (!this.couldShow) return;
			
			this.cursor.visible = true;
			//this.cursor.
			
			this.moveTo(480, 320);
		}
		
		public function hide():void {
			this.cursor.visible = false;
		}
		
		private function moveTo(x:int, y:int):void {
			//将鼠标移到位置 x, y
			var x0:int = this.cursor.x;
			var y0:int = this.cursor.y;
			var xm:int = x - x0;
			var ym:int = y - y0;
			
			var d:Number = Math.sqrt(xm * xm + ym * ym);	//距离
			var steps:Number = d / this.step;
			
			var xs:Number = xm / steps;
			var ys:Number = ym / steps;
			
			var ob:Sprite = this.cursor;
			var tmOut:uint;
			var _this:Object = this;
			
			var move:Function = function (x:int, y:int, xs:Number, ys:Number):void {
				if (Math.abs(ob.x - x) < 1 && Math.abs(ob.y - y) < 1) {
					clearTimeout(tmOut);
					_this.hover();
					return;
				}
				//trace(ob.x, ob.y);
				
				if (Math.abs(ob.x - x) < Math.abs(xs))
					xs = 1;
				if (Math.abs(ob.y - y) < Math.abs(ys))
					ys = 1;
				
				ob.x += xs;
				ob.y += ys;
			};
			
			var f:Function = function():void {
				tmOut = setTimeout(f, 30);
				move(x, y, xs, ys);
				if (!_this.couldShow) {
					clearTimeout(tmOut);
				}
			}
			
			f();
		}
		
		private function hover():void {
			//var p:Point = new Point(this.cursor.x, this.cursor.y);
			//var obs:Array = this.stage.getObjectsUnderPoint(p);
			//var prov:DisplayObject = obs[0];
			var sp:Sprite = this.stage.getChildAt(1) as Sprite;
			var prov:DisplayObject = sp.getChildAt(22);
			//trace(obs, prov, sp.getChildAt(3));
			//for (var i:int = 0; i < sp.numChildren; i ++) {
			//	trace(i, sp.getChildAt(i));
			//}
			//trace(sp.numChildren);
			/*var filter:GlowFilter = new GlowFilter();
			filter.color = 0x333333;
			filter.strength = 2;
			prov.filters = [filter];*/
			
			this.su.hover2(prov);
		}
	}
}