package lab.spring.di.test;

import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import lab.spring.di.service.HelloService;

public class AnnotationDITest {

	public static void main(String[] args) {
		
		//Spring ioc 컨테이너 객체 생성
		AnnotationConfigApplicationContext context = 
				new AnnotationConfigApplicationContext(AppConfig.class);
		
		HelloService service = context.getBean("hello", HelloService.class);
		service.sayHello();
	}

}

