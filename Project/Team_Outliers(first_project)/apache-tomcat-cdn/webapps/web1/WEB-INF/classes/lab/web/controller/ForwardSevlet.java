package lab.web.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/message")
public class ForwardSevlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	ServletContext sctx;
	RequestDispatcher rd;
       
    public ForwardSevlet() {
        super();
    }

	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		sctx = request.getServletContext();
		rd = sctx.getRequestDispatcher("/WEB-INF/view/message.jsp");
		rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		
		//추가 정보를 request에 저장
		request.setAttribute("msg2", "mr.laughaway@gmail.com");
		
		sctx = request.getServletContext();
		rd = sctx.getRequestDispatcher("/WEB-INF/view/result.jsp");
		rd.forward(request, response);
	}

}
