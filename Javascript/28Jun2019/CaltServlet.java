package lab.web.controller;

	import java.awt.print.Printable;
	import java.io.IOException;
	import java.io.PrintWriter;
	 
	import javax.servlet.ServletException;
	import javax.servlet.annotation.WebServlet;
	import javax.servlet.http.HttpServlet;
	import javax.servlet.http.HttpServletRequest;
	import javax.servlet.http.HttpServletResponse;
	 

	@WebServlet("/calt")
	public class CaltServlet extends HttpServlet {
	    private static final long serialVersionUID = 1L;
	 
	    public CaltServlet() {
	        super();

	    }
	 
	 
	    
	   
	 
	 
	    protected void doPost(HttpServletRequest request, HttpServletResponse response)
	            throws ServletException, IOException {
	        int num1, num2;
	        int result;
	        String ms;
	 
	        response.setContentType("text/html; charset=euc-kr");
	 
	        PrintWriter out = response.getWriter();
	 
	        num1 = Integer.parseInt(request.getParameter("num1"));
	        num2 = Integer.parseInt(request.getParameter("num2"));
	        ms = request.getParameter("mathsign");
	        
	 
	        result = calt(num1, num2, ms);
	 
	 
	        out.println("<html>");
	        out.println("<head><title>계산기</title></head>");
	        out.println("<body><center>");
	        out.println("<h2>계산 결과</h2>");
	     
	        out.println(num1 + ms + num2 + " = " + result);
	        out.println("</body></html>");
	    }
	 
	    public int calt(int num1, int num2, String ms) {
	        int result = 0;
	        if (ms.equals("+")) {
	            result = num1 + num2;
	        } else if (ms.equals("-")) {
	            result = num1 - num2;
	        } else if (ms.equals("*")) {
	            result = num1 * num2;
	        } else if (ms.equals("/")) {
	            result = num1 / num2;
	        }
	        return result;
	    }
	 
	}