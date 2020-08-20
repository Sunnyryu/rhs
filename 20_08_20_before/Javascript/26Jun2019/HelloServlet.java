package lab.web.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.PrintWriter;
import java.io.IOException;
import javax.servlet.http.HttpServlet;
import javax.servlet.ServletException;

public class HelloServlet extends HttpServlet{
      public void init(){//override하지 않으면 부모의 init() 수행
        //서블릿이 요청되어서 컨테이너 메모리에 생성될때 1번 수행
        System.out.println("init() : 초기화");
      }
      public void service(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException{
        //서블릿의 요청시마다 반복적으로 수행
        res.setContentType("text/html;charset=utf-8");
        PrintWriter out = res.getWriter();
        out.print("<html>");
        out.print("<head><title>HelloServlet</title></head>");
        out.print("<body>");
        out.print("Hello 요청에 대한 Servlet 응답<br>");
        out.print("안녕하세요? 서블릿입니다. ^^");
        out.print("</body></html>");

      }
      public void destroy(){//override하지 않으면 부모의 init()수행
        // 서블릿이 컨테이너로부터 소멸될 때 1번만 수행
        System.out.println("destroy(): 컨테이너 종료 또는 GC될 때 수행 ");
      }
}
