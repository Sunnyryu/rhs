package lab.web.controller;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class send
 */
@WebServlet("/send")
public class SendServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	 ServletContext sctx;
	 RequestDispatcher rd;

    public SendServlet() {
        super();

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		request.setAttribute("msg2", "acsryu@live.co.kr");
		sctx = request.getServletContext();
		rd = sctx.getRequestDispatcher("/WEB-INF/view/result.jsp");
		rd.forward(request, response);


    }
}
