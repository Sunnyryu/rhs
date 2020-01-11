const bigtable  = requrire('@google-cloud/bigtable')({
  projectId: 'projectubuntu'
});

console.log('listing your instance and cluster');

bigtable.getInstance().then((data) => {
  const instances = data[0];
  for(let in instances){
    let instance = instances[i];
    console.log('- Instance', instance.id);
    instance.getClusters().then((data) => {
      const clusters = data[0]
      const cluster = clusters[0];
      console.log(' - Cluster', cluster.id);
    });
  }
});
