package lab.spring.di.service;

import org.springframework.beans.BeansException;
import org.springframework.beans.factory.BeanFactory;
import org.springframework.beans.factory.BeanNameAware;
import org.springframework.beans.factory.DisposableBean;
import org.springframework.beans.factory.InitializingBean;
import org.springframework.beans.factory.NoSuchBeanDefinitionException;
import org.springframework.core.ResolvableType;

import lab.spring.di.persist.Message;

public class HelloServiceLifeCycle implements HelloService, BeanNameAware,
BeanFactory, InitializingBean, DisposableBean{
	private String name;
	private Message myMessage;
	private String beanName;
	private BeanFactory beanFactory; //스프링 컨테이너 클래스

	public HelloServiceLifeCycle() {
		super();
		System.out.println("1. default 생성자 이용한 빈 인스턴스 생성");
	}
	public void setMyMessage(Message myMessage) {
		this.myMessage = myMessage;
		System.out.println("2. 의존성 체크 후 property로 빈  인스턴스 생성");
	}

	public void setName(String name) {
		this.name = name;
		System.out.println("2-1. 의존성 체크 후 property로 빈  인스턴스 생성");
	}






	public void destroy() throws Exception{
		System.out.println("8. Inc컨테이너로부터 빈이 제거될때 정리 및 종료 수행 메서드");
	}
	public void custom_end() {
		System.out.println("9. Inc컨테이너로부터 빈이 제거될때 정리 및 종료 및 정리 수행 메서드 (컨테이너에 독립적인...)");
	}
	public void afterPropertiesSet() throws Exception{
		System.out.println("5. 모든 property가 설정된 후 유효성 체크등의 수행하기 위한 용도");
	}
	public void custom_init() {
		System.out.println("6. 사용자 정의 초기화 메서드(스프링 컨테이너에 독립적인...)");
	}
	public void setBeanFactory(BeanFactory arg0) throws BeansException {
		System.out.println("4. 스프링 컨테이너 객체 주입");
		this.beanFactory = arg0;
	}

	public void setBeanName(String arg0) {
		System.out.println("3. 설정 파일에서의 빈 이름을 주입");
		this.beanName = arg0;
		System.out.println("주인받은 빈 이름 :"+beanName);
	}

	public String getName() {
		return name;
	}
	public void sayHello() {//서비스 메서드
		System.out.println("7. 빈의 서비스 메서드 호출");
		System.out.println(myMessage.getMessage()+"from"+name);
	}


	public Object getBean(String name) throws BeansException {
		// TODO Auto-generated method stub
		return null;
	}


	public <T> T getBean(String name, Class<T> requiredType) throws BeansException {
		// TODO Auto-generated method stub
		return null;
	}


	public Object getBean(String name, Object... args) throws BeansException {
		// TODO Auto-generated method stub
		return null;
	}


	public <T> T getBean(Class<T> requiredType) throws BeansException {
		// TODO Auto-generated method stub
		return null;
	}


	public <T> T getBean(Class<T> requiredType, Object... args) throws BeansException {
		// TODO Auto-generated method stub
		return null;
	}


	public boolean containsBean(String name) {
		// TODO Auto-generated method stub
		return false;
	}


	public boolean isSingleton(String name) throws NoSuchBeanDefinitionException {
		// TODO Auto-generated method stub
		return false;
	}


	public boolean isPrototype(String name) throws NoSuchBeanDefinitionException {
		// TODO Auto-generated method stub
		return false;
	}


	public boolean isTypeMatch(String name, ResolvableType typeToMatch) throws NoSuchBeanDefinitionException {
		// TODO Auto-generated method stub
		return false;
	}


	public boolean isTypeMatch(String name, Class<?> typeToMatch) throws NoSuchBeanDefinitionException {
		// TODO Auto-generated method stub
		return false;
	}


	public Class<?> getType(String name) throws NoSuchBeanDefinitionException {
		// TODO Auto-generated method stub
		return null;
	}


	public String[] getAliases(String name) {
		// TODO Auto-generated method stub
		return null;
	}




}
