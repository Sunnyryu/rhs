package lab.web.controller;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/cookieLogin")
public class CookieLoginServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
	String uid = null, passwd = null;
	ServletContext sctx = null;
	RequestDispatcher rd = null;
	
       
    public CookieLoginServlet() {
        super();
    }

	@Override
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		//Get 방식으로 접근하는 경우에 쿠키를 체크합니다.
		Cookie cookies[] = request.getCookies();
		if(cookies != null) {
			for(int i = 0; i < cookies.length; i++) {
				String name = cookies[i].getName();
				if(name.equals("userid")) {
					uid = cookies[i].getValue();
					System.out.println(uid);
					request.setAttribute("userid", uid);
				}
			}
			//request.setAttribute("userid", uid);
		}
		
		sctx = request.getServletContext();
		rd = sctx.getRequestDispatcher("/cookie_login.jsp");
		rd.forward(request, response);
	}

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		uid = request.getParameter("userid");
		passwd = request.getParameter("passwd");
		String useCookie = request.getParameter("cookie");
		
		if(useCookie != null) {
			Cookie uidCookie = new Cookie("userid", uid);
			uidCookie.setMaxAge(60*60*24*365);
			response.addCookie(uidCookie);
		}
		
		if(uid.equals("admin") && passwd.equals("1234")) {
			request.setAttribute("userid", uid);
			sctx = request.getServletContext();
			rd = sctx.getRequestDispatcher("/main.jsp");
			rd.forward(request, response);
		}
		else {
			out.print("<script>");
			out.print("alert(\"아이디 또는 비밀번호 오류입니다.\");");
			out.print("location.href=\"./cookie_login.jsp\";");
			out.print("</script>");
		}
	}

}
