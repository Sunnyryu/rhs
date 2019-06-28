package lab.web.controller;

	import java.awt.print.Printable;
	import java.io.IOException;
	import java.io.PrintWriter;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletContext;
import javax.servlet.ServletException;
	import javax.servlet.annotation.WebServlet;
	import javax.servlet.http.HttpServlet;
	import javax.servlet.http.HttpServletRequest;
	import javax.servlet.http.HttpServletResponse;
	 

	@WebServlet("/snack")
	public class SnackServlet extends HttpServlet {
	    private static final long serialVersionUID = 1L;
	    ServletContext sctx;
	    ServletContext sctx1;
	    ServletContext sctx2;
		 RequestDispatcher rd; 
		 RequestDispatcher rd1; 
		 RequestDispatcher rd2; 
	    public SnackServlet() {
	        super();
	        

	    }
	 

	    protected void doPost(HttpServletRequest request, HttpServletResponse response)
	    	    throws ServletException, IOException {
	       	request.setCharacterEncoding("utf-8");
	    	response.setContentType("text/plain;charset=utf-8");
	    	PrintWriter out = response.getWriter();
	    	 int price1 = Integer.parseInt(request.getParameter("price1"));
		     int value1 = Integer.parseInt(request.getParameter("value1"));
		     int price2 = Integer.parseInt(request.getParameter("price2"));
		     int value2 = Integer.parseInt(request.getParameter("value2"));
		     int price3 = Integer.parseInt(request.getParameter("price3"));
		     int value3 = Integer.parseInt(request.getParameter("value3"));
		     request.setAttribute("result", price1*value1);
		     request.setAttribute("result1", price2*value2);
		     request.setAttribute("result2", price3*value3);
		     sctx = request.getServletContext();
		     sctx1 = request.getServletContext();
		     sctx2 = request.getServletContext();
		    rd = sctx.getRequestDispatcher("/money.jsp");
		    rd1 = sctx1.getRequestDispatcher("/money.jsp");
		    rd2 = sctx2.getRequestDispatcher("/money.jsp");
		    rd.forward(request, response);
		    rd1.forward(request, response);
		    rd2.forward(request, response);
		     
		     
	    	
	    }
	}    
	   
	 
	 
