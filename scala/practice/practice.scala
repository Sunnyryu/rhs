import scala.io.Source
import java.io.FileReader
import java.io.FileNotFoundException
import java.io.IOException

object Demo {
	def main(args: Array[String]) {
		print("Following is the content read : ")
		
		Source.fromFile("Demo.txt" ).foreach {
			print
		}


