const gce = require('@google-cloud/compute')({
  projectID: 'projectubuntu'
});

const zone = gce.zone('us-central1-b');

console.log('getting your VMs..');

zone.getVMs().then((data) => {
  data[0].forEach((vm) => {
    console.log('found a vm called', vm.name);
    //console.log('Stooping', vm.name, '...');
    //vm.stop((err, operation) => {
    //operation.on('complete', (err) => {
    //console.log('Stopped', vm.name)});
  });
  console.log('Done');
});
