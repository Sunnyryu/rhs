package lab.web.controller;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/PostServlet")
public class PostServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
    public PostServlet() {
        super();
    }
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		String msg = request.getParameter("msg");
		request.setAttribute("address", "서울특별시 강남구 역삼동");
		response.sendRedirect("http://www.daum.net");
	}

}
