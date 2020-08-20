## spark3

```
spark 윈도우 연산 연습 1

import org.apache.spark.streaming.StreamingContext
import org.apache.spark.streaming.Seconds
import scala.collection.mutable

val ssc = new StreamingContext(sc, Seconds(1))
ssc.checkpoint(".")
val input = for (i <- mutable.Queue(1 to 100: _*)) yield sc.parallelize(i :: Nil)
val ds = ssc.queueStream(input)
ds.window(Seconds(3), Seconds(2)).print
ssc.start
ssc.awaitTermination()

val ssc = new StreamingContext(sc, Seconds(1))
ssc.checkpoint(".")
val input = for (i <- mutable.Queue(1 to 100: _*)) yield sc.parallelize(i :: Nil)
val ds = ssc.queueStream(input)
ds.countByWindow(Seconds(3), Seconds(2)).print
ssc.start
ssc.awaitTermination()

val ssc = new StreamingContext(sc, Seconds(1))
ssc.checkpoint(".")
val input = for (i <- mutable.Queue(1 to 100: _*)) yield sc.parallelize(i :: Nil)
val ds = ssc.queueStream(input)
ds.reduceByWindow((a, b) => Math.max(a, b), Seconds(3), Seconds(2)).print
ssc.start
ssc.awaitTermination()

val ssc = new StreamingContext(sc, Seconds(1))
ssc.checkpoint(".")
val input = for (i <- mutable.Queue(1 to 100: _*)) yield sc.parallelize(i :: Nil)
val ds = ssc.queueStream(input)
ds.map( v => (v%2, 1)).reduceByKeyAndWindow((a: Int, b: Int) => a+b, Seconds(4), Seconds(2)).print
ssc.start
ssc.awaitTermination()

val ssc = new StreamingContext(sc, Seconds(1))
ssc.checkpoint(".")
val input = for (i <- mutable.Queue(1 to 100: _*)) yield sc.parallelize(i :: Nil)
val ds = ssc.queueStream(input)
ds.countByValueAndWindow(Seconds(3), Seconds(2)).print
ssc.start
ssc.awaitTermination()
```
