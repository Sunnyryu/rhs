const storage  = requrire('@google-cloud/storage')({
  projectId: 'projectubuntu'
});

const bucket = storage.bucket('my-first-bucket-abc');
bucket.getFiles()
  .on('data', (file) => {
    console.log('found a file called', file.name)
  })
  .on('end', () => {
    console.log('no more files!');
  });
