// ActionScript file
package {
	public class HTML2Content {
		
		public var html:String = "";
		public var content:String = "";
		public var title:String = "";
		public var lines:Array = [];
		
		public function HTML2Content(html:String) {
			this.html = html;
			
			this.getTitle();
		}
		
		private function getTitle():void {
			var t:String = this.html.match(/(?:<title>)(.+?)(?=<\/title>)/i)[0] || "";
			trace(t);
		}
		
		private function split2Lines():void {
			
		}
	}
}