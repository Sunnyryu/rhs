package lab.web.controller;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;


@WebServlet("/Join")
public class JoinServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;


    public JoinServlet() {
        super();

    }

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		  out.print("<html>");
	        out.print("<head><title>Request로 파라미터 처리</title></head>");
	        out.print("<body>");
	        out.print("<h3>Request로 파라미터 처리</h3>");
	        out.print("<ul>");

	        out.print("<li> userid:" + request.getParameter("userid")+"</li>");
	        out.print("<li> password :" + request.getParameter("userpwd")+"</li>");
	        out.print("<li> address :" + request.getParameter("address")+"</li>");
	        String interest[] = request.getParameterValues("interest");
	        out.print("<li> 관심사항:");
	        for(String inter : interest) {
	        	out.print(inter +",");
	        }
	        out.println("</li>");
	        out.print("</body></html>");

	}
}
