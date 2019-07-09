package lab.spring.di.service;

import lab.spring.di.persist.Message;


	

	public class HelloServiceImpl implements HelloService{
		private Message message;
		
		public HelloServiceImpl() {
			
		}
		public HelloServiceImpl(Message message) {
			
			this.message = message;
			System.out.println("생성자를 이용해서 bean 주입");
		}
		public void sayHello() {
			System.out.println(message.getMessage());
		}
//		public void setMessage(Message message) {
//			this.message = message;
//		}

		

		
}
