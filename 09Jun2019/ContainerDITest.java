package lab.spring.di.test;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import lab.spring.di.service.HelloService;

public class ContainerDITest {

	public static void main(String[] args) {
		ApplicationContext context = new ClassPathXmlApplicationContext("application.xml");
		
		String beanName = "hello";
		HelloService service = context.getBean(beanName, HelloService.class);
		service.sayHello();
		HelloService service2 = context.getBean(beanName, HelloService.class);
		System.out.println("스프링 생성 빈이 singleton이면 동일한 객체 리턴"+(service==service2));
		// service와 service2를 비교하여 같으면 true, 틀리면 false처리!
		// scope를 주면 service 1과 service 2가 달라져서 false가 나오게 됨..	
	}

}
