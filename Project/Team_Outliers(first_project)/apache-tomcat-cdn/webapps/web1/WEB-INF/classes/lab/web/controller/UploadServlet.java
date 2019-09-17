package lab.web.controller;

import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Collection;

import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;

@WebServlet("/upload")
@MultipartConfig(location = "C:\\apache-tomcat-9.0.21\\webapps\\web1\\uploads",
		maxFileSize=1024*1024*5, maxRequestSize=1024*1024*5*5)
public class UploadServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    public UploadServlet() {
        super();
    }

	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		
		String path = "C:\\apache-tomcat-9.0.21\\webapps\\web1\\uploads";
		File isDir = new File(path);
		if( !isDir.isDirectory()) {
			isDir.mkdirs();
		}
		
		Collection<Part> parts = request.getParts();
		for(Part part : parts) {
			if(part.getContentType() != null) {
				String fileName = part.getSubmittedFileName();
				if(fileName != null) {
					String newName = fileName.substring(0, fileName.lastIndexOf("."))
							+ "_" + System.currentTimeMillis() +
							fileName.substring(fileName.lastIndexOf("."));
					part.write(newName);
					out.print("<br>업로드한 파일 이름: " + fileName);
					out.print("<br>크기: " + part.getSize());
					out.print("<br><img src='./uploads/"+newName+"' width=300 height=200>");
					
					System.out.println("<br>업로드한 파일 이름: " + fileName);
				}
			}
			else {
				String partName = part.getName();
				String fieldValue = request.getParameter(partName);
				out.print("<br>" + partName + ": " + fieldValue);
			}
		}
		out.close();
	}

}
