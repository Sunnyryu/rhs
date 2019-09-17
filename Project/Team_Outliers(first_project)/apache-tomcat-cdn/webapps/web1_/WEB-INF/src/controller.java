package lab.web.controller;

public class HelloServelt extends HttpServlet {
	//overide 하지 않으면 부모의 init() 수행;
	//서블릿이 요청되어서 컨테이너 메모리에 생성될 때 1번 수행
	public void init() { 
		
		system.out.println("init(): 초기화");
		
	}
	
	//서블릿이 요청될 때 마다 반복적으로 수행
	public void service(
			HttpServletRequest req, 
			HttpServletResponse res
	) throws ServletException, IOException {
		
	}
	
	//overide 하지 않으면 부모의 destory() 수행;
	//서블릿이 요청되어서 컨테이너 메모리에 생성될 때 1번 수행
	public void destory() {
		System.out.println("destroy(): 컨테이너 종료 또는 GC 될 때 수행");
	}
}