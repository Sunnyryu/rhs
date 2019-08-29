package lab.spring.di.test;

import org.springframework.beans.factory.xml.XmlBeanFactory;
import org.springframework.core.io.ClassPathResource;
import org.springframework.core.io.Resource;

import lab.spring.di.service.HelloService;

public class LifeCycleTest {

	public static void main(String[] args) {
		Resource resource = new ClassPathResource("application.xml");
		//Resource inferface를 받아옴.
		//spring ioc 컨테이너 객체 생성
		XmlBeanFactory beanFactory = new XmlBeanFactory(resource);
		// deprecated = 향후에 없어질 예정임.
		String beanName = "service";
		HelloService service = beanFactory.getBean("service", HelloService.class);
		// HelloService를 받아옴
		service.sayHello();
		//컨테이너로부터 빈 제거
		beanFactory.removeBeanDefinition(beanName);

	}

}
