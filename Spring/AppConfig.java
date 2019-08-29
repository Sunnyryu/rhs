package lab.spring.di.test;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import lab.spring.di.persist.Message;
import lab.spring.di.service.HelloService;
import lab.spring.di.service.HelloServiceImpl;

@Configuration
public class AppConfig {
	// anotation 방식으로 해서 configuration과 bean을 import해서 사용하며
	// Helloservice hello(), Message를 각각 import해서 받아서 사용함.
	@Bean
	public HelloService hello() {
		Message msg = new Message();
		HelloServiceImpl service = new HelloServiceImpl(msg);
		return service;
		
	}
}
