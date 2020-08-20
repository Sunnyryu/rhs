package lab.hadoop.delaycount;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class DelayCountMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
	
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
					if(workType.equals("departure")){
							if(!colums[15].equals("NA")) {
								int depDelayTIme = Integer.parseInt(colums[15]);
								if(depDelayTIme > 0) {
									outputKey.set(colums[0] + "," + colums[1]);
									context.write(outputKey, outputValue);
								}
							}
				
			} else if (workType.equals("arrival")) {
				if(!colums[14].equals("NA")) {
					int arrDelayTIme = Integer.parseInt(colums[14]);
					if (arrDelayTIme > 0) {
						outputKey.set(colums[0] + "," + colums[1]);
						context.write(outputKey, outputValue);
					}	
				}
			}
				
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
	
	
	
	}
}
