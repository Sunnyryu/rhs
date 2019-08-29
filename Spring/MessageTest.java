package lab.spring.di.test;

import java.util.Locale;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import lab.spring.di.service.UserService;

public class MessageTest {
	public static void main(String[] args) {
		ApplicationContext context = new ClassPathXmlApplicationContext("application.xml");
		
		Locale locale = Locale.getDefault();
		String greet = context.getMessage("greeting", new Object[0], locale);
		System.out.println("default locale 인삿말 :"+greet);
		
		Locale locale_en = Locale.ENGLISH;
		greet = context.getMessage("greeting", new Object[0], locale_en);
		System.out.println("ENGLISH locale 인삿말 :"+greet);
		
		UserService proc = context.getBean("loginService", UserService.class);
		
		String[] results = proc.login("admin", "1234");
		//String[] result = proc.login("korea", "1234");
		for (String m: results) {
			System.out.println(m);
		}
	}

}
