package lab.hadoop.sort;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.output.MultipleOutputs;

public class DelayCountReduceWithDateKey extends Reducer<DateKey, IntWritable, DateKey, IntWritable>{

	private MultipleOutputs<DateKey, IntWritable> mos;
	
	private DateKey outputKey = new DateKey();
	
	private IntWritable result = new IntWritable();

	@Override
	public void setup(Context context)
			throws IOException, InterruptedException {
		mos = new MultipleOutputs<DateKey, IntWritable>(context);
	}
	public void reduce(DateKey key, Iterable<IntWritable> values, Context context) throws IOException,
		InterruptedException {
		
		String[] colums = key.getYear().split(",");
		
		int sum = 0;
		Integer bMonth = key.getMonth();
		
		if(colums[0].equals("D")) {
			for(IntWritable value : values) {
				if (bMonth != key.getMonth()) {
					result.set(sum);
					outputKey.setYear(key.getYear().substring(2));
					outputKey.setMonth(bMonth);
					mos.write("departure", outputKey, result);
					sum = 0;
				}
				sum += value.get();
				bMonth = key.getMonth();
		}
			if (key.getMonth() == bMonth) {
				outputKey.setYear(key.getYear().substring(2));
				outputKey.setMonth(key.getMonth());
				result.set(sum);
				mos.write("departure", outputKey, result);
			}
		} else {
			for(IntWritable value : values) {
				if(bMonth != key.getMonth()) {
					result.set(sum);
					outputKey.setYear(key.getYear().substring(2));
					outputKey.setMonth(bMonth);
					mos.write("arrival", outputKey, result);
					sum= 0;
				}
				sum += value.get();
				bMonth = key.getMonth();
			}
			if (key.getMonth() == bMonth) {
				outputKey.setYear(key.getYear().substring(2));
				outputKey.setMonth(key.getMonth());
				result.set(sum);
				mos.write("arrival", outputKey, result);
			}
		}
	}
	
	@Override
	protected void cleanup(Context context)
			throws IOException, InterruptedException {
		mos.close();
	}
}
