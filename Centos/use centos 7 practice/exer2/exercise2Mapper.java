package lab.hadoop.exercise2;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class exercise2Mapper extends Mapper<LongWritable, Text, Text, IntWritable> {
	
	private String workType;
	
	private final static IntWritable outputValue = new IntWritable(1);
	
	private Text outputKey = new Text();

	@Override
	public void setup(Context context)
			throws IOException, InterruptedException {
		workType = context.getConfiguration().get("workType");
	}
		
	
	public void map(LongWritable key, Text value, Context context) 
			throws IOException, InterruptedException {
		if (key.get()> 0) {
			String[] colums = value.toString().split(",");
			if (colums != null && colums.length > 0) {
				try {
					outputKey.set(colums[0]);
				context.write(outputKey, new IntWritable(Integer.parseInt(colums[2])));
					
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
	
	
	
	}
}

