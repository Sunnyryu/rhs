/*
 * Generated by the Jasper component of Apache Tomcat
 * Version: Apache Tomcat/9.0.21
 * Generated at: 2019-08-07 07:10:11 UTC
 * Note: The last modified time of this file was set to
 *       the last modified time of the source file after
 *       generation to assist with modification tracking.
 */
package org.apache.jsp.WEB_002dINF.views;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class home_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent,
                 org.apache.jasper.runtime.JspSourceImports {

  private static final javax.servlet.jsp.JspFactory _jspxFactory =
          javax.servlet.jsp.JspFactory.getDefaultFactory();

  private static java.util.Map<java.lang.String,java.lang.Long> _jspx_dependants;

  static {
    _jspx_dependants = new java.util.HashMap<java.lang.String,java.lang.Long>(4);
    _jspx_dependants.put("/WEB-INF/views/global/resources_header.jsp", Long.valueOf(1564982880000L));
    _jspx_dependants.put("jar:file:/C:/apache-tomcat-outliers/webapps/outliers/WEB-INF/lib/jstl-1.2.jar!/META-INF/c.tld", Long.valueOf(1153352682000L));
    _jspx_dependants.put("/WEB-INF/lib/jstl-1.2.jar", Long.valueOf(1563953904000L));
    _jspx_dependants.put("/WEB-INF/views/global/resources_body.jsp", Long.valueOf(1564982912000L));
  }

  private static final java.util.Set<java.lang.String> _jspx_imports_packages;

  private static final java.util.Set<java.lang.String> _jspx_imports_classes;

  static {
    _jspx_imports_packages = new java.util.HashSet<>();
    _jspx_imports_packages.add("javax.servlet");
    _jspx_imports_packages.add("javax.servlet.http");
    _jspx_imports_packages.add("javax.servlet.jsp");
    _jspx_imports_classes = null;
  }

  private volatile javax.el.ExpressionFactory _el_expressionfactory;
  private volatile org.apache.tomcat.InstanceManager _jsp_instancemanager;

  public java.util.Map<java.lang.String,java.lang.Long> getDependants() {
    return _jspx_dependants;
  }

  public java.util.Set<java.lang.String> getPackageImports() {
    return _jspx_imports_packages;
  }

  public java.util.Set<java.lang.String> getClassImports() {
    return _jspx_imports_classes;
  }

  public javax.el.ExpressionFactory _jsp_getExpressionFactory() {
    if (_el_expressionfactory == null) {
      synchronized (this) {
        if (_el_expressionfactory == null) {
          _el_expressionfactory = _jspxFactory.getJspApplicationContext(getServletConfig().getServletContext()).getExpressionFactory();
        }
      }
    }
    return _el_expressionfactory;
  }

  public org.apache.tomcat.InstanceManager _jsp_getInstanceManager() {
    if (_jsp_instancemanager == null) {
      synchronized (this) {
        if (_jsp_instancemanager == null) {
          _jsp_instancemanager = org.apache.jasper.runtime.InstanceManagerFactory.getInstanceManager(getServletConfig());
        }
      }
    }
    return _jsp_instancemanager;
  }

  public void _jspInit() {
  }

  public void _jspDestroy() {
  }

  public void _jspService(final javax.servlet.http.HttpServletRequest request, final javax.servlet.http.HttpServletResponse response)
      throws java.io.IOException, javax.servlet.ServletException {

    if (!javax.servlet.DispatcherType.ERROR.equals(request.getDispatcherType())) {
      final java.lang.String _jspx_method = request.getMethod();
      if ("OPTIONS".equals(_jspx_method)) {
        response.setHeader("Allow","GET, HEAD, POST, OPTIONS");
        return;
      }
      if (!"GET".equals(_jspx_method) && !"POST".equals(_jspx_method) && !"HEAD".equals(_jspx_method)) {
        response.setHeader("Allow","GET, HEAD, POST, OPTIONS");
        response.sendError(HttpServletResponse.SC_METHOD_NOT_ALLOWED, "JSP들은 오직 GET, POST 또는 HEAD 메소드만을 허용합니다. Jasper는 OPTIONS 메소드 또한 허용합니다.");
        return;
      }
    }

    final javax.servlet.jsp.PageContext pageContext;
    javax.servlet.http.HttpSession session = null;
    final javax.servlet.ServletContext application;
    final javax.servlet.ServletConfig config;
    javax.servlet.jsp.JspWriter out = null;
    final java.lang.Object page = this;
    javax.servlet.jsp.JspWriter _jspx_out = null;
    javax.servlet.jsp.PageContext _jspx_page_context = null;


    try {
      response.setContentType("text/html; charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;

      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("<!DOCTYPE html>\r\n");
      out.write("<html>\r\n");
      out.write("<head>\r\n");
      out.write("    <meta charset=\"utf-8\">\r\n");
      out.write("    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1, shrink-to-fit=no\">\r\n");
      out.write("    <meta name=\"description\" content=\"\">\r\n");
      out.write("    <meta name=\"author\" content=\"Mark Otto, Jacob Thornton, and Bootstrap contributors\">\r\n");
      out.write("    <meta name=\"generator\" content=\"Jekyll v3.8.5\">\r\n");
      out.write("    <!-- global resources -->\r\n");
      out.write("    ");
      out.write("\r\n");
      out.write("\r\n");
      out.write("<link rel=\"stylesheet\" href=\"/outliers/resources/bootstrap/4.3.1/dist/css/bootstrap.min.css\">\r\n");
      out.write("<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/bootstrap-slider/10.6.2/css/bootstrap-slider.min.css\">\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("    <!-- Custom styles for this template -->\r\n");
      out.write("    <link href=\"/outliers/resources/css/home.css\" rel=\"stylesheet\"> \r\n");
      out.write("    <link href=\"/outliers/resources/css/carousel.css\" rel=\"stylesheet\">\r\n");
      out.write("\r\n");
      out.write("    <title>Blindspot Finder</title>\r\n");
      out.write("</head>\r\n");
      out.write("<body>\r\n");
      out.write("  \r\n");
      out.write("\r\n");
      out.write("   \r\n");
      out.write("  <nav class=\"navbar navbar-dark fixed-top bg-dark flex-md-nowrap p-0 shadow\">\r\n");
      out.write("    <a class=\"navbar-brand col-sm-3 col-md-2 mr-0\" href=\"/outliers\">Blindspot Finder</a>\r\n");
      out.write("  </nav>\r\n");
      out.write(" \r\n");
      out.write("\r\n");
      out.write("  <main role=\"main\">\r\n");
      out.write("\r\n");
      out.write("    <div id=\"myCarousel\" class=\"carousel slide\" data-ride=\"carousel\">\r\n");
      out.write("      <ol class=\"carousel-indicators\">\r\n");
      out.write("        <li data-target=\"#myCarousel\" data-slide-to=\"0\" class=\"active\"></li>\r\n");
      out.write("        <li data-target=\"#myCarousel\" data-slide-to=\"1\"></li>\r\n");
      out.write("        <li data-target=\"#myCarousel\" data-slide-to=\"2\"></li>\r\n");
      out.write("      </ol>\r\n");
      out.write("      <div class=\"carousel-inner\">\r\n");
      out.write("        <div class=\"carousel-item active\">\r\n");
      out.write("          <img src = \"/outliers/resources/images/2.jpg\" width=\"100%\" height=\"100%\" /> \r\n");
      out.write("          <div class=\"container\">\r\n");
      out.write("            <div class=\"carousel-caption\">\r\n");
      out.write("              <h1>늦은 밤 </h1>\r\n");
      out.write("              <p>당신의 길은 안녕하신가요??</p>\r\n");
      out.write("              <p><a class=\"button-3d\" href=\"./map\" role=\"button\">start</a></p>\r\n");
      out.write("            </div>\r\n");
      out.write("          </div>\r\n");
      out.write("        </div>\r\n");
      out.write("        <div class=\"carousel-item\">\r\n");
      out.write("          <img src = \"/outliers/resources/images/3.jpg\" width=\"100%\" height=\"100%\" />        \r\n");
      out.write("        <div class=\"container\">\r\n");
      out.write("            <div class=\"carousel-caption\">\r\n");
      out.write("              <h1>CCTV가 </h1>\r\n");
      out.write("              <p>모든 구역을 지켜볼 수 없기에 ....</p>\r\n");
      out.write("              <p><a class=\"button-3d\" href=\"./map\" role=\"button\">start</a></p>\r\n");
      out.write("            </div>\r\n");
      out.write("          </div>\r\n");
      out.write("        </div>\r\n");
      out.write("        <div class=\"carousel-item\">\r\n");
      out.write("          <img src = \"/outliers/resources/images/4.jpg\" width=\"100%\" height=\"100%\" />\r\n");
      out.write("            <div class=\"container\">\r\n");
      out.write("            <div class=\"carousel-caption\">\r\n");
      out.write("               <h1>범죄사각지대 예측시스템이</h1>\r\n");
      out.write("              <p>당신의 범죄를 예방해드립니다.</p>\r\n");
      out.write("              <p><a class=\"button-3d\" href=\"./map\" role=\"button\">start</a></p>\r\n");
      out.write("            </div>\r\n");
      out.write("          </div>\r\n");
      out.write("        </div>\r\n");
      out.write("      </div>\r\n");
      out.write("      <a class=\"carousel-control-prev\" href=\"#myCarousel\" role=\"button\" data-slide=\"prev\">\r\n");
      out.write("        <span class=\"carousel-control-prev-icon\" aria-hidden=\"true\"></span>\r\n");
      out.write("        <span class=\"sr-only\">Previous</span>\r\n");
      out.write("      </a>\r\n");
      out.write("      <a class=\"carousel-control-next\" href=\"#myCarousel\" role=\"button\" data-slide=\"next\">\r\n");
      out.write("        <span class=\"carousel-control-next-icon\" aria-hidden=\"true\"></span>\r\n");
      out.write("        <span class=\"sr-only\">Next</span>\r\n");
      out.write("      </a>\r\n");
      out.write("    </div>\r\n");
      out.write("  </main>\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("  <!-- Marketing messaging and featurettes\r\n");
      out.write("  ================================================== -->\r\n");
      out.write("  <!-- Wrap the rest of the page in another container to center all the content. -->\r\n");
      out.write("\r\n");
      out.write("  <div class=\"container marketing\">\r\n");
      out.write("    <h2 style=\"text-align:center;\">기능 한눈에 보기</h2><br>\r\n");
      out.write("    <!-- Three columns of text below the carousel -->\r\n");
      out.write("    <div class=\"row\">\r\n");
      out.write("      <div class=\"col-lg-4\">\r\n");
      out.write("        <img src = \"/outliers/resources/images/5.jpg\" width=\"200px\" height=\"200px\" style=\"border-radius:50%;border:1px solid black\"  style=\"cursor: pointer;\" onclick=\"doImgPop('/outliers/resources/images/5.jpg')\" \" />\r\n");
      out.write("        <h3>1</h3>\r\n");
      out.write("        <p>검색 기능을 사용하여 해당 지역으로 이동할 수 있고 cctv와 경찰서가 지도에 표시되어 있습니다.</p>\r\n");
      out.write("     \r\n");
      out.write("      </div><!-- /.col-lg-4 -->\r\n");
      out.write("      <div class=\"col-lg-4\">\r\n");
      out.write("        <img src = \"/outliers/resources/images/6.jpg\" width=\"200px\" height=\"200px\" style=\"border-radius:50%;border:1px solid black\"  style=\"cursor: pointer;\" onclick=\"doImgPop('/outliers/resources/images/6.jpg')\" \" />\r\n");
      out.write("        <h3>2</h3>\r\n");
      out.write("        <p>방범시설을  분석하여 사각 지대로 예측이 되는 지역을 색상으로 확인 할 수 있습니다.</p>\r\n");
      out.write("        \r\n");
      out.write("      </div><!-- /.col-lg-4 -->\r\n");
      out.write("      <div class=\"col-lg-4\">\r\n");
      out.write("        <img src = \"/outliers/resources/images/7.jpg\" width=\"200px\" height=\"200px\" style=\"border-radius:50%;border:1px solid black\"  style=\"cursor: pointer;\" onclick=\"doImgPop('/outliers/resources/images/7.jpg')\" \" />\r\n");
      out.write("        <h3>3</h3>\r\n");
      out.write("        <p>각 구의 2014~ 2017년의 5대범죄 현황을 그래프 및 차트로 확인할 수 있습니다.</p>\r\n");
      out.write("        \r\n");
      out.write("      </div><!-- /.col-lg-4 -->\r\n");
      out.write("    </div><!-- /.row -->\r\n");
      out.write("  </div><!-- /.container -->\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("  <!-- global resources -->\r\n");
      out.write("  ");
      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("  <!-- Bootstrap core JavaScript\r\n");
      out.write("  ================================================== -->\r\n");
      out.write("  <!-- Placed at the end of the document so the pages load faster -->\r\n");
      out.write("  <script type=\"text/javascript\" src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js\"></script>\r\n");
      out.write("  <script type=\"text/javascript\" src=\"/outliers/resources/third-party-etc/popper.min.js\"></script>\r\n");
      out.write("  <script type=\"text/javascript\" src=\"/outliers/resources/bootstrap/4.3.1/dist/js/bootstrap.min.js\"></script>\r\n");
      out.write("  <script type=\"text/javascript\" src=\"https://use.fontawesome.com/releases/v5.2.0/js/all.js\"></script>\r\n");
      out.write("  <script type=\"text/javascript\" src=\"https://cdnjs.cloudflare.com/ajax/libs/bootstrap-slider/10.6.2/bootstrap-slider.min.js\"></script>\r\n");
      out.write("  \r\n");
      out.write("  \r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("\r\n");
      out.write("  \r\n");
      out.write("  <!-- current resources -->\r\n");
      out.write("  <script type=\"text/javascript\" src=\"/outliers/resources/js/home.js\"></script>\r\n");
      out.write("\r\n");
      out.write("</body>\r\n");
      out.write("</html>\r\n");
    } catch (java.lang.Throwable t) {
      if (!(t instanceof javax.servlet.jsp.SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          try {
            if (response.isCommitted()) {
              out.flush();
            } else {
              out.clearBuffer();
            }
          } catch (java.io.IOException e) {}
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
