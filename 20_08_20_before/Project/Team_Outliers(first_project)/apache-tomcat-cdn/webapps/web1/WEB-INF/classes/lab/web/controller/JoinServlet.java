package lab.web.controller;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.Enumeration;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/join")
public class JoinServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    public JoinServlet() {
        super();
    }

	@Override
	protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
		// TODO Auto-generated method stub
		super.doGet(req, resp);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		
		out.print("<html>");
		out.print("<head><title>HeaderInfo</title></head>");
		out.print("<body>");
		
		out.print("<h3>Request로 파라미터 처리</h3>");
		out.print("<ul>");
		
		out.print("<li> userid : " + request.getParameter("userid") + "</li>");
		out.print("<li> userpwd : " + request.getParameter("userpwd") + "</li>");
		out.print("<li> address : " + request.getParameter("address") + "</li>");
		String interest[] = request.getParameterValues("interest");
		out.print("<li> 관심사항: ");
		for(String inter : interest) {
			out.print(inter + ", ");
		}
		out.print("</li>");
		out.print("</body></html>");
	}

}
